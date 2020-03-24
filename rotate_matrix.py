
def print_matrix(A):
    for a in A:
        print(a)
    print('\n')

def clockwise_rotate_outmost_ring_one_step(i, j, r):
    ''' r: nth ride.
    '''
    global A
    if len(A) <= 1:
        return 
    
    x_, y_ = A[r][j-1-r], A[i-1-r][r]

    tmp1, tmp2 = x_, y_
    #print(tmp1, tmp2)

    # 第0行A[0][0]....A[0][j-2] -> 右移一位
    # 第i-1行 A[i-1][1]...A[i-1][j-2] -> 左移一位w
    k = j-r
    while (k > r):
         A[r][k-1] = A[r][k-2]
         k -= 1
    k = r
    while (k < i-1-r):  
        A[i-1-r][k] = A[i-1-r][k+1]
        k += 1
    
    A[r][j-1-r], tmp1 = tmp1, A[r][j-1-r]
    A[i-1-r][r], tmp2 = tmp2, A[i-1-r][r]

    # 第0列A[1][0]....A[i-1][0] -> 上移一位
    # 第j-1行 A[0][1-1]...A[i-1][j-1] ->  下移一位
    k = r
    while (k < i-1-r):
        A[k][r] = A[k+1][r]
        k += 1

    k = i-1-r
    while(k >= r):
        A[k][j-1-r] = A[k-1][j-1-r]
        k -= 1

    A[r][j-1-r], tmp1 = tmp1, A[r][j-1-r]
    A[i-1-r][r], tmp2 = tmp2, A[i-1-r][r]

if __name__ == "__main__":
    A = [[1,2,3,4,5],[4,5,6,7,8],[7,8,9,0,1],[1,2,3,4,5],[1,2,3,4,5]]
    #A = [[1,2],[3,4]]
    
    #A = [[1]]
    #A = []
    if len(A) > 1:
        m , n = len(A), len(A[0])
    print_matrix(A)
    i = 0
   
    # rotate len(A)-1 times. 
    
    for r in range(int(len(A)/2)):
        for i in range(len(A)-2*r-1):
            clockwise_rotate_outmost_ring_one_step(m, n, r)
    print_matrix(A)


    
  
       
   