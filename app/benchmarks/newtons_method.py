import taichi as ti

@ti.func
def function(x: ti.f64) -> ti.f64:
    return 2.12*x ** 3 - 6.23*x ** 2 + 4.63*x - 3.14159265359

@ti.func
def derivative(x: ti.f64) -> ti.f64:
    return 6.36*x ** 2 - 12.46*x + 4.63

@ti.kernel
def newtons_method_1T() -> ti.f64:
    x = 100_000.0
    ti.loop_config(serialize=True)
    for _ in range(100_000_000):
        x = x - function(x) / derivative(x)
    return x