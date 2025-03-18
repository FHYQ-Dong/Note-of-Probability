# The program for HW-5.5.c
import math
import random

S = 0
print("==========  Progress  ==========")
for i in range(1, 10001):
    x, y = random.random(), random.random()
    if (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.25:
        S = ((i - 1) * S + 1) / i
    else:
        S = ((i - 1) * S) / i
    if i % 1000 == 0:
        print(f"i = {i:5d}, S = {S}")
print("==========  Result  ==========")
print(f"S = {S}, 4*S = {4*S}")
print(f"|pi - 4*S| = {abs(math.pi - 4*S)}")