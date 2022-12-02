from multiprocessing import pool
from threading import Semaphore, Thread, BoundedSemaphore, current_thread
from time import sleep

s = Semaphore(2)

max = 3
pool = BoundedSemaphore(value=max)


def semaphore_func():
    with pool:
        print(current_thread().name)
        sleep(3)


for i in range(7):
    Thread(target=semaphore_func, name=f"{i}").start()
