#!/usr/bin/env python3
"""Independent small-tensor checks for the MP2/AO-to-MO/Laplace addition.

Uses only the standard library. This checks algebra and contraction order,
not the accuracy of a particular molecule or the efficiency of a production
implementation. The Laplace integral is evaluated after t=-log(u), mapping
the positive half-line to 0<u<1 without an arbitrary tail cutoff.
"""

from itertools import combinations, product
from math import exp


def close(actual, expected, label, tolerance=1e-10):
    assert abs(actual - expected) < tolerance, (label, actual, expected)


def main():
    k = 4
    indices = range(k)
    c = ((0.5, 0.5, 0.5, 0.5), (0.5, -0.5, 0.5, -0.5),
         (0.5, 0.5, -0.5, -0.5), (0.5, -0.5, -0.5, 0.5))
    kernel = ((1.2, 0.2, 0.1, 0.15), (0.2, 1.4, 0.3, 0.12),
              (0.1, 0.3, 1.1, 0.25), (0.15, 0.12, 0.25, 1.3))
    # AO functions are orthonormal delta functions on four grid points.
    ao = {(m, n, l, s): kernel[m][l] if m == n and l == s else 0.0
          for m, n, l, s in product(indices, repeat=4)}
    naive = {(p, q, r, s): sum(c[m][p]*c[n][q]*c[l][r]*c[v][s]*ao[m, n, l, v]
                               for m, n, l, v in product(indices, repeat=4))
             for p, q, r, s in product(indices, repeat=4)}
    first = {(m, n, l, s): sum(c[v][s]*ao[m, n, l, v] for v in indices)
             for m, n, l, s in product(indices, repeat=4)}
    second = {(m, n, r, s): sum(c[l][r]*first[m, n, l, s] for l in indices)
              for m, n, r, s in product(indices, repeat=4)}
    third = {(m, q, r, s): sum(c[n][q]*second[m, n, r, s] for n in indices)
             for m, q, r, s in product(indices, repeat=4)}
    final = {(p, q, r, s): sum(c[m][p]*third[m, q, r, s] for m in indices)
             for p, q, r, s in product(indices, repeat=4)}
    for quartet in naive:
        close(final[quartet], naive[quartet], "four quarter-transformations")

    eps = (-1.5, -1.0, 0.5, 1.0)
    occupied, virtual = (0, 1), (2, 3)
    rhf = 0.0
    for i, j, a, b in product(occupied, occupied, virtual, virtual):
        direct, exchange = naive[i, a, j, b], naive[i, b, j, a]
        denominator = eps[i]+eps[j]-eps[a]-eps[b]
        rhf += (2*direct*direct-direct*exchange)/denominator

    occ_spin = list(product(occupied, (0, 1)))
    vir_spin = list(product(virtual, (0, 1)))
    def antisym(i, j, a, b, weights=None):
        p, spin_p = i
        q, spin_q = j
        r, spin_r = a
        s, spin_s = b
        direct = naive[p, r, q, s] if spin_p == spin_r and spin_q == spin_s else 0.0
        exchange = naive[p, s, q, r] if spin_p == spin_s and spin_q == spin_r else 0.0
        value = direct-exchange
        if weights is not None:
            value *= weights[p]*weights[q]*weights[r]*weights[s]
        return value

    terms = []
    for i, j, a, b in product(occ_spin, occ_spin, vir_spin, vir_spin):
        gap = eps[a[0]]+eps[b[0]]-eps[i[0]]-eps[j[0]]
        assert gap > 0
        g = antisym(i, j, a, b)
        terms.append((g*g, gap))
        for t in (0.0, 0.3, 2.1):
            weights = [exp(eps[p]*t/2) if p in occupied else exp(-eps[p]*t/2)
                       for p in indices]
            dressed = antisym(i, j, a, b, weights)
            close(dressed, g*exp(-gap*t/2), "dressed integral exponent")
            close(dressed*dressed, g*g*exp(-gap*t), "squared damping exponent")

    spin_energy = -0.25*sum(numerator/gap for numerator, gap in terms)
    close(spin_energy, rhf, "spin-orbital versus RHF MP2 factors and index conversion")
    ordered_energy = 0.0
    for i, j in combinations(occ_spin, 2):
        for a, b in combinations(vir_spin, 2):
            gap = eps[a[0]]+eps[b[0]]-eps[i[0]]-eps[j[0]]
            ordered_energy -= antisym(i, j, a, b)**2/gap
    close(ordered_energy, spin_energy, "unordered pairs versus one-quarter factor")
    assert spin_energy < -1e-5, "test must have a nonzero correlation energy"

    def integrand(u):
        return -0.25*sum(numerator*u**(gap-1) for numerator, gap in terms)
    intervals = 1000
    integral = (integrand(0.0)+integrand(1.0)+sum(
        (4 if n % 2 else 2)*integrand(n/intervals) for n in range(1, intervals))) / (3*intervals)
    close(integral, spin_energy, "independent Laplace quadrature", tolerance=1e-9)
    print(f"AO-to-MO: all {k**4} integrals agree between direct and four-stage contractions")
    print(f"MP2: RHF, unrestricted spin sums, and unordered pairs agree ({rhf:.12f})")
    print(f"Laplace: orbital exponents/sign and numerical integral agree (error {abs(integral-spin_energy):.2e})")


if __name__ == "__main__":
    main()
