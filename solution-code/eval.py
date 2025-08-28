from decimal import localcontext, Decimal, ROUND_HALF_UP

def single_prob(c, k):
    if c == 'A' or c == 'T':
        return (1 - k)/2
    else:
        return (k / 2)

def prob(n, s, gc):
    # returns probability that substring s appears in a superstring n characters long with a gc-content of gc
    result = 1
    for char in s:
        result *= single_prob(char, gc)
    x = str(result * (n-len(s)+1))
    with localcontext() as ctx:
        ctx.rounding = ROUND_HALF_UP
        y = Decimal(x)
        return y.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_eval.txt"
    file = open(file_path, "r").readlines()
    n = file[0].strip()
    s = str(file[1]).strip()
    A = []
    for item in file[2].split():
        A.append(item)
    # print(n, s, A)
    for i in range(len(A)):
        print(prob(int(n), s, float(A[i])), end=' ')
