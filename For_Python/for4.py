import random
from time import perf_counter


USERS_BUY = [
    ("confirmed", 100),
    ("unconfirmed", 500),
    ("confirmed", 900)
]

def fill_users_list():
    global USERS_BUY
    temp = [("confirmed", random.randint(10, 200)) for user in range(1_000_000)]
    USERS_BUY += temp


def cycle_example():
    res = 0

    for user in USERS_BUY:
        if user[0] == "confirmed":
            res += user[1]
    print(res)


def list_example():
    balance_list = [user[1] for user in USERS_BUY if user[0] == "confirmed"]
    res = sum(balance_list)
    print(res)


def generator_example():
    balance_list = (user[1] for user in USERS_BUY if user[0] == "confirmed")
    res = sum(balance_list)
    print(res)

if __name__ == "__main__":
    fill_users_list()

    start = perf_counter()
    fill_users_list()
    print(f"time fill_users_list(): {(perf_counter() - start):.02f}")

    start = perf_counter()
    cycle_example()
    print(f"time cycle_example(): {(perf_counter() - start):.02f}")

    start = perf_counter()
    list_example()
    print(f"time list_example(): {(perf_counter() - start):.02f}")

    start = perf_counter()
    generator_example()
    print(f"time generator_example(): {(perf_counter() - start):.02f}")