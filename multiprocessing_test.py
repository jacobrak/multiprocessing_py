import multiprocessing 
import time
import random

class Process(multiprocessing.Process): 
    def __init__(self, id): 
        super(Process, self).__init__() 
        self.id = id
                 
    def run(self): 
        time.sleep(0.1)
        print("I'm the process with id: {}".format(self.id))
        random_func()



def random_func():
    # Just for time reference
    total_sum = 0

    for i in range(10000000):
        total_sum += i * random.randint(1, 100)


if __name__ == '__main__': 
    start = time.time()
    # Start both processes
    p1 = Process(0)
    p2 = Process(1)
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    end = time.time()
    print(f"Took me in parallel: {end - start:.2f} seconds")

    start = time.time()
    random_func()
    random_func()
    end = time.time()
    print(f"Took me normally: {end - start:.2f} seconds")