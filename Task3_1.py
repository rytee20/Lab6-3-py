from random import randint
from time import perf_counter


def generate_p():
    p=[]
    for i in range(5000):
        p.append(randint(0,100))
    return p

def generate_q():
    q=[]
    for i in range(5000):
        q.append(randint(0,100))
    return q

def formula(p_list,q_list):
    count=0
    for p in p_list:
        count=0
        for q in q_list:
            r = 1 / (1 + abs(q - p))
            print(round(r,2), end='')
            count+=1
            if(count==5000):
                print("\n", end='')
            else:
                print(" ", end='')

p_list=generate_p()
q_list=generate_q()

tic=perf_counter()
formula(p_list,q_list)
tac=perf_counter()

print(f"Вычисление заняло {tac - tic:0.4f} секунд")
#Вычисление заняло 592.7188 секунд
