"""Independent numerical checks of the chapter's OS recurrences and RI algebra.

Run with Python 3; no third-party packages are required. The reference ERIs
are integrated from Gaussian conditional moments, rather than OS recurrences.
All primitives are unnormalized, as in the chapter.
"""

import math
import random


def integrate(fn, intervals=800):
    return sum(
        (1 if k in (0, intervals) else 4 if k % 2 else 2)
        * fn(k / intervals)
        for k in range(intervals + 1)
    ) / (3 * intervals)


def check_close(actual, expected, description):
    error = abs(actual - expected) / max(1.0, abs(expected))
    assert error < 2e-8, (description, actual, expected, error)
    return error


def check_os():
    rng = random.Random(2026)
    worst = 0.0
    checks = 0
    for sample in range(12):
        alpha, beta, gamma, delta = [rng.uniform(0.4, 1.8) for _ in range(4)]
        centers = [[rng.uniform(-1.0, 1.0) for _ in range(3)] for _ in range(4)]
        A, B, C, D = centers
        zeta, eta = alpha + beta, gamma + delta
        theta = zeta * eta / (zeta + eta)
        P = [(alpha * a + beta * b) / zeta for a, b in zip(A, B)]
        Q = [(gamma * c + delta * d) / eta for c, d in zip(C, D)]
        kab = math.exp(-alpha * beta / zeta * sum((a-b)**2 for a, b in zip(A, B)))
        kcd = math.exp(-gamma * delta / eta * sum((c-d)**2 for c, d in zip(C, D)))
        prefactor = 2 * math.pi**2.5 * kab * kcd / (zeta * eta * math.sqrt(zeta + eta))
        T = theta * sum((p-q)**2 for p, q in zip(P, Q))
        for axis in range(3):
            pa, qc, pq = P[axis] - A[axis], Q[axis] - C[axis], P[axis] - Q[axis]

            def reference(a, c, m):
                def integrand(u):
                    mean_a = pa - eta / (zeta + eta) * pq * u*u
                    mean_c = qc + zeta / (zeta + eta) * pq * u*u
                    if (a, c) == (0, 0):
                        moment = 1.0
                    elif (a, c) == (1, 0):
                        moment = mean_a
                    elif (a, c) == (0, 1):
                        moment = mean_c
                    elif (a, c) == (2, 0):
                        moment = mean_a**2 + (1 - eta/(zeta+eta)*u*u)/(2*zeta)
                    elif (a, c) == (0, 2):
                        moment = mean_c**2 + (1 - zeta/(zeta+eta)*u*u)/(2*eta)
                    elif (a, c) == (1, 1):
                        moment = mean_a * mean_c + u*u/(2*(zeta+eta))
                    else:
                        raise ValueError((a, c))
                    return u**(2*m) * math.exp(-T*u*u) * moment
                return prefactor * integrate(integrand)

            for m in range(3):
                s = reference(0, 0, m)
                snext = reference(0, 0, m+1)
                p = pa*s - eta/(zeta+eta)*pq*snext
                q = qc*s + zeta/(zeta+eta)*pq*snext
                d = pa*reference(1, 0, m) - eta/(zeta+eta)*pq*reference(1, 0, m+1)
                d += (s - eta/(zeta+eta)*snext)/(2*zeta)
                e = qc*reference(0, 1, m) + zeta/(zeta+eta)*pq*reference(0, 1, m+1)
                e += (s - zeta/(zeta+eta)*snext)/(2*eta)
                mixed = qc*reference(1, 0, m) + zeta/(zeta+eta)*pq*reference(1, 0, m+1)
                mixed += snext/(2*(zeta+eta))
                for result, a, c in [(p,1,0), (q,0,1), (d,2,0), (e,0,2), (mixed,1,1)]:
                    worst = max(worst, check_close(result, reference(a,c,m), (sample,axis,m,a,c)))
                    checks += 1
    print(f"OS: {checks} moment-integral checks passed; largest scaled error {worst:.2e}")


def check_ri():
    # Euclidean coordinates represent a positive Coulomb metric after whitening.
    # A nonorthogonal, incomplete auxiliary space tests actual projection error.
    auxiliary = [(1.0, 0.3, 0.0), (0.2, 1.2, 0.0)]
    densities = [(0.7, -0.4, 0.2), (-0.2, 0.9, 0.5), (1.1, 0.6, -0.3)]
    dot = lambda a, b: sum(x*y for x,y in zip(a,b))
    V = [[dot(a,b) for b in auxiliary] for a in auxiliary]
    determinant = V[0][0]*V[1][1] - V[0][1]*V[1][0]
    inverse = [[V[1][1]/determinant, -V[0][1]/determinant],
               [-V[1][0]/determinant, V[0][0]/determinant]]
    fits, three_center = [], []
    for rho in densities:
        g = [dot(a,rho) for a in auxiliary]
        coefficients = [dot(row,g) for row in inverse]
        fit = [sum(coefficients[j]*auxiliary[j][i] for j in range(2)) for i in range(3)]
        residual = [r-f for r,f in zip(rho,fit)]
        for a in auxiliary:
            check_close(dot(a,residual), 0.0, "Coulomb orthogonality")
        fits.append(fit)
        three_center.append(g)
    for i, rho in enumerate(densities):
        for j, other in enumerate(densities):
            factored = sum(three_center[i][a]*inverse[a][b]*three_center[j][b]
                           for a in range(2) for b in range(2))
            check_close(factored, dot(fits[i],fits[j]), "three-index contraction")
            check_close(factored, dot(rho,fits[j]), "one-sided projection")
            ri_error = dot(rho,other) - factored
            residual_i = [r-f for r,f in zip(rho,fits[i])]
            residual_j = [r-f for r,f in zip(other,fits[j])]
            check_close(ri_error, dot(residual_i,residual_j), "residual interaction")
    print("RI: orthogonality, fitted-pair equality, metric contraction, and residual error passed")


def check_ghf():
    # Arbitrary complex occupied spinors in a real two-function AO basis.
    occupied = [(0.5+0.2j, -0.3+0.4j, 0.1-0.7j, 0.6+0.1j),
                (0.2-0.1j, 0.4+0.5j, -0.2+0.3j, 0.1+0.8j)]
    full = [[sum(c[i]*c[j].conjugate() for c in occupied) for j in range(4)] for i in range(4)]
    blocks = [[[full[2*s+i][2*t+j] for j in range(2)] for i in range(2)]
              for s in range(2) for t in range(2)]
    aa, ab, ba, bb = blocks
    charge = [[(aa[i][j]+bb[i][j])/2 for j in range(2)] for i in range(2)]
    mx = [[(ab[i][j]+ba[i][j])/2 for j in range(2)] for i in range(2)]
    my = [[(ba[i][j]-ab[i][j])/(2j) for j in range(2)] for i in range(2)]
    mz = [[(aa[i][j]-bb[i][j])/2 for j in range(2)] for i in range(2)]
    pauli = [((0,1),(1,0)), ((0,-1j),(1j,0)), ((1,0),(0,-1))]
    for s in range(2):
        for t in range(2):
            for i in range(2):
                for j in range(2):
                    reconstructed = (charge[i][j] if s==t else 0)
                    reconstructed += sum(sigma[s][t]*moment[i][j] for sigma,moment in zip(pauli,(mx,my,mz)))
                    check_close(reconstructed, full[2*s+i][2*t+j], "spin-first tensor order")
    # Discretize the real-space nonlocal exchange kernel independently.
    phi = ((1.0,0.2), (0.4,1.1), (-0.2,0.7))
    coulomb = ((2.0,0.8,0.4), (0.8,1.5,0.6), (0.4,0.6,1.8))
    def eri(mu,nu,lam,sig):
        return sum(phi[x][mu]*phi[x][nu]*coulomb[x][y]*phi[y][lam]*phi[y][sig]
                   for x in range(3) for y in range(3))
    for density in blocks:
        for mu in range(2):
            for nu in range(2):
                contracted = sum(density[lam][sig]*eri(mu,lam,sig,nu)
                                 for lam in range(2) for sig in range(2))
                kernel = sum(phi[x][mu]*phi[y][nu]*coulomb[x][y]
                             * sum(phi[x][lam]*density[lam][sig]*phi[y][sig]
                                   for lam in range(2) for sig in range(2))
                             for x in range(3) for y in range(3))
                check_close(contracted, kernel, "complex-density exchange kernel")
    print("GHF: spin/AO tensor ordering and complex-density exchange contraction passed")


if __name__ == "__main__":
    check_os()
    check_ri()
    check_ghf()
