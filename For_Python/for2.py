from time import perf_counter

def index_access():
    temp = 0
    numbers = [num for num in range(1_000_000)]

    for num in range(len(numbers)):
        temp += numbers[num]
    print(temp)


def enumerate_example():
    temp = 0
    numbers = [num for num in range(1_000_000)]

    for index, num in enumerate(numbers):
        temp = num
    print(temp)


if __name__ == "__main__":
    start = perf_counter()
    index_access()
    print(f"time index_access(): {(perf_counter() - start):.02f}")

    start = perf_counter()
    enumerate_example()
    print(f"time enumerate_example(): {(perf_counter() - start):.02f}")