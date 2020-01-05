
def print_matrix(A):
    for a in A:
        print(a)
    print('\n')


def left_move_one_step(A):

    i ,j = len(A), len(A[0])
    tmp1,tmp2 = A[0][j-1], A[i-1][0]

    # 第0行A[0][0]....A[0][j-2] -> 右移一位
    # 第i-1行 A[i-1][1]...A[i-1][j-2] -> 左移一位w
    k = j
    while (k > 0):  
         A[0][k-1] = A[0][k-2]
         k -= 1
    k = 0
    while (k < i-1):  
        A[i-1][k] = A[i-1][k+1]
        k += 1

    A[0][j-1], tmp1 = tmp1, A[0][j-1]
    A[i-1][0], tmp2 = tmp2, A[i-1][0] 

    # 第0列A[1][0]....A[i-1][0] -> 上移一位
    # 第j-1行 A[0][1-1]...A[i-1][j-1] ->  下移一位
    k = 0
    while (k < i-1):
        A[k][0] = A[k+1][0]
        k += 1

    k = i-1
    while(k >= 0):
        A[k][j-1] = A[k-1][j-1]
        k -= 1

    A[0][j-1], tmp1 = tmp1, A[0][j-1]
    A[i-1][0], tmp2 = tmp2, A[i-1][0] 



if __name__ == "__main__":

    A = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6]]
    #A = [[1,2],[3,4]]
    
    print_matrix(A)
    for i in range(len(A)-1):
        left_move_one_step(A)
        print_matrix(A)



