from multiprocessing import Queue, Process
from random import randint
from time import perf_counter


def generate_p():
    p = []
    for i in range(5000):
        p.append(randint(0, 100))
    return p


def generate_q():
    q = []
    for i in range(5000):
        q.append(randint(0, 100))
    return q


def adder(queue, p, q):
    for i in range(len(p)):
        for j in range(len(q)):
            r = 1 / (1 + abs(q[j] - p[i]))
            round(r, 2)
            queue.put(r)


def printer(queue):
    for i in range(10000000):
        r_one = queue.get()
        print(round(r_one, 3), end='')
        if i % 5000 == 0:
            print("\n", end='')
        else:
            print(" ", end='')


p_list = generate_p()
q_list = generate_q()

if __name__ == '__main__':

    queue = Queue()
    a = Process(target=adder, args=(queue, p_list, q_list,))
    a.start()
    b = Process(target=printer, args=(queue,))
    b.start()
    a.join()
    b.join()
