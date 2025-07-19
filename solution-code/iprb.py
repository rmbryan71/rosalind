import itertools
import os
from itertools import combinations
import random

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_iprb.txt"
    solution_path = "../solution-outputs/rosalind_iprb.txt"
    file = open(file_path, "r").readline().split(' ')
    k = int(file[0])
    m = int(file[1])
    n = int(file[2])
    ### Solving code goes here
    def iprb(k, m, n):
        population = k * ["AA"] + m * ["Aa"] + n * ["aa"]
        # print(population)
        # pop_size = len(population)
        trial_size = 10000000
        possible_pairs = sorted(itertools.combinations(population, 2))
        count = 0
        for x in range(trial_size):
            parents = random.choice(possible_pairs)
            if parents in (('AA', 'AA'), ('AA', 'Aa'), ('AA', 'aa')):
                count += 1
            if parents == ('Aa', 'Aa'):
                count += .75
            if parents == ('Aa', 'aa'):
                count += .50
        return str(round((count/trial_size), 3))

    solution = iprb(k, m, n)
    ### End of solving code
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(solution)
    file.close()
    print(solution)