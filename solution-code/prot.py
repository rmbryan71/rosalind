import os
from Bio.Seq import Seq

def read_rna_sequence(file_path):
    try:
        with open(file_path, 'r') as dna_file:
            return dna_file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find DNA file: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading DNA file: {e}")

### Solving code goes here
def prot(file_path):
    seq = Seq(read_rna_sequence(file_path))
    return str(seq.translate(stop_symbol=''))
### End of solving code

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_prot.txt"
    solution_path = "../solution-outputs/rosalind_prot.txt"
    if os.path.exists(solution_path):
        os.remove(solution_path)
    file = open(solution_path, "x")
    file.write(prot(file_path))
    file.close()
    print(f"Done.")