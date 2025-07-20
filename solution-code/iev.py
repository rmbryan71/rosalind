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
        return str(a*2 + b*2 + c*2 + d*1.5 + e)

    solution = iev(a, b, c, d, e, f)

    ### End of solving code
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(solution)
    file.close()
    print(solution)