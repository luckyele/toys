
import time
import random

class Arry_map():
    def Arry_map_init(self, m, n):
        self.row = m
        self.col = n
        self.map = [[0 for i in range(n)] for i in range(m)]

    def set_all_to_zero(self):
        self.map = [[0 for i in range(self.col)] for i in range(self.row)]

    def disp_arry_map(self):
        for r in self.map:
            for i in r:
                if i == 1:
                    print("\033[1;34;40m%d\033[40m"%(i),end='')
                else:
                    print("\033[0m%d"%(i),end='')
            print('\n', end='')	
       # print('\n')

    def set_outside(self):
        for i in range(self.row):
            if i == 0 or i == self.row - 1:
                for j in range(self.col):
                    self.map[i][j] = 1
            else:
                self.map[i][0] = 1
                self.map[i][self.col-1] = 1
	
    def set_line(self, x1,y1,x2,y2):
        if x1 == x2 and x1 < self.row:
            for i in range(y1,y2+1):
                self.map[x1][i] = 1
        if y1 == y2 and y1 < self.col:
            for i in range(x1, x2+1):
                self.map[i][y1] = 1

    def set_rect(self, r1, c1, r2, c2):
        self.set_line(r1,c1,r1,c2)
        self.set_line(r2,c1,r2,c2)
        self.set_line(r1,c2,r2,c2)
        self.set_line(r1,c1,r2,c1)
				
    def zoom_in_outside(self, r1, c1, r2, c2):
				    pass
				     
    def rand_rect(self):
        while True:
            a = random.randint(0, self.row-1)
            b = random.randint(0, self.col-1)
            c = random.randint(0, self.row-1)
            d = random.randint(0, self.col-1)
            #if c>a and d>b:
            #    return a,b,c,d
            if a==c or b==d:
                return a,b,c,d
	
def test():
    arry_map = Arry_map()
    arry_map.Arry_map_init(40, 40)
    arry_map.disp_arry_map()
			
    while True:
        a,b,c,d = arry_map.rand_rect()
        arry_map.set_line(a,b,c,d)
        arry_map.disp_arry_map()
        #arry_map.set_all_to_zero()
        time.sleep(.5)
	

if __name__ == "__main__":
    test()