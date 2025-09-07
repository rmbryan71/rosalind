import numpy as np
from math import factorial

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_indc.txt"
    n = int(open(file_path, "r").readline()[0])
    p = .5
    Pr = 0
    A = []
    for k in range(2*n, 0, -1):
        Pr += factorial(2*n)/(factorial(k)*factorial(2*n-k)) * np.power(p,k)*np.power(1-p, 2*n-k)
        A.append(round(np.log10(Pr), 4))
    for i in A[::-1]:
        print(i, end=" ")