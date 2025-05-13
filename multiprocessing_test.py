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



def random_func(input=1):
    # Just for time reference
    total_sum = 0

    for i in range(10000000):
        total_sum += i * random.randint(1, 100)*input
    
    return total_sum

if __name__ == '__main__': 
    start = time.time()
    pool = multiprocessing.Pool()
    pool = multiprocessing.Pool(processes=6)
    inputs = [0, 1, 2, 3, 4, 5]
    inputs =  [x + 1 for x in inputs]
    outputs = pool.map(random_func, inputs)
    
    print("Input: {}".format(inputs)) 
    print("Output: {}".format(outputs))
    end = time.time()
    print(f"Total time: {end-start}")