def rumor():
    k = 2 / 796
    R = 2
    for n in range(1, 14):
        R = R + k * R * (400 - R)
        print("After", n, "hours", R, "people know.")


rumor()


def coffee(k, dt):
    t = 0
    T = 190
    n = int(50 / dt)
    for i in range(n):
        t = t + dt
        T = T + k * (67 - T)
    print("After", t, "minutes the coffee temp is", T)


coffee(0.05, 0.1)
