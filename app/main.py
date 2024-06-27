import taichi as ti
ti.init(arch=ti.cpu, default_fp=ti.f64, default_ip=ti.i64)

from timeit import default_timer as timer  # noqa: E402
from benchmarks.factoring import factor_loop_1T, factor_loop_nT  # noqa: E402
from benchmarks.pi_calc import pi_calc_1T, pi_calc_nT  # noqa: E402\
from benchmarks.newtons_method import newtons_method_1T  # noqa: E402

single_threaded_tests = [factor_loop_1T, pi_calc_1T, newtons_method_1T]
multi_threaded_tests = [factor_loop_nT, pi_calc_nT]

def main():
    single_threaded_times = {}
    multi_threaded_times = {}

    for test in single_threaded_tests:
        start = timer()
        test()
        single_threaded_times[test.__name__] = timer() - start

    for test in multi_threaded_tests:
        start = timer()
        test()
        multi_threaded_times[test.__name__] = timer() - start

    print(f"Single-threaded time: {sum(single_threaded_times.values()):.6f}s")
    print(f"Multi-threaded time: {sum(multi_threaded_times.values()):.6f}s")
    print(f"Speedup: {sum(single_threaded_times.values()) / sum(multi_threaded_times.values()):.6f}\n--------------------------------------------------\n")
    
    print(single_threaded_times)
    print(multi_threaded_times)

if __name__ == "__main__":
    main()