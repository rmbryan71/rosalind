from numpy import roots

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_afrq.txt"
    probs = []
    proportion_recessives = [float(x) for x in open(file_path).read().strip().split()]
    # print(proportion_recessives)
    for item in proportion_recessives:
        q = item ** 0.5
        p = max(roots([1, 2*q, q**2-1]))
        probs.append((2*p*q) + (q ** 2))
    print(*probs)
