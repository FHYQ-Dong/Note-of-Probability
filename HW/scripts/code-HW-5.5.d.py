# The program for HW-5.5.d
import math
import random

S = 0
print("==========  Progress  ==========")
for i in range(1, 10001):
    x, y = random.random(), random.random()
    tmp = math.cos(math.pi * x) + math.sin(math.pi * y)
    if 0 <= tmp <= 1:
        S = ((i - 1) * S + 1) / i
    else:
        S = ((i - 1) * S) / i
    if i % 1000 == 0:
        print(f"i = {i:5d}, S = {S}")
print("==========  Result  ==========")
print(f"S = {S}")