import math
def quad_root(a,b,c):
 # finds the roots of the quadratic ax^2+bx+c, 
 # assuming a != 0

  if a == 0:
    print("This is not a quadratic.")
  else:
    disc = b**2 - 4*a*c
    if disc < 0:
      print("This has no real roots.")
    elif disc == 0:
      print("The quadratic has a double root at:", - b/(2*a))
    else:  
      if b > 0:
        t = -b - math.sqrt(disc)
        print("The quadratic has two distinct roots at:", (2*c)/t, t/(2*a))
      else:  
        t = -b + math.sqrt(disc)
        print("The quadratic had two distinct roots at:", (2*c)/t, t/(2*a))

#quad_root(-1,-99,-1)

def bisect_for(a,b,nmax,eps):
  # finds the root of the external function f(x) 
    #in the interval [a,b]

  fa = f(a)
  fb = f(b)

  if fa*fb > 0:
    print("There is an error")
    return
  error = b-a
  for i in range(1, nmax):
    error = error/2
    m = a + error
    fm = f(m)
    if abs(error) < eps:
      print("The solution for m is", m, "and the number of steps is" ,nmax)
      return
    if fa*fm > 0: 
      a = m 
      fa = fm
    else:
      b = m 
      fb =fm
  print("The root estimate for m is", m, "and the function took too many steps", nmax)



def bisect_while(a,b,nmax,eps):
  #finds the root of the external function f(x) 
    #in the interval [a,b] if there is a sign change

  fa = f(a)
  fb = f(b)

  if fa*fb > 0:
    print("an error message")
  else:
    error = b-a
    count = 0
    while count < nmax and abs(error) >= eps:
      count = count + 1
      error = error/2
      m = a + error
      fm = f(m) 
      if fa*fm > 0: 
        a = m 
        fa = fm
      else:
        b = m 
        fb =fm
    if count == nmax:
      print("root estimate", m,"and it took too many steps", nmax)
    if abs(error) < eps:
        print("the solution", m, "and the number of steps is" , nmax)

def f(x):
  #return x**3*math.cos(x)
 #return math.exp(-.01*x)*math.sin(0.2*x)
  #return x**10-8*x**3+2*x-.25
  #return x**5-8*x**4+24*x**3-32*x**2+16*x
  return x**6-10*x**5+40*x**4-80*x**3+80*x**2-32*x

bisect_for(1, 4, 100, 10**-10)
bisect_while(1, 4, 100, 10**-10)
