from scipy.stats import binom
import os

def P(n, k):
    return binom.cdf(n - 1, 2 ** k, 0.25)

def lia(k, N):
    return 1 - sum([P(n, k) for n in range(N)])

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_lia.txt"
    solution_path = "../solution-outputs/rosalind_lia.txt"
    file = open(file_path, "r").readline().split(' ')
    n = int(file[0])
    k = int(file[1])
    solution = str(P(n, k))
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(solution)
    file.close()
    print(solution)