import random



def gen_map():
    a_map = [[0 for i in range(10)] for i in range(10)]
    
    for i in range(len(a_map)):
        if i == 0 or (i == len(a_map) - 1):
            pass
        for j in range(len(a_map)):
            if j == 0 or (j == len(a_map) - 1):
                pass
            a_map[i][j] = random.randint(0, 1)
    
    return a_map

def prt_map(m):
    for line in m:
        print(line)

if __name__ == '__main__':
    r = gen_map()
    prt_map(r)
