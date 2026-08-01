import multiprocessing
import math
import time


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

    start = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(is_prime, num_list)

    end_time = time.time() - start

    final_results = dict(zip(num_list, results))

    print("--- Results ---")
    for num, status in final_results.items():
        result_text = "Prime" if status else "Composite"
        print(f"Number {num}: {result_text}")

    print(f"\nExecution time: {end_time:.4f} seconds")
