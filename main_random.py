import random
import math

def test_mers(n):
# tests the python random number
# generator to see if the numbers
# appear to be uniformly distributed
# the counts for each subinterval are 
# stored in a list called "dist"

  dist = [ 0 for i in range(10)]
  s = 1234
  k = 16807
  j = 2147483647
  for i in range(n):
    s = ( k * s ) % j
    r = s / j
    if r < .1: dist[0] = dist[0] + 1
    elif r < .2: dist[1] = dist[1] + 1
    elif r < .3: dist[2] = dist[2] + 1
    elif r < .4: dist[3] = dist[3] + 1
    elif r < .5: dist[4] = dist[4] + 1
    elif r < .6: dist[5] = dist[5] + 1
    elif r < .7: dist[6] = dist[6] + 1
    elif r < .8: dist[7] = dist[7] + 1
    elif r < .9: dist[8] = dist[8] + 1
    else: dist[9] = dist[9] + 1
  print(dist)

test_mers(10000)

def test_python(n):
# tests the python random number
# generator to see if the numbers
# appear to be uniformly distributed;
# the counts for each subinterval are 
# stored in a list called "dist"

  dist = [ 0 for i in range(10)]
  for i in range(n):
    r = random.random()
    if r < .1: dist[0] = dist[0] + 1
    elif r < .2: dist[1] = dist[1] + 1
    elif r < .3: dist[2] = dist[2] + 1
    elif r < .4: dist[3] = dist[3] + 1
    elif r < .5: dist[4] = dist[4] + 1
    elif r < .6: dist[5] = dist[5] + 1
    elif r < .7: dist[6] = dist[6] + 1
    elif r < .8: dist[7] = dist[7] + 1
    elif r < .9: dist[8] = dist[8] + 1
    else: dist[9] = dist[9] + 1
  print(dist)

test_python(10000)

def monte(n):
# integrates exp(x) from 0 to 1
# using Monte Carlo
# methods with n points.
  total = 0
  for i in range(n):
    r = random.random()
    total = total + math.exp(r)
  total = total * (1/n)

  print(total)

monte(1000)

def drunk(n):
# prints out the results of simulating
# the drunk walk problem from the text
  count = 0
  for i in range(n):
    x = 0
    y = 0
    for steps in range(50):
      r = random.random()
      if r < .25: x = x + 1
      elif r < .5: y = y + 1
      elif r < .67: y = y - 1
      else: x = x - 1
    if x**2 + y**2 >= 400:
      count = count + 1;
  print(count/n)

drunk(10000)

def double6(n):
# prints out the results of simulating
# the rolling double sixes from the text
 
  count = 0
  for i in range(n):
    found = 0
    rolls = 0
    while found == 0 and rolls < 24: 
      r1 = random.randint(1,6)
      r2 = random.randint(1,6)
      #print(r1+r2)
      if r1 + r2 == 12:
        found = 1
        count = count + 1
      rolls = rolls + 1
      #print(rolls)
  print(count/n)

double6(10000)
