import taichi as ti

@ti.kernel
def pi_calc_1T() -> ti.f64:
    n = 100_000_000
    pi = 0.0
    ti.loop_config(serialize=True)
    for i in range(n):
        pi += ((1/16) ** i) * ((4 / (8 * i + 1)) - (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6)))
    return pi

@ti.kernel
def pi_calc_nT() -> ti.f64:
    n = 100_000_000
    pi = 0.0
    for i in range(n):
        pi += ((1/16) ** i) * ((4 / (8 * i + 1)) - (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6)))
    return pi