import os

# See my article about this code: https://www.robertbryan.net/posts/2025-07-16-rna.html

def dna_rna_transcribe(sequence):
    return (
        sequence.replace("T", "U")
    )

def read_dna_sequence(file_path):
    try:
        with open(file_path, 'r') as dna_file:
            return dna_file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find DNA file: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading DNA file: {e}")

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_rna.txt"
    solution_path = "../solution-outputs/rosalind_rna.txt"
    if os.path.exists(solution_path):
        os.remove(solution_path)
    file = open(solution_path, "x")
    file.write(dna_rna_transcribe(read_dna_sequence(file_path)))
    file.close()
    print(f"Done.")