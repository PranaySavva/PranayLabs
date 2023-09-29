import random
import utime


random.seed(utime.ticks_ms())

class Numbers:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
    def create_random_array(self):
        random_numbers = []
        for _ in range(3):
            random_num = random.randint(1, 2) 
            random_numbers.append(random_num)
        print(random_numbers)
        return random_numbers
        

