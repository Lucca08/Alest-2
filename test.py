def apply_mutations(dna_chain):
    mutated_chain = list(dna_chain)
    mutated = True
    
    while mutated:
        mutated = False
        i = 0
        
        while i < len(mutated_chain) - 1:
            if mutated_chain[i] != mutated_chain[i + 1]:
                mutated_chain[i:i+2] = "A" if ("D" in (mutated_chain[i], mutated_chain[i + 1])) else "D"
                mutated = True
            i += 1
    
    return "".join(mutated_chain)

# Lista de caminhos para os arquivos de teste
test_files = ["caso3.txt"]

for file_path in test_files:
    with open(file_path, "r") as file:
        dna_chain = file.read().strip()  # Lê a cadeia de DNA do arquivo
        mutated_result = apply_mutations(dna_chain)
        print(f"File: {file_path}")
        print(f"Original: {dna_chain} | Mutated: {mutated_result} | Size: {len(mutated_result)}")
        print("------------------")

