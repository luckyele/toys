def is_swap(A, b, e):
    for a in range(b ,e):
        if A[e] == A[a]:
            return False
    return True

def perm(A, m, n):
    s = []
    if m == n:
        for i in range(n):
            s.append(A[i])
        r.append(s)
    else:
        i = m
        for i in range(m,n):
            if is_swap(A, m, i):
                A[m], A[i] = A[i], A[m]
                perm(A, m+1, n)
                A[m], A[i] = A[i], A[m]

r =[]
A = [0,2,6,6]
perm(A,0,4)
while():
    a, b  = r[i][2], r[i][3]
    if a*10+b >= 60:
        r.remove(r[i])
print(r)
