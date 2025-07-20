import itertools
import os
import random

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_iev.txt"
    solution_path = "../solution-outputs/rosalind_iev.txt"
    file = open(file_path, "r").readline().split(' ')
    a = int(file[0])
    b = int(file[1])
    c = int(file[2])
    d = int(file[3])
    e = int(file[4])
    f = int(file[5])
    ### Solving code goes here
    def iev(a, b, c, d, e, f):
        print(a, b, c, d, e, f)
        couples = a * [("AA", "AA")] + b * [("AA", "Aa")] + c * [("AA", "aa")] + d * [("Aa", "Aa")] + e * [("Aa", "aa")] + f * [("aa", "aa")]
        count = 0
        for couple in couples:
            if couple in [("AA", "AA"), ("AA", "Aa"), ("AA", "aa")]:
                count += 2 # both children will have the dominant phenotype
            if couple in [("Aa, Aa")]:
                count += 1.5 # On average, 1.5 children will have the dominant phenotype
            if couple in [("Aa, aa")]:
                count += 1 # On average, 1 child will have the dominant phenotype
        return str(count)

    solution = iev(a, b, c, d, e, f)

    ### End of solving code
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(solution)
    file.close()
    print(solution)