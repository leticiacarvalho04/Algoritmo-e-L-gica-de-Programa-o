frase ='''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help
each other live up to these principles. We want our community to be more
diverse: whoever you are, and whatever your background, we welcome you'''

frase = frase.lower()
frase = frase.replace(',',' ')
frase = frase.replace('.',' ')
frase = frase.replace(':',' ')
frase= frase.split()
lista = []
for p in frase:
    for l in p:
        if l in 'python':
            if p not in lista:
                lista.append(p)
print(f'Lista com a frase: {lista}')
