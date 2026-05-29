from datetime import timedelta

while True:
    horario = list(map(int, input().split()))
    if all(v == 0 for v in horario):
        break
    h1, m1, h2, m2 = horario
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    diff = t2 - t1
    if diff <= 0:
        diff += 1440
    print(diff)