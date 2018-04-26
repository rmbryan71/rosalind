import math
import random

while True:
    n = random.randrange(1, 100000)
    k = random.randrange(n)
    if k < n:
        print(n, k)
