import random

def mersenne(n):
  # generates a list of n random numbers
  r = [0 for i in range(n)]
  s = 354

  k = 16807
  j = 2147483647
  for i in range(n):
    s = ( k * s ) % j
    r[i] = s / j
  print(r)

#mersenne(10)

def check_random():
  # checks to see if randoms generated in (0,10) are < 5 
  # about half of the time
  count = 0
  for i in range(1000):
    r = 10*random.random()
    if r < 5:
      count = count + 1
  print(count/1000)

#check_random()

def check_m_random(n):
  # checks to see if the mersenne generator also has 
  # randoms generated in (0,10) less than 5 about
  # half of the time
  count = 0
  s = 173
  k = 16807
  j = 2147483647
  for i in range(n):
    s = ( k * s ) % j
    r = 10 * s/j
    if r < 5:
      count = count + 1
  print(count/n)

#check_m_random(1000)

def two_dice(n):
  # counts the number of time the dice add to 2 and 7
  count2 = 0
  count7 = 0
  for i in range(n):
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    if r1+r2 == 2:
      count2 = count2 + 1
    elif r1+r2 == 7:
      count7 = count7 + 1
  print("experimental sum of 2:", count2/n, "theoretical:", 1/36)
  print("experimental sum of 7:", count7/n, "theoretical:", 6/36)

two_dice(10)

