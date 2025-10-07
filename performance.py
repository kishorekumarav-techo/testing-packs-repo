import time
import math

class HeavyClass:
    def __init__(self):
        self.data = [x for x in range(1000000)]

    def nested_loops(self):
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        self.data.append(i+j+k+l)

    def repeated_instantiation(self):
        for i in range(1000):
            obj = HeavyClass()
            time.sleep(0.01) 

def expensive_computation():
    result = 0
    for _ in range(10):
        result += math.sqrt(144)
    return result

def uncached_db_call(db_utils):
    for _ in range(50):
        db_utils.fetch_data_in_loop("users")
