from scipy.stats import binom
import os

def lia(k, n):
    return sum(binom.pmf(x,2**k,0.25) for x in range(n,2**k+1))

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_lia.txt"
    solution_path = "../solution-outputs/rosalind_lia.txt"
    file = open(file_path, "r").readline().split(' ')
    k = int(file[0])
    n = int(file[1])
    solution = str(lia(k, n))
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(solution)
    file.close()
    print(solution)