def coffee(k,dt):
  t = 0
  T = 190
  n = int(50/dt)
  for i in range(n):
    t = t+dt
    T = T+k*(67-T)
  print("After", t, "minutes the coffee temp is", T)

