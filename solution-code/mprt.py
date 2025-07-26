import os
from Bio import ExPASy
from Bio import SwissProt
from re import finditer

def get_uniprot_record(protein_id):
    handle = ExPASy.get_sprot_raw(protein_id.split('_')[0])
    try:
        solution = SwissProt.read(handle)
    except:
        print("Could not find " + protein_id.split('_')[0])
    return solution

def read_sequence_id_file(file_path):
    file = open(file_path, "r")
    return file.read().splitlines()

if __name__ == "__main__":
    file_path = "/Users/robertbryan/Downloads/rosalind_mprt.txt"
    solution_path = "../solution-outputs/rosalind_mprt.txt"
    ### Solving code goes here
    if os.path.exists(solution_path):
        os.remove(solution_path)
    file = open(solution_path, "x")
    motif = '(N[^P][ST][^P])'
    for id in read_sequence_id_file(file_path):
        seq = get_uniprot_record(id).sequence
        sites = [g.start()+1 for g in finditer(r'(?=N[^P][ST][^P])', seq)]
        if sites:
            file.write(str(id))
            file.write('\n')
            file.write(str(sites).replace('[','').replace(']','').replace(',',''))
            file.write('\n')
    file.close()
