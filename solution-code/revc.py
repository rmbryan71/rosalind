import os
from Bio.Seq import Seq

def read_dna_sequence(file_path):
    try:
        with open(file_path, 'r') as dna_file:
            return dna_file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find DNA file: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading DNA file: {e}")


if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_revc.txt"
    solution_path = "../solution-outputs/rosalind_revc.txt"
    s = read_dna_sequence(file_path)
    seq = Seq(s)
    if os.path.exists(solution_path):
        os.remove(solution_path) #idempotent : https://en.wikipedia.org/wiki/Idempotence
    file = open(solution_path, "x")
    file.write(str(seq.reverse_complement()))
    file.close()
    print(seq.reverse_complement())
