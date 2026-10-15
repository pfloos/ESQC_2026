"""Render real solid-harmonic Gaussian isosurfaces on PubChem porphine.

Run from the repository root:
  blender --background --python scripts/render_basis_cover.py -- --quick
No generative image or retouched raster is used. NumPy is bundled with Blender.
"""

import argparse
import json
import math
from pathlib import Path
import sys

import numpy as np
try:
    import bpy
    from mathutils import Vector
except ImportError:
    bpy = None

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "drafts/cover-studies"
STEM = "06-porphine-exact-gaussians"
# Entries are coefficient, Cartesian powers. Coordinates are local to each atom.
FUNCTIONS = [
    ("s", 14, 2.00, [(1, (0, 0, 0))]),
    ("p_z", 8, 3.00, [(1, (0, 0, 1))]),
    ("d_xy", 19, 3.00, [(1, (1, 1, 0))]),
    ("f_z(x2-y2)", 5, 4.20, [(1, (2, 0, 1)), (-1, (0, 2, 1))]),
    ("g_xy(x2-y2)", 21, 5.20, [(1, (3, 1, 0)), (-1, (1, 3, 0))]),
]


def moment(power, beta):
    if power % 2:
        return 0.0
    n = power // 2
    odd = math.prod(range(1, 2 * n, 2))
    return odd * math.sqrt(math.pi) / (2**n * beta ** (n + 0.5))


def normalization(poly, alpha):
    integral = 0.0
    for a, pa in poly:
        for b, pb in poly:
            integral += a * b * math.prod(moment(i + j, 2 * alpha)
                                          for i, j in zip(pa, pb))
    return integral ** -0.5


def evaluate(points, poly, alpha, norm):
    value = np.zeros(points.shape[:-1])
    for coefficient, powers in poly:
        term = np.full(points.shape[:-1], float(coefficient))
        for axis, power in enumerate(powers):
            term *= points[..., axis] ** power
        value += term
    return norm * value * np.exp(-alpha * np.sum(points**2, axis=-1))


def check_harmonic(poly):
    laplacian = {}
    for coefficient, powers in poly:
        for axis, n in enumerate(powers):
            if n >= 2:
                p = list(powers)
                p[axis] -= 2
                key = tuple(p)
                laplacian[key] = laplacian.get(key, 0) + coefficient*n*(n-1)
    assert all(c == 0 for c in laplacian.values()), laplacian


def gradient_at(points, poly, alpha, norm):
    result = np.zeros_like(points)
    for axis in range(3):
        derivative = []
        for coefficient, powers in poly:
            if powers[axis]:
                new = list(powers)
                new[axis] -= 1
                derivative.append((coefficient*powers[axis],tuple(new)))
        result[:,axis] = evaluate(points,derivative,alpha,norm) - 2*alpha*points[:,axis]*evaluate(points,poly,alpha,norm)
    return result


def check_functions():
    nodes,weights = np.polynomial.hermite.hermgauss(12)
    triples = np.stack(np.meshgrid(nodes,nodes,nodes,indexing="ij"),axis=-1)
    w = weights[:,None,None]*weights[None,:,None]*weights[None,None,:]
    for name,_,alpha,poly in FUNCTIONS:
        check_harmonic(poly)
        norm = normalization(poly,alpha)
        q = triples / math.sqrt(2*alpha)
        # Independent Gauss-Hermite integral of the squared polynomial.
        polynomial = sum(c*np.prod(q**np.array(p),axis=-1) for c,p in poly)
        integral = norm**2*np.sum(w*polynomial**2)/(2*alpha)**1.5
        assert abs(integral-1)<1e-12, (name,integral)
        for c,p in poly:
            assert sum(p)==sum(poly[0][1])
    # Exact nodal planes for the selected p,d,f,g components.
    q = np.array([[.3,.3,.7],[.3,-.3,.7],[.3,.6,0]])
    for index,rows in [(1,[2]),(3,[0,1,2]),(4,[0,1])]:
        _,_,alpha,poly=FUNCTIONS[index]
        assert np.max(np.abs(evaluate(q[rows],poly,alpha,normalization(poly,alpha))))<1e-14
    print("Five pure-angular harmonic polynomials, unit norms, and selected nodal planes passed.",flush=True)


def isosurface(points, values, level, poly, alpha, norm, sign):
    """March six consistently tiled tetrahedra per cube, then weld vertices."""
    n = values.shape[0]
    i, j, k = np.indices((n-1, n-1, n-1))
    base = ((i*n+j)*n+k).ravel()
    offsets = np.array([0, n*n, n*n+n, n, 1, n*n+1, n*n+n+1, n+1])
    cubes = base[:, None] + offsets
    flat_points, flat_values = points.reshape(-1, 3), values.ravel()
    triangles = []
    for tet in [(0,1,2,6), (0,2,3,6), (0,3,7,6),
                (0,7,4,6), (0,4,5,6), (0,5,1,6)]:
        ids = cubes[:, tet]
        samples = flat_values[ids]
        codes = np.sum((samples > level) * (1 << np.arange(4)), axis=1)
        for code in range(1, 15):
            use = codes == code
            if not np.any(use):
                continue
            xyz, v = flat_points[ids[use]], samples[use]
            inside = [a for a in range(4) if code & (1 << a)]
            outside = [a for a in range(4) if not code & (1 << a)]

            def edge(a, b):
                fraction = (level-v[:, a]) / (v[:, b]-v[:, a])
                return xyz[:, a] + fraction[:, None]*(xyz[:, b]-xyz[:, a])

            if len(inside) in (1, 3):
                a, others = (inside[0], outside) if len(inside) == 1 else (outside[0], inside)
                triangles.append(np.stack([edge(a,b) for b in others], axis=1))
            else:
                a,b = inside
                c,d = outside
                ac,ad,bc,bd = edge(a,c),edge(a,d),edge(b,c),edge(b,d)
                triangles.extend([np.stack([ac,ad,bd],axis=1),
                                  np.stack([ac,bd,bc],axis=1)])
    triangles = np.concatenate(triangles)
    center = triangles.mean(axis=1)
    gradient = []
    for axis in range(3):
        delta = np.zeros(3)
        delta[axis] = 1e-5
        gradient.append(sign*(evaluate(center+delta,poly,alpha,norm)-
                              evaluate(center-delta,poly,alpha,norm)))
    gradient = np.stack(gradient,axis=1)
    normal = np.cross(triangles[:,1]-triangles[:,0], triangles[:,2]-triangles[:,0])
    flip = np.sum(normal*gradient,axis=1) > 0
    triangles[flip] = triangles[flip][:,[0,2,1]]
    vertices, inverse = np.unique(triangles.reshape(-1,3).round(8),axis=0,return_inverse=True)
    # Project interpolated vertices onto the analytic level set. Connectivity
    # remains that of the tetrahedral extraction; no artistic reshaping occurs.
    for _ in range(5):
        residual = sign*evaluate(vertices,poly,alpha,norm)-level
        grad = sign*gradient_at(vertices,poly,alpha,norm)
        vertices -= residual[:,None]*grad/np.sum(grad**2,axis=1)[:,None]
    error = np.max(np.abs(sign*evaluate(vertices,poly,alpha,norm)-level))
    assert error/level < 1e-8, error/level
    return vertices, inverse.reshape(-1,3), float(error/level)


def material(name, color, alpha=1.0, metallic=0.0):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, alpha)
    mat.use_nodes = True
    shader = mat.node_tree.nodes.get("Principled BSDF")
    shader.inputs["Base Color"].default_value = (*color, 1)
    shader.inputs["Roughness"].default_value = 0.25
    shader.inputs["Metallic"].default_value = metallic
    shader.inputs["Alpha"].default_value = alpha
    return mat


def mesh_lobes(vertices, faces):
    edges=np.concatenate([faces[:,[0,1]],faces[:,[1,2]],faces[:,[2,0]]])
    edges.sort(axis=1)
    edges,counts=np.unique(edges,axis=0,return_counts=True)
    assert np.all(counts==2), "Each isosurface must be closed and manifold"
    parent=list(range(len(vertices)))

    def root(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]
            a=parent[a]
        return a

    for a,b in edges:
        ra,rb=root(int(a)),root(int(b))
        parent[rb]=ra
    count=len({root(i) for i in range(len(vertices))})
    assert len(vertices)-len(edges)+len(faces)==2*count
    return count


def sphere(name, center, radius, mat):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=20,
                                      radius=radius, location=center)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    for face in obj.data.polygons:
        face.use_smooth = True


def cylinder(name, start, end, radius, mat):
    delta = Vector(end)-Vector(start)
    bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=radius,
                                      depth=delta.length,
                                      location=(Vector(start)+Vector(end))/2)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = delta.to_track_quat("Z", "Y").to_euler()
    obj.data.materials.append(mat)
    for face in obj.data.polygons:
        face.use_smooth = True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--opaque-preview", action="store_true")
    options = parser.parse_args(sys.argv[sys.argv.index("--")+1:] if "--" in sys.argv else [])
    check_functions()
    if options.check:
        return
    if bpy is None:
        raise RuntimeError("Rendering requires Blender; numerical checks need only NumPy")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = 24 if options.quick else 80
    scene.cycles.use_denoising = True
    scene.render.resolution_x = 1600 if options.quick else 2400
    scene.render.resolution_y = 1100 if options.quick else 1650
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = True
    scene.view_settings.view_transform = "AgX"
    scene.world.use_nodes = True
    scene.world.node_tree.nodes["Background"].inputs[0].default_value = (0.87,0.94,0.91,1)
    scene.world.node_tree.nodes["Background"].inputs[1].default_value = 0.65
    if options.opaque_preview:
        scene.cycles.samples=32
        scene.render.resolution_x=1600
        scene.render.resolution_y=1100
        scene.render.film_transparent=False
        # Separate camera background from environment illumination. This is a
        # fresh scene render, not a painted or retouched raster background.
        nodes=scene.world.node_tree.nodes
        links=scene.world.node_tree.links
        light_path=nodes.new("ShaderNodeLightPath")
        backdrop=nodes.new("ShaderNodeBackground")
        backdrop.inputs[0].default_value=(0.92,1.0,0.97,1)
        backdrop.inputs[1].default_value=5.0
        mix=nodes.new("ShaderNodeMixShader")
        links.new(light_path.outputs["Is Camera Ray"],mix.inputs[0])
        links.new(nodes["Background"].outputs[0],mix.inputs[1])
        links.new(backdrop.outputs[0],mix.inputs[2])
        links.new(mix.outputs[0],nodes["World Output"].inputs[0])
    carbon = material("carbon", (0.09,0.105,0.11), metallic=0.15)
    nitrogen = material("nitrogen", (0.025,0.12,0.65), metallic=0.1)
    hydrogen = material("hydrogen", (0.9,0.91,0.87))
    bond_mat = material("bonds", (0.19,0.23,0.24), metallic=0.3)
    positive = material("positive function: emerald", (0.008,0.36,0.22), alpha=0.84)
    negative = material("negative function: amber", (0.9,0.34,0.025), alpha=0.84)
    raw = json.loads((OUT/"porphine-pubchem-3d.json").read_text())["PC_Compounds"][0]
    assert raw["id"]["id"]["cid"] == 66868
    atoms, bonds = raw["atoms"], raw["bonds"]
    conformer = raw["coords"][0]["conformers"][0]
    xyz = np.column_stack([conformer[key] for key in ("x","y","z")])
    xyz -= xyz.mean(axis=0)
    # Orient in the best-fit heavy-atom molecular plane, retaining distortions.
    heavy = xyz[np.array(atoms["element"]) != 1]
    _,_,axes = np.linalg.svd(heavy-heavy.mean(axis=0))
    if np.linalg.det(axes) < 0:
        axes[2] *= -1
    xyz = xyz @ axes.T
    positions = dict(zip(atoms["aid"],xyz))
    assert atoms["element"].count(6)==20 and atoms["element"].count(7)==4 and atoms["element"].count(1)==14
    for aid, element in zip(atoms["aid"],atoms["element"]):
        sphere(f"atom_{aid}",positions[aid],{1:.15,6:.25,7:.26}[element],
               {1:hydrogen,6:carbon,7:nitrogen}[element])
    for a,b,order in zip(bonds["aid1"],bonds["aid2"],bonds["order"]):
        start,end = positions[a],positions[b]
        tangent = end-start
        sideways = np.cross(tangent,[0,0,1])
        sideways /= np.linalg.norm(sideways)
        shifts = [-.085,.085] if order==2 else [0]
        for number,shift in enumerate(shifts):
            cylinder(f"bond_{a}_{b}_{number}",start+sideways*shift,end+sideways*shift,
                     .048 if order==2 else .063,bond_mat)
    metadata = {"source":"https://pubchem.ncbi.nlm.nih.gov/compound/66868",
                "cid":66868,"formula":"C20H14N4","units":"angstrom for source coordinates; inverse-square angstrom for alpha",
                "grid_n":89,"positive":"emerald","negative":"amber","functions":[]}
    axis = np.linspace(-2,2,89)
    points = np.stack(np.meshgrid(axis,axis,axis,indexing="ij"),axis=-1)
    for name,aid,alpha,poly in FUNCTIONS:
        check_harmonic(poly)
        norm = normalization(poly,alpha)
        values = evaluate(points,poly,alpha,norm)
        peak = float(np.max(np.abs(values)))
        level = .20*peak
        boundary = np.concatenate([values[0].ravel(),values[-1].ravel(),values[:,0].ravel(),
                                   values[:,-1].ravel(),values[:,:,0].ravel(),values[:,:,-1].ravel()])
        assert np.max(np.abs(boundary)) < level
        meshes=[]
        for sign,mat in [(1,positive),(-1,negative)]:
            if np.max(sign*values) <= level:
                continue
            vertices,faces,residual = isosurface(points,sign*values,level,poly,alpha,norm,sign)
            lobes=mesh_lobes(vertices,faces)
            expected={"s":1,"p_z":1,"d_xy":2,"f_z(x2-y2)":4,"g_xy(x2-y2)":4}[name]
            assert lobes==expected,(name,sign,lobes)
            mesh = bpy.data.meshes.new(f"{name}_{sign}")
            mesh.from_pydata(vertices.tolist(),[],faces.tolist())
            mesh.update()
            obj = bpy.data.objects.new(f"{name}_atom_{aid}_sign_{sign}",mesh)
            scene.collection.objects.link(obj)
            obj.location = positions[aid]
            obj.data.materials.append(mat)
            for face in mesh.polygons:
                face.use_smooth=True
            meshes.append({"sign":sign,"lobes":lobes,"triangles":len(faces),"max_relative_isovalue_error":residual})
        metadata["functions"].append({"name":name,"atom_id":aid,"alpha":alpha,
                                      "polynomial":poly,"normalization":norm,"isovalue":level,
                                      "center":positions[aid].tolist(),"meshes":meshes})
    bpy.ops.object.camera_add(location=(3,-15,12))
    camera=bpy.context.object
    camera.rotation_euler=(Vector((0,0,0))-camera.location).to_track_quat("-Z","Y").to_euler()
    camera.data.type="ORTHO"
    camera.data.ortho_scale=14.2
    scene.camera=camera
    for name,location,power,size in [("key",(-6,-6,12),1500,8),("fill",(7,3,9),1100,7)]:
        bpy.ops.object.light_add(type="AREA",location=location)
        light=bpy.context.object
        light.name=name
        light.data.energy=power
        light.data.shape="DISK"
        light.data.size=size
        light.rotation_euler=(-light.location).to_track_quat("-Z","Y").to_euler()
    scene.render.filepath=str(OUT/(STEM+("-review" if options.opaque_preview else "")+".png"))
    if not options.opaque_preview:
        bpy.context.preferences.filepaths.save_version=0
        bpy.ops.wm.save_as_mainfile(filepath=str(OUT/(STEM+".blend")),compress=True)
        (OUT/(STEM+".json")).write_text(json.dumps(metadata,indent=2)+"\n")
    bpy.ops.render.render(write_still=True)
    print("Exact normalized Gaussian meshes rendered; harmonic-polynomial and mesh-residual checks passed.")


if __name__ == "__main__":
    main()
