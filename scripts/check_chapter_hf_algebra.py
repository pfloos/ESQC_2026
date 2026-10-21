#!/usr/bin/env python3
"""Small independent checks of the chapter's HF conventions (standard library).

These finite-dimensional examples check identities, not the accuracy of a
molecular calculation. They also retain counterexamples for two audit findings:
real integral values do not imply real orbitals, and a bra conjugates its
coefficients. No chapter formulas are generated or edited by this script.
"""

import cmath
from itertools import permutations
from math import cos, factorial, isclose, pi, sin, sqrt


def close(actual, expected, description, tolerance=1e-10):
    assert abs(actual - expected) < tolerance, (description, actual, expected)


def determinant_normalization():
    for n in (2, 3, 4):
        # Orthogonal Kronecker-delta orbitals: the only nonzero amplitudes
        # occur at permutations of their n distinct coordinate labels.
        norm = 0.0
        for p in permutations(range(n)):
            inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
            amplitude = (-1) ** inversions / sqrt(factorial(n))
            norm += amplitude ** 2
        close(norm, 1.0, f"{n}-electron determinant norm")


def energy_and_koopmans():
    # Three real spatial functions on three quadrature points, with a
    # symmetric positive-definite interaction matrix. Orthonormality is not
    # needed for the pair-counting identities tested here.
    phi = ((1.0, 0.2, -0.3), (0.4, 1.1, 0.5), (-0.2, 0.7, 0.9))
    kernel = ((1.2, 0.2, 0.1), (0.2, 1.4, 0.3), (0.1, 0.3, 1.1))
    h = (-1.7, -0.8, 0.2)

    def eri(a, b, c, d):
        return sum(phi[x][a] * phi[x][b] * kernel[x][y] * phi[y][c] * phi[y][d]
                   for x in range(3) for y in range(3))

    def pair(i, j):
        p, spin_p = i
        q, spin_q = j
        return eri(p, p, q, q) - (eri(p, q, q, p) if spin_p == spin_q else 0)

    def energy(occupied):
        return sum(h[p] for p, _ in occupied) + 0.5 * sum(
            pair(i, j) for i in occupied for j in occupied)

    rhf = [(p, s) for p in (0, 1) for s in (0, 1)]
    spatial = 2 * sum(h[p] for p in (0, 1)) + sum(
        2 * eri(p, p, q, q) - eri(p, q, q, p) for p in (0, 1) for q in (0, 1))
    close(energy(rhf), spatial, "RHF spin sum and factors of two")
    li = [(0, 0), (0, 1), (1, 0)]
    close(energy(li), 2 * h[0] + h[1] + eri(0, 0, 0, 0)
          + 2 * eri(0, 0, 1, 1) - eri(0, 1, 1, 0), "lithium pair count")
    boron = rhf + [(2, 0)]
    close(energy(boron), spatial + h[2] + sum(
        2 * eri(p, p, 2, 2) - eri(p, 2, 2, p) for p in (0, 1)), "boron pair count")

    for occupied in (rhf, li, boron):
        eps = lambda orbital: h[orbital[0]] + sum(pair(orbital, j) for j in occupied)
        e = energy(occupied)
        # Spin-resolved density traces: each occupied spin orbital counts once.
        # The one-half spin sum recovers both one-body and pair contributions.
        close(0.5 * sum(h[p] + eps((p, spin)) for p, spin in occupied), e,
              "UHF summary: one-half spin-density/Fock energy trace")
        for k in occupied:
            remaining = [j for j in occupied if j != k]
            close(energy(remaining) - e, -eps(k), "frozen removal / IP sign")
        for a in [(p, s) for p in range(3) for s in (0, 1) if (p, s) not in occupied]:
            close(e - energy(occupied + [a]), -eps(a), "frozen attachment / EA sign")
        interaction = sum(pair(i, j) for i in occupied for j in occupied)
        close(e, sum(eps(i) for i in occupied) - 0.5 * interaction,
              "orbital-energy double-counting correction")

    # Exact decompositions: independent synthetic relaxation/correlation shifts.
    e_n, eps_k, eps_a = -10.0, -0.6, 0.1
    frozen_minus, frozen_plus = e_n - eps_k, e_n + eps_a
    relaxed_minus, relaxed_plus = frozen_minus - 0.08, frozen_plus - 0.12
    corr_n, corr_minus, corr_plus = -0.3, -0.2, -0.45
    close((relaxed_minus + corr_minus) - (e_n + corr_n),
          -eps_k + (relaxed_minus - frozen_minus) + (corr_minus - corr_n),
          "exact IP relaxation/correlation decomposition")
    close((e_n + corr_n) - (relaxed_plus + corr_plus),
          -eps_a + (frozen_plus - relaxed_plus) + (corr_n - corr_plus),
          "exact EA relaxation/correlation decomposition")


def completed_exercise_contractions():
    """Check added AO-energy steps and unrestricted lithium independently."""
    n = 3
    basis = [[1.1, .2+.1j, -.1j], [0, .9, .15], [0, 0, 1.2]]
    h = [[-1.3, .1j, .2], [-.1j, -.5, .1], [.2, .1, .4]]
    interaction = [[1.2, .3, .2], [.3, 1.4, .4], [.2, .4, 1.1]]

    def inner(u, v):
        return sum(a.conjugate()*b for a, b in zip(u, v))

    def to_grid(c):
        return [sum(basis[x][mu]*c[mu] for mu in range(n)) for x in range(n)]

    def one(u, v):
        return sum(u[x].conjugate()*h[x][y]*v[y]
                   for x in range(n) for y in range(n))

    def eri(u, v, w, z):
        return sum(u[x].conjugate()*v[y].conjugate()*interaction[x][y]*w[x]*z[y]
                   for x in range(n) for y in range(n))

    # Gram--Schmidt in the physical grid, while retaining nonorthogonal AO
    # coefficients. This avoids assuming the density/trace identity tested.
    coefficients, orbitals = [], []
    for seed in ([.7+.1j, .2-.3j, .4], [.1-.2j, .6, -.3+.2j]):
        c = seed[:]
        for old_c, old_orbital in zip(coefficients, orbitals):
            overlap = inner(old_orbital, to_grid(c))
            c = [a-overlap*b for a, b in zip(c, old_c)]
        length = sqrt(inner(to_grid(c), to_grid(c)).real)
        c = [a/length for a in c]
        coefficients.append(c)
        orbitals.append(to_grid(c))
    for i in range(2):
        for j in range(2):
            close(inner(orbitals[i], orbitals[j]), int(i == j), "exercise orbital normalization")

    p = [[sum(c[mu]*c[nu].conjugate() for c in coefficients)
          for nu in range(n)] for mu in range(n)]
    assert max(abs(x.imag) for row in p for x in row) > .01
    aos = [[basis[x][mu] for x in range(n)] for mu in range(n)]
    h_ao = [[one(u, v) for v in aos] for u in aos]
    g_ao = [[sum(p[sigma][lam]*(eri(aos[mu], aos[lam], aos[nu], aos[sigma])
                               -eri(aos[mu], aos[lam], aos[sigma], aos[nu]))
                 for lam in range(n) for sigma in range(n))
             for nu in range(n)] for mu in range(n)]
    for mu in range(n):
        for nu in range(n):
            direct = sum(eri(aos[mu], w, aos[nu], w)-eri(aos[mu], w, w, aos[nu])
                         for w in orbitals)
            close(g_ao[mu][nu], direct, "Fock exercise: Coulomb/exchange index order")
    e1 = sum(one(v, v) for v in orbitals)
    e2 = .5*sum(eri(v, w, v, w)-eri(v, w, w, v)
                 for v in orbitals for w in orbitals)
    close(sum(p[nu][mu]*h_ao[mu][nu] for mu in range(n) for nu in range(n)),
          e1, "AO exercise: one-electron density contraction")
    close(.5*sum(p[nu][mu]*g_ao[mu][nu] for mu in range(n) for nu in range(n)),
          e2, "AO exercise: two-electron density contraction")
    close(.5*sum(p[nu][mu]*(2*h_ao[mu][nu]+g_ao[mu][nu])
                 for mu in range(n) for nu in range(n)),
          e1+e2, "AO exercise: complex nonorthogonal trace energy")
    for mu in range(n):
        for lam in range(n):
            for nu in range(n):
                for sigma in range(n):
                    direct = sum(ci[mu].conjugate()*cj[lam].conjugate()*ci[nu]*cj[sigma]
                                 for ci in coefficients for cj in coefficients)
                    close(direct, p[nu][mu]*p[sigma][lam],
                          "AO exercise: four coefficients become two densities")

    alpha1, alpha2 = orbitals
    beta = [1/sqrt(3), cmath.exp(.3j)/sqrt(3), cmath.exp(-.4j)/sqrt(3)]
    assert abs(inner(alpha1, beta)) > .1
    for beta1 in (beta, alpha1):
        occupied = [(alpha1, 0), (alpha2, 0), (beta1, 1)]
        direct = sum(one(v, v) for v, _ in occupied)
        for i, (v, spin_v) in enumerate(occupied):
            for w, spin_w in occupied[i+1:]:
                direct += eri(v, w, v, w)
                if spin_v == spin_w:
                    direct -= eri(v, w, w, v)
        same_spin = eri(alpha1, alpha2, alpha1, alpha2)-eri(alpha1, alpha2, alpha2, alpha1)
        mixed_spin = eri(alpha1, beta1, alpha1, beta1)+eri(alpha2, beta1, alpha2, beta1)
        expanded = one(alpha1, alpha1)+one(alpha2, alpha2)+one(beta1, beta1)+same_spin+mixed_spin
        close(direct, expanded, "UHF lithium: three distinct pairs")
        if beta1 is alpha1:
            restricted = (2*one(alpha1, alpha1)+one(alpha2, alpha2)
                          +eri(alpha1, alpha1, alpha1, alpha1)
                          +2*eri(alpha1, alpha2, alpha1, alpha2)
                          -eri(alpha1, alpha2, alpha2, alpha1))
            close(expanded, restricted, "UHF lithium: common-spatial-orbital limit")
    print("Completed exercises: complex AO coefficient/density contractions and unrestricted lithium limits passed")


def complex_counterexamples():
    # Physicists' periodic plane-wave ERIs, with the zero mode removed.
    # All values below are real, although the functions exp(i k x) are complex.
    def pw(i, j, k, l):
        return 0.0 if i + j != k + l or i == k else 1.0 / (i - k) ** 2

    g = pw(0, 3, 1, 2)
    close(g, pw(3, 0, 2, 1), "electron-interchange symmetry")
    close(g, pw(1, 2, 0, 3), "Hermitian integral symmetry")
    assert not isclose(g, pw(1, 3, 0, 2)), "real values do not give eightfold symmetry"

    c = (sqrt(0.6), sqrt(0.4) * cmath.exp(0.7j))
    h = ((-1.0, 0.2), (0.2, 0.4))
    direct = sum(c[i].conjugate() * h[i][j] * c[j] for i in range(2) for j in range(2))
    density = [[c[i] * c[j].conjugate() for j in range(2)] for i in range(2)]
    trace = sum(density[j][i] * h[i][j] for i in range(2) for j in range(2))
    close(trace, direct, "complex density trace order")
    close(direct.imag, 0, "Hermitian expectation is real")
    double_conjugated = sum(c[i] * h[i][j] * c[j] for i in range(2) for j in range(2))
    assert abs(double_conjugated - direct) > 0.1
    print(f"  Real-valued plane-wave ERIs: {g:g} != {pw(1, 3, 0, 2):g} after extra permutation")
    print(f"  Correct bra expectation: {direct.real:.8f}; double-conjugated: {double_conjugated:.8f}")


def spin_adaptation():
    # Order: i-alpha, i-beta, a-alpha, a-beta. Retain fermionic phases.
    def act(vector, orbital, create):
        result = {}
        for bits, coefficient in vector.items():
            present = bool(bits & (1 << orbital))
            if present == create:
                continue
            sign = (-1) ** (bits & ((1 << orbital) - 1)).bit_count()
            new = bits ^ (1 << orbital)
            result[new] = result.get(new, 0) + sign * coefficient
        return result

    def add(*vectors):
        result = {}
        for vector in vectors:
            for bits, coefficient in vector.items():
                result[bits] = result.get(bits, 0) + coefficient
        return result

    def flip(vector, raising):
        return add(*(act(act(vector, p + (1 if raising else 0), False),
                              p + (0 if raising else 1), True) for p in (0, 2)))

    def s2(vector):
        zz = {}
        for bits, coefficient in vector.items():
            ms = 0.5 * sum((1 if p % 2 == 0 else -1) for p in range(4) if bits & (1 << p))
            zz[bits] = ms * ms * coefficient
        transverse = add(flip(flip(vector, False), True), flip(flip(vector, True), False))
        return add(zz, {bits: 0.5 * v for bits, v in transverse.items()})

    ref = {0b0011: 1.0}
    determinants = [act(act(ref, 0, False), 2, True), act(act(ref, 1, False), 3, True)]
    expected = ((1, -1), (-1, 1))
    for i, bra in enumerate(determinants):
        for j, ket in enumerate(determinants):
            operated = s2(ket)
            close(sum(v * operated.get(bits, 0) for bits, v in bra.items()), expected[i][j],
                  "spin-adapted single-excitation phase convention")


def h2_curvature():
    hg, hu, jg, ju, jgu, kgu = -1.2, -0.4, 0.7, 0.6, 0.3, 0.1
    a = jgu - 2 * kgu
    def energy(theta):
        x = cos(theta) ** 2
        return 2*x*hg + 2*(1-x)*hu + x*x*jg + (1-x)**2*ju + 2*x*(1-x)*a
    step = 1e-3
    numeric = (energy(step) - 2*energy(0) + energy(-step)) / step**2
    close(numeric, 4*(hu-hg-jg+jgu-2*kgu), "H2 restricted curvature", tolerance=4e-6)
    for theta in (0.0, 0.2, 0.6):
        close(1 - cos(2*theta)**2, sin(2*theta)**2, "two-electron UHF spin contamination")


def orbital_derivative():
    # Discrete spatial/spin coordinates: the polynomial energy is defined
    # off the orthonormal manifold, as required for a functional derivative.
    orbitals = [[0.7+0.1j, 0.2-0.3j, -0.1+0.4j, 0.3],
                [0.1-0.2j, 0.6+0.1j, 0.2, -0.4+0.2j]]
    h = ((-1.0, 0, 0.2, 0), (0, -1.0, 0, 0.2),
         (0.2, 0, -0.3, 0), (0, 0.2, 0, -0.3))
    kernel = ((1.2, 0.4), (0.4, 1.1))
    def interaction(x, y):
        return kernel[x // 2][y // 2]

    def energy(c):
        one = sum(v[x].conjugate()*h[x][y]*v[y]
                  for v in c for x in range(4) for y in range(4))
        coulomb = 0.5*sum(abs(v[x])**2*interaction(x, y)*abs(w[y])**2
                          for v in c for w in c for x in range(4) for y in range(4))
        exchange = -0.5*sum(v[x].conjugate()*w[x]*interaction(x, y)*w[y].conjugate()*v[y]
                             for v in c for w in c for x in range(4) for y in range(4))
        return one.real, coulomb, exchange.real

    step = 1e-6
    for i, v in enumerate(orbitals):
        for x in range(4):
            one = sum(h[x][y]*v[y] for y in range(4))
            coulomb = sum(abs(w[y])**2*interaction(x, y)*v[x]
                          for w in orbitals for y in range(4))
            exchange = -sum(w[x]*w[y].conjugate()*interaction(x, y)*v[y]
                             for w in orbitals for y in range(4))
            for direction in (1, 1j):
                plus, minus = [w[:] for w in orbitals], [w[:] for w in orbitals]
                plus[i][x] += step*direction
                minus[i][x] -= step*direction
                for a, b, gradient in zip(energy(plus), energy(minus), (one, coulomb, exchange)):
                    close((a-b)/(2*step), 2*(direction.conjugate()*gradient).real,
                          "separate one-electron/Coulomb/exchange orbital derivatives", tolerance=2e-9)


def operator_unitary_invariance():
    """Test total operators separately from their occupied-basis matrices."""
    def adjoint(a):
        return [[complex(a[j][i]).conjugate() for j in range(len(a))]
                for i in range(len(a[0]))]

    def multiply(a, b):
        return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
                 for j in range(len(b[0]))] for i in range(len(a))]

    def difference(a, b):
        return max(abs(x-y) for ra, rb in zip(a, b) for x, y in zip(ra, rb))

    def check(a, b, label):
        close(difference(a, b), 0.0, label)

    c = [[0.5*cmath.exp(0.5j*pi*mu*i) for i in range(2)] for mu in range(4)]
    phase, theta = cmath.exp(0.7j), 0.41
    u = [[cos(theta), -phase.conjugate()*sin(theta)],
         [phase*sin(theta), cos(theta)]]
    identity = [[1, 0], [0, 1]]
    check(multiply(adjoint(c), c), identity, "occupied orthonormality")
    check(multiply(adjoint(u), u), identity, "U dagger U")
    check(multiply(u, adjoint(u)), identity, "U U dagger")
    rotated = multiply(c, u)
    check(multiply(rotated, adjoint(rotated)), multiply(c, adjoint(c)),
          "complex occupied projector invariance")

    # A finite quadrature model of the Coulomb and nonlocal exchange kernels.
    interaction = [[1.3, .4, .2, .15], [.4, 1.5, .3, .1],
                   [.2, .3, 1.7, .25], [.15, .1, .25, 1.9]]
    h = [[-1.2, .1j, .2, 0], [-.1j, -.6, 0, .1],
         [.2, 0, .3, -.15j], [0, .1, .15j, .8]]

    def orbital_operators(v):
        j = [[sum(abs(v[z])**2*interaction[x][z] for z in range(4))
              if x == y else 0 for y in range(4)] for x in range(4)]
        k = [[v[x]*v[y].conjugate()*interaction[x][y]
              for y in range(4)] for x in range(4)]
        return j, k

    def totals(coefficients):
        individual = [orbital_operators(v) for v in zip(*coefficients)]
        j, k = [[[sum(pair[t][x][y] for pair in individual)
                  for y in range(4)] for x in range(4)] for t in range(2)]
        f = [[h[x][y]+j[x][y]-k[x][y] for y in range(4)] for x in range(4)]
        return j, k, f

    g = [[.3+.2j], [-.4j], [.7], [-.1+.5j]]
    original, transformed = totals(c), totals(rotated)
    for a, b, label in zip(original, transformed, ("Coulomb", "exchange", "Fock")):
        check(a, b, f"total {label} operator invariance")
        check(multiply(a, g), multiply(b, g), f"{label} action on arbitrary function")
    first = orbital_operators([row[0] for row in c])
    first_rotated = orbital_operators([row[0] for row in rotated])
    for a, b in zip(first, first_rotated):
        assert difference(a, b) > 0.01, "individual orbital contributions change"

    f_oo = multiply(multiply(adjoint(c), original[2]), c)
    rotated_f_oo = multiply(multiply(adjoint(rotated), transformed[2]), rotated)
    check(rotated_f_oo, multiply(multiply(adjoint(u), f_oo), u),
          "occupied Fock block transforms by unitary similarity")
    assert difference(f_oo, rotated_f_oo) > 0.01, "matrix entries need not be invariant"
    print("Operator invariance: complex occupied rotations preserve total J, K, F; individual contributions and MO entries change")


def density_and_residual_exercises():
    """Check AO metric, RHF factors, and residual blocks in a complex basis.

    B embeds nonorthogonal AOs in an independent orthonormal reference
    space. Transforming operators and orbitals separately avoids assuming
    the metric identities that are being tested.
    """
    def adjoint(a):
        return [[complex(a[j][i]).conjugate() for j in range(len(a))]
                for i in range(len(a[0]))]

    def multiply(a, b):
        return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
                 for j in range(len(b[0]))] for i in range(len(a))]

    def scale(a, factor):
        return [[factor*x for x in row] for row in a]

    def subtract(a, b):
        return [[x-y for x, y in zip(row_a, row_b)]
                for row_a, row_b in zip(a, b)]

    def norm(a):
        return max(abs(x) for row in a for x in row)

    def check_matrix(a, b, label):
        close(norm(subtract(a, b)), 0.0, label)

    def trace(a):
        return sum(a[i][i] for i in range(len(a)))

    def inverse(a):
        n = len(a)
        rows = [[complex(x) for x in row] + [complex(i == j) for j in range(n)]
                for i, row in enumerate(a)]
        for k in range(n):
            pivot = max(range(k, n), key=lambda i: abs(rows[i][k]))
            rows[k], rows[pivot] = rows[pivot], rows[k]
            divisor = rows[k][k]
            rows[k] = [x/divisor for x in rows[k]]
            for i in range(n):
                if i != k:
                    factor = rows[i][k]
                    rows[i] = [x-factor*y for x, y in zip(rows[i], rows[k])]
        return [row[n:] for row in rows]

    b = [[1.2, 0.2+0.1j, -0.1j], [0, 0.9, 0.25], [0, 0, 1.1]]
    s = multiply(adjoint(b), b)
    angle, phase = 0.37, cmath.exp(0.4j)
    u = [[cos(angle), -sin(angle), 0],
         [phase*sin(angle), phase*cos(angle), 0],
         [0, 0, cmath.exp(-0.3j)]]
    c = multiply(inverse(b), u)
    identity = [[int(i == j) for j in range(3)] for i in range(3)]
    check_matrix(multiply(multiply(adjoint(c), s), c), identity, "S-orthonormal MOs")

    def density(occupied, weight=1):
        co = [row[:occupied] for row in c]
        return scale(multiply(co, adjoint(co)), weight)

    for occupied in (1, 2):
        p = density(occupied)
        check_matrix(adjoint(p), p, "single-spin Hermiticity")
        close(trace(multiply(p, s)), occupied, "single-spin electron count")
        check_matrix(multiply(multiply(p, s), p), p, "single-spin metric idempotency")
        ps = multiply(p, s)
        check_matrix(multiply(ps, ps), ps, "coefficient-space projector")
        # Integrate density in the independent orthonormal reference space.
        close(trace(multiply(multiply(b, p), adjoint(b))), occupied,
              "real-space density integral")
        assert norm(subtract(multiply(p, p), p)) > 1e-3
        assert abs(trace(p)-occupied) > 1e-3
        rhf = scale(p, 2)
        close(trace(multiply(rhf, s)), 2*occupied, "RHF electron count")
        check_matrix(multiply(multiply(rhf, s), rhf), scale(rhf, 2),
                     "RHF metric idempotency factor of two")

    alpha, beta = density(2), density(1)
    charge = [[a+z for a, z in zip(ra, rb)] for ra, rb in zip(alpha, beta)]
    close(trace(multiply(charge, s)), 3, "unequal collinear spin populations")
    assert norm(subtract(multiply(multiply(charge, s), charge), scale(charge, 2))) > 0.1

    f_mo = [[-1.1, 0.2+0.15j, -0.1j],
            [0.2-0.15j, -0.4, 0.3+0.1j], [0.1j, 0.3-0.1j, 0.6]]
    f_ref = multiply(multiply(u, f_mo), adjoint(u))
    f = multiply(multiply(adjoint(b), f_ref), b)

    def residual(fock, p):
        return subtract(multiply(multiply(fock, p), s),
                        multiply(multiply(s, p), fock))

    # With N^alpha=2 and N^beta=1, mixing only the first two MOs leaves
    # the alpha occupied space invariant but not the beta occupied space.
    # Convergence of one spin channel is therefore insufficient.
    f_partial_mo = [[-1.1, 0.2+0.15j, 0],
                    [0.2-0.15j, -0.4, 0], [0, 0, 0.6]]
    f_partial = multiply(multiply(adjoint(b),
                         multiply(multiply(u, f_partial_mo), adjoint(u))), b)
    close(norm(residual(f_partial, alpha)), 0.0,
          "UHF summary: vanishing alpha residual")
    assert norm(residual(f_partial, beta)) > 0.1

    for occupied in (1, 2):
        p = density(occupied, 2)
        e = residual(f, p)
        check_matrix(adjoint(e), scale(e, -1), "anti-Hermitian AO residual")
        e_mo = multiply(multiply(adjoint(c), e), c)
        occupations = [2 if i < occupied else 0 for i in range(3)]
        expected = [[(occupations[j]-occupations[i])*f_mo[i][j]
                     for j in range(3)] for i in range(3)]
        check_matrix(e_mo, expected, "occupied-virtual residual factors/signs")
        p_mo = multiply(multiply(multiply(multiply(adjoint(c), s), p), s), c)
        check_matrix(p_mo, [[occupations[i] if i == j else 0 for j in range(3)]
                            for i in range(3)], "MO density transformation")

    # A stationary non-Aufbau occupied space still has zero residual.
    diagonal = [[(0.7, -1.1, -0.4)[i] if i == j else 0 for j in range(3)]
                for i in range(3)]
    f_stationary = multiply(multiply(adjoint(b),
                           multiply(multiply(u, diagonal), adjoint(u))), b)
    close(norm(residual(f_stationary, density(1, 2))), 0.0,
          "zero residual does not select Aufbau occupation")

    # Exact diagonalization gives a mixed-iteration zero even when P changes.
    f_old = multiply(multiply(adjoint(b), diagonal), b)
    c_new = inverse(b)
    co_new = [row[:1] for row in c_new]
    p_new = scale(multiply(co_new, adjoint(co_new)), 2)
    assert norm(residual(f_old, density(1, 2))) > 0.1
    close(norm(residual(f_old, p_new)), 0.0, "mixed-iteration residual vanishes")
    assert norm(subtract(p_new, density(1, 2))) > 0.1

    # One-electron-level RHF model: energy plateaus and both curvature signs.
    for occupied_energy, virtual_energy in ((-1.0, 0.5), (0.5, -1.0)):
        energy = lambda q: 2*(occupied_energy*cos(q)**2 + virtual_energy*sin(q)**2)
        step = 1e-3
        curvature = (energy(step)-2*energy(0)+energy(-step))/step**2
        close(curvature, 4*(virtual_energy-occupied_energy),
              "stable versus unstable stationary curvature", tolerance=3e-6)
        q, tiny_step = 0.2, 1e-10
        gradient = 4*(virtual_energy-occupied_energy)*sin(q)*cos(q)
        assert abs(energy(q+tiny_step)-energy(q)) < 1e-8
        assert abs(gradient) > 0.1
    print("Density/SCF exercises: complex AO metric, spin factors, projector, residual blocks, mixed iterations, and stability passed")


if __name__ == "__main__":
    determinant_normalization()
    energy_and_koopmans()
    completed_exercise_contractions()
    complex_counterexamples()
    spin_adaptation()
    h2_curvature()
    orbital_derivative()
    operator_unitary_invariance()
    density_and_residual_exercises()
    print("HF algebra checks passed: normalization, spin sums, pair counts, IP/EA, complex conventions, CSF phases, H2, orbital derivatives")
