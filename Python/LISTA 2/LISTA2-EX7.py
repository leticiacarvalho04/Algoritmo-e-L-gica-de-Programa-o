metros = int(input("Qual o tamanho da área em metros quadrados? "))
if metros%54==0:
    litros=metros/54
else:
    litros = int(metros/54)+1
valor=litros*80
print(f'Quantidade de litros: {litros} l')
print(f'Preço total: R$ {valor:.2f}')
