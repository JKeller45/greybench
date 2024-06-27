import taichi as ti

factors = ti.field(ti.i64, shape=100)

@ti.func
def factorize(n: ti.i64):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            factors[0] = i
            n //= i
            break
    cnt = 1
    while n > 1:
        if n % i:
            i += 1
        else:
            factors[cnt] = i
            n //= i
            cnt += 1
    return cnt

@ti.kernel
def factor_loop_1T():
    ti.loop_config(serialize=True)
    for num in range(100000):
        factorize(num)

@ti.kernel
def factor_loop_nT():
    for num in range(100000):
        factorize(num)