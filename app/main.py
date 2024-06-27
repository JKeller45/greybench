import taichi as ti
ti.init(arch=ti.cpu, default_fp=ti.f64, default_ip=ti.i64)

from timeit import default_timer as timer  # noqa: E402
from benchmarks.factoring import factor_loop  # noqa: E402

def main():
    start = timer()
    factor_loop()
    end = timer()
    print(f"Factoring time: {end - start:.6f} s")
    

if __name__ == "__main__":
    main()