import random

# Uniform Mutation
def uniform_mutation(kromosom, mutation_rate=0.1):
# Pastikan kromosom adalah list
    kromosom = list(kromosom) # Konversi ke list jika perlu
    for i in range(len(kromosom)):
        if random.random() < mutation_rate:
            kromosom[i] = 1 - kromosom[i] # Membalik nilai gen
    return kromosom