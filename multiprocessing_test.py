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
    p3 = Process(2)
    p4 = Process(3)
    p5 = Process(4)
    p6 = Process(5)
    p7 = Process(6) # I only have 6 cores should slow down

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.stat()
    # Wait 
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    
    end = time.time()
    print(f"Took me in parallel: {end - start:.2f} seconds")

    start = time.time()
    random_func()
    random_func()
    end = time.time()
    print(f"Took me normally: {end - start:.2f} seconds")