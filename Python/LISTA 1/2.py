from random import sample
vetor = sample(range(100),20)
par = [x for x in vetor if x % 2 == 0]
impar = [x for x in vetor if x % 2 == 1]

for x in vetor:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
print ('Vetor', vetor)
print ('Pares', par)
print ('Ímpares', impar)


