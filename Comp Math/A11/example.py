def for_list():
  for i in [0, 1, 2, 3]:
    print(i)
  for i in range(4):
    print(i)

#for_list()

def seq(n):
  x = [0 for i in range(n+1)]
  x[0] = 11.0/2.0
  x[1] = 61.0/11.0
  for i in range(2,n+1):
    x[i] = 111 - ( 1130 - 3000/x[i-2])/x[i-1]
  print(x)

#seq(100)

def matrix_add(A, B, n, m):
  ApB = [ [ 0 for j in range(m) ] for i in range(n)]
  print(ApB)
  for i in range(n):
    for j in range(m):
      ApB[i][j] = A[i][j] + B[i][j]
  print(ApB)

A = [ [ 1,2, 6], [3,4, -3]]
B = [ [ 7,-2, -2], [3,6, -2]]
#matrix_add(A, B, 2, 3)

def matrix_add_1(A, B):
    n = len(A)
    m = len(A[0])
    ApB = [ [ 0 for j in range(m) ] for i in range(n)]
    for i in range(n):
        for j in range(m):
            ApB[i][j] = A[i][j] + B[i][j]
    print(ApB)

#matrix_add_1(A, B)

def seq_1(n):
    x = [11/2, 61/11]
    for i in range(2,n+1):
        x.append(111 - ( 1130 - 3000/x[i-2])/x[i-1] )
    print(x)

seq_1(100)
