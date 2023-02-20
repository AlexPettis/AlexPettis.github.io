import math

def step_test(a,b,n): 
# This program compares two methods for updating
# the time step, t.

  h = (b-a)/n
  t1 = a
  for i in range(1,n+1):
    t1 = t1 + h 
    t2 = a + i*h
  print(t1, t2)

step_test(0,1,2**20)

def Euler(a,b,x,n):
# finds the approximate solution to x’(t) = f(t,x)
# (a,x) is the initial value point, 
# b is the target value for t 
# n is the number of subintervals between a and b
# requires a separately defined function f(t,x)


  h = (b-a)/n
  t = a
  print("Step, Time, X-value")
  print(0, t, x)
  for k in range (1, n+1):
    x = x + h * f(t,x)
    t = a + k * h
  print(k, t, x)
 


def f(t,x):
  # return t**2 - math.sin(t)
  # return t + x
  return x * math.sin(t)

# return the (t,x) value of the
# right hand side of differential equation being solved
#suggestion! Use this same function definition for all three functions -- simply comment out the ones you are NOT running.

# Euler(0,.9,0,1000)
