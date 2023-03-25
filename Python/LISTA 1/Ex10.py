cigarros = int(input("Informe a quantidade de cigarros fumados por dia: "))
anos = int(input("Informe há quantos anos utiliza o cigarro: "))
perda = cigarros*anos*365/144
print(f'Você perdeu {perda: .0f} dias')
