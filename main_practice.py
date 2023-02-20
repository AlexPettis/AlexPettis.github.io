import math

def start_calc(A):
  n = len(A)

  mean = 0
  for i in range(n):
    mean = mean + A[i]
  mean = mean / n
  
  v = 0
  for i in range(n):
    v = v + (A[i] - mean) ** 2
  v = v / (n-1)
  print("The mean is", mean)
  print("The variance is", v)
  sd = math.sqrt(v)
  print("The standard deviation is", sd)





def atan_calc(x,n):
    a = 2**(-n/2)
    b = x / (1+math.sqrt(1+x**2))
    c = 1
    d = 1

    while 1 - a > 2 **-n:
      c = (2 * c)/(1+a)
      d = (2 * a * b)/(1 + b**2)
      d = (d)/(1 + math.sqrt(1 - d**2))
      d = (b + d)/(1 - b * d)
      b = (d)/(1 + math.sqrt(1 + d**2))
      a = (2*math.sqrt(a))/(1 + a)

  
    f = c * math.log((1+b)/(1-b))
    print(f)

def int_calc(a,b):

  if b == -1:
    x = math.log(abs(a))
  else:
    x =((a**(b+1)-1)/(b+1))
  print(x)

def m_v_mult(A,v):
# Performs matrix-vector multiplication
# with an mxn matrix A (stored as rows)
# and an n element vector v

  m = len(A)
  n = len(A[0])

  Av = [0 for i in range(m)]

  if len(v) != n:
    print("dimensions do not match")
  else:

      for i in range(m):
        for j in range(n):
          Av[i] = Av[i] + A[i][j] * v[j]
      print(Av)
  
A = [ [ 1, 2, 3, 4], [5, 6, 7, 8], [0, 1, 0, 1]]
v = [ 3, 1, 22, 9]

m_v_mult(A,v)

#start_calc([1,2,3])

#int_calc(2,-1)

#atan_calc(0.5,53)
#print(math.atan(0.5))
start_calc([2,5,3,7,4])
atan_calc(0.5, 53)
int_calc(3.1, 0)
m_v_mult([[1,2,3,4],[5,6,7,8],[0,1,0,1]], [3,0,1,0])
m_v_mult([[1,2,3,4],[5,6,7,8],[0,1,0,1]], [3,0,1])
int_calc(-2,-1)
