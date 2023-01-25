from time import perf_counter

def cycle_example():
    result = 0
    numbers = [num for num in range(1_000_000)]

    for num in numbers:
        result += num
    print(result)

def sum_example():
    numbers = [num for num in range(1_000_000)]
    print(sum(numbers))

if __name__ == "__main__":
    start = perf_counter()
    cycle_example()
    print(f"time cycle_example(): {(perf_counter() - start):.02f}")

    start = perf_counter()
    sum_example()
    print(f"time sum_example(): {(perf_counter() - start):.02f}")













