
def work():
  E = 40
  P = 27
  T = 14
  for i in range(1,101):
    Enew = .33*E + .14*P + .1*T
    Pnew = .25*E + .25*P + .56*T
    Tnew = .42*E + .61*P + .34*T
    E = Enew
    P = Pnew
    T = Tnew
  print(i, E, P, T)

work()

def rabbits(n):
# n: the number of time steps to take from t=0 to t=5
    dt= 5/n
    t = 0
    P = 15
    k = 0.49
    for i in range(1,n+1):
         P = P + k * P * dt
         t = t + dt
    print("The population in 5 years is:", P)
    print("When the number of time steps is:", n)
    print("and thus dt is:", dt)

rabbits(10000)

def operate(n):
  print(n, " plus 1 is equal to", n+1)
  print(n, " times 10 is equal to", n * 10)
  print(n, "divided by 100 is equal to", n / 100)
  print(n, " raised to a power of 5 is equal to", n**5)
  print(n, "^3 is equal to", n^3)

def some_calcs(n): 
  n=add_one(n) 
  print("n is now", n)
  print("after *10:", mult_by_ten(n))
    
def add_one(x):
  return(x+1)
  
def mult_by_ten(x):
  return(10*x)
    
def loop_test():
  for i in range(10,1,-1):
    print(i)
