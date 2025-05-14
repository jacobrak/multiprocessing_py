import threading
import time
import random

def time_test():
    time.sleep(5)
    print("Wow 5 seconds!")


def random_calculation(num):
    result = 50000**random.randint(9**2,9**3)*num
    time.sleep(1)
    print("Done!")
    return result

def single():
    time.sleep(5)
    print("Wow 5 seconds!")
    random_calculation(2)

if __name__ == "__main__":
    start = time.time()
    t1 = threading.Thread(target=time_test)
    t2 = threading.Thread(target=random_calculation, args=(2, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end = time.time()
    print(f"Done time: {end -start}")

    start = time.time()
    single()
    end = time.time()
    print(f"Done time: {end -start}")