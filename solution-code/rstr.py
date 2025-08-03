import math

def single_prob(c, k):
    # Given a char (c) and a float(k), return likelihood of randomly generating c if k is the G/C content
    if c == 'A' or c == 'T':
        return (1 - k)/2
    else:
        return (k / 2)

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_rstr.txt"
    N = int(open(file_path, "r").readline().split(' ')[0])
    x = float(open(file_path, "r").readline().split(' ')[1])
    A = str(open(file_path, 'r').readlines()[1]).strip()
    # print(N)
    # print(x)
    # print(A)
    prob = 1
    for char in A:
        # print(char)
        prob *= single_prob(char, x)
    answer = (1-((1 - prob)**N))
    print(round(answer, 3))
