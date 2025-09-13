def add_cyclic(s, t):
    if len(s) < len(t):
        return False
    s1 = s + s
    if t in s1:
        return s
    return s + t


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_pcov_sample.txt"
    reads = []
    with open(file_path) as file:
        for line in file:
            reads.append(line.strip())
    response = reads[0]
    for i in range(1, len(reads)):
        response = add_cyclic(response, reads[i])
    print(response)
