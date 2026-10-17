#!/usr/bin/env python3
"""Small independent checks of the chapter's HF conventions (standard library).

These finite-dimensional examples check identities, not the accuracy of a
molecular calculation. They also retain counterexamples for two audit findings:
real integral values do not imply real orbitals, and a bra conjugates its
coefficients. No chapter formulas are generated or edited by this script.
"""

import cmath
from itertools import permutations
from math import cos, factorial, isclose, sin, sqrt


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


if __name__ == "__main__":
    determinant_normalization()
    energy_and_koopmans()
    complex_counterexamples()
    spin_adaptation()
    h2_curvature()
    print("HF algebra checks passed: normalization, spin sums, pair counts, IP/EA, complex conventions, CSF phases, H2")
