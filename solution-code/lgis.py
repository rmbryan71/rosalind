import os

def read_sequence(file_path):
    try:
        with open(file_path, 'r') as sequence_file:
            mylist = list(sequence_file.readlines()[1].split(' '))
        result = []
        for item in mylist:
            result.append(int(item))
        return result
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find sequence file: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading sequence file: {e}")

def lcis(mylist):
    n = len(mylist)-1
    M = [None] * (n+1)
    P = [None] * (n+1)
    L = 0
    for i in range(1, n+1):
        if L == 0 or mylist[M[1]] >= mylist[i]:
            j = 0
        else:
            lo = 1
            hi = L+1
            while lo < hi-1:
                mid = (lo + hi)//2
                if mylist[M[mid]] < mylist[i]:
                    lo = mid
                else:
                    hi = mid
            j = lo

        P[i] = M[j]
        if j == L or mylist[i] < mylist[M[j+1]]:
            M[j+1] = i
            L = max(L, j+1)
    # Backtrack to find the best sequence
    output = []
    pos = M[L]
    while L > 0:
        output.append(mylist[pos])
        pos = P[pos]
        L -= 1
    output.reverse()
    return output

def lcds(X):
    n = len(mylist) - 1
    M = [None] * (n + 1)
    P = [None] * (n + 1)
    L = 0
    for i in range(1, n + 1):
        if L == 0 or mylist[M[1]] <= mylist[i]:
            j = 0
        else:
            lo = 1
            hi = L + 1
            while lo < hi - 1:
                mid = (lo + hi) // 2
                if mylist[M[mid]] > mylist[i]:
                    lo = mid
                else:
                    hi = mid
            j = lo

        P[i] = M[j]
        if j == L or mylist[i] > mylist[M[j + 1]]:
            M[j + 1] = i
            L = max(L, j + 1)
    # Backtrack to find the best sequence
    output = []
    pos = M[L]
    while L > 0:
        output.append(mylist[pos])
        pos = P[pos]
        L -= 1
    output.reverse()
    return output

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_lgis.txt"
    solution_path = "../solution-outputs/rosalind_lgis.txt"
    mylist = list(read_sequence(file_path))
    # print(mylist)

    if os.path.exists(solution_path):
        os.remove(solution_path)
    file = open(solution_path, "x")
    print(str(lcis(mylist)).replace(',', ''))
    file.write(str(lcis(mylist)).replace(',', '').replace('[','').replace(']',''))
    file.write('\n')
    print(str(lcds(mylist)).replace(',', ''))
    file.write(str(lcds(mylist)).replace(',', '').replace('[','').replace(']',''))
    file.close()