while True:
    nome = input('Digite o nome de usuário: ')
    senha = input('Digite a sua senha: ')
    if nome == senha:
        print('A senha não pode ser igual ao nome do usuário. Faça novamente: ')
        continue
    else:
        print('Senha e usuário aceitos')
        break
