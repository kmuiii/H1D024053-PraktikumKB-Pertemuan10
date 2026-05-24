import random

def one_point_crossover(parent1, parent2):
    if len(parent1) <= 1:   # Pastikan panjang kromosom lebih dari 1 untuk melakukan crossover
        return parent1.copy(), parent2.copy()
    
    titik_potong = random.randint(1, len(parent1)-1)
    anak1 = parent1[:titik_potong] + parent2[titik_potong:]
    anak2 = parent2[:titik_potong] + parent1[titik_potong:]
    return anak1, anak2
