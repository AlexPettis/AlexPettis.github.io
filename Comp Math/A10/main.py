import math

def golden(a, b, eps, nmax):
    # finds a local minimum of
    # the externally defined f(x)
    # in the interval [a,b] to within
    # an accuracy of eps 
    r = (-1.0 + math.sqrt(5.0))/2.0
    rs = r**2
    x = a + r*(b-a)
    y = a + rs*(b-a)
    u = f(x)
    v = f(y)
    for i in range(1,nmax+1):
      if abs(b-a) < eps:
        print("Here is the point where the minimum occurs", (x, u))
        return
      if u > v:
        b = x
        x = y
        u = v
        y = a + rs*(b-a)
        v = f(y)
      else:
        a = y
        y = x
        v = u
        x = a + r*(b-a)
        u = f(x)
        


def f(x):
    # the first equation is to be solved on [-3,2]:
    #return x * ( x * (2.0 * x + 3.0) - 12.0) + 4.0
    # the second equation is to be solved on [0, pi]
    # return math.exp(-x) * math.cos(x)
    # the third equation is to be solved on [-2,6]
    # return x * ( x * x * ( x - 6.0 ) + 30.0 ) - 4.0
    return .75*(1000)*math.sqrt((3.9**2) + (x**2))+2.25*(1000)*math.sqrt((1.3**2)+((2.3-x)**2))
  
golden(0, 5.2, 10**-10, 100)
