from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(8):
            print('Hello')
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(8):
            print("hi")
            sleep(1)

t1=Hello()
t2=Hi()

t1.start()
sleep(0.1)
t2.start()

t1.join()
t2.join()
print('Bye')
 