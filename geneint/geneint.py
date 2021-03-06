from random import randint, choice
import collections
import array

import cProfile

def read():
    return int(input())

def generate_int(k):
    aint = []
    
    while True:
        if len(aint) == k:
            break
        a = randint(1, k)
        if a not in aint:
            aint.append(a)
    return aint     

def generate_int2(k):
    aint = []
    bint = []

    bint = [i for i in range(1, k+1)]

    while True:
        if len(bint) == 0:
            break
        a = choice(bint)
        bint.remove(a)      
        aint.append(a)

    return aint

def generate_int3(k):
    aint = []
    bint = collections.deque() 

    for i in range(1, k+1):
        bint.append(str(i))

    while True:
        if len(bint) == 0:
            break
        a = choice(bint)
        bint.remove(a)      
        aint.append(a)

    return aint

def save(a):
    f = open('data.txt', 'w')
    buf = ''
    for item in a:
        buf += str(item)+'\n'
        
    f.write(buf)
    f.close()
    print("total write %d items to files."%len(a))

def main():
    save(generate_int2(read()))

if __name__ == "__main__":
    cProfile.run('main()')
