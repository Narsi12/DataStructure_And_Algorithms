import time
from threading import *

def cal_square(numbers):
    print('The sauqre numbers : ')
    for num in numbers:
        time.sleep(0.2)
        print(num**2)

def cal_cub(numbers):
    print('The cube numbers : ')
    for num in numbers:
        time.sleep(0.2)
        print(num**3)

intial_time = time.time()

numbers = [1,3,4,5,6]

t1 = Thread(target=cal_square,args=(numbers,))
t2 = Thread(target=cal_cub,args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()

# cal_square(numbers)
# cal_cub(numbers)

print('total time is : ',(time.time() - intial_time))

