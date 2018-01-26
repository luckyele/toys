import sys

        

def read():

    if len(sys.argv) <=1 :
        print 'Input error'

    f = open(sys.argv[1], "r")
    
    rline = []

    for l in f.readlines():
        if l != '\n':
            rline.append(l[:-1])

    f.close()

    return rline

def char_to_digital(c):
    if c in ['A','B','C']:
        return '2'
    elif c in ['D','E','F']:
        return '3'
    elif c in ['G','H','I']:
        return '4'
    elif c in ['J','K','L']:
        return '5'
    elif c in ['M','N','O']:
        return '6'
    elif c in ['P','R','S']:
        return '7'
    elif c in ['T','U','V']:
        return '8'
    elif c in ['W','X','Y']:
        return '9'

def process(r):
    
    print r
    new_array = []
    new_str = ''
    for a in r:
        if '-' not in a and a.isdigit():
            new_array.append(a)
        else:
            for aletter in a:
                if aletter.isalpha():
                    new_str += char_to_digital(aletter)
                if aletter.isdigit():
                    new_str += aletter
                    
            new_array.append(new_str)
            new_str = ''

    return new_array        

def count_num(a):
    c = {}
    i = 0

    for n in a:
        if a.count(n) > 1:
            c[n] = a.count(n)
    return c

def output_result(c):    

    if len(c) == 0:
        print "No diplications."
        return 1

    for k, v in c.items():
        i = 0
        for a in k:
            i += 1
            sys.stdout.write(a) 
            if i == 3:
                print '-',
        i = 0
                      
        print '', v

if __name__ == '__main__':
    
    output_result(count_num(process(read())))
    
   

