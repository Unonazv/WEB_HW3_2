import multiprocessing
import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(numbers):
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(factorize, numbers)
    end_time = time.time()
    duration = end_time - start_time
    return results, duration

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    print("Synchronous execution:")
    sync_start_time = time.time()
    for num in numbers:
        factors = factorize(num)
    sync_end_time = time.time()
    sync_duration = sync_end_time - sync_start_time
    print(f"Total synchronous execution time: {sync_duration:.5f} seconds")

    print("\nParallel execution:")
    factors, parallel_duration = factorize_parallel(numbers)
    for num, factors_list in zip(numbers, factors):
        print(f"Factors of {num}: {factors_list}")
    print(f"Parallel execution time: {parallel_duration:.5f} seconds")