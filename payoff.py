from math import sqrt


def lp(p: float, p0: float, n: float):
    return n * sqrt(p / p0)


def income_lp(p: float, p0: float, k: float, n: float):
    K = lp(k, p0, n)
    return min(lp(p, p0, n), K) + (100 - K)


def income_vanilla(p: float, protection: float, gearing: float, notional: float):
    K = 100
    H = K - protection
    G = gearing
    N = notional
    if p >= H:
        return N
    else:
        x = N - G * H
        return x + G * p


def growth_lp(p: float, protection, p0: float, participation: float, notional: float):
    K = 100
    H = K - protection
    L = participation
    N = notional
    if p >= H:
        return N + L * max(lp(p, K, N) - N, 0)
    else:
        K = lp(H, p0, N)
        return min(lp(p, p0, N), K) + (100 - K)


def growth_vanilla(p: float, protection: float, gearing: float, participation: float, notional: float):
    K = 100
    H = K - protection
    G = gearing
    L = participation
    N = notional
    if p >= H:
        return N + L * max(lp(p, K, N) - N, 0)
    else:
        x = N - G * H
        return x + G * p
