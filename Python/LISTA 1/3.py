import random
vetor1 = random.sample(range(100),10)
vetor2 = random.sample(range(100),10)
vetor3 = []
for x in range(10):
    vetor3.append(vetor1[x])
    vetor3.append(vetor2[x])
print(f'Vetor 1: {vetor1}')
print(f'Vetor 2: {vetor2}')
print(f'Vetor 3: {vetor3}')
