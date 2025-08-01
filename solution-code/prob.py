import math

def single_prob(c, k):
    # Given a char (c) and a float(k), return likelihood of randomly generating c if k is the G/C content
    if c == 'A' or c == 'T':
        return (1 - k)/2
    else:
        return (k / 2)

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_prob.txt"
    s = open(file_path, "r").readline().strip()
    A = list(open(file_path, 'r').readlines()[1].split(' '))
    # print(s)
    # print(A)
    for i in A:
        prob = 1
        for char in s:
            prob *= single_prob(char, float(i))
        print(round(math.log10(prob), 3), end = ' ')
