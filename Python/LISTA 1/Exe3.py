segundos = int(input("Digite a quantia de segundos do usuário: "))
minutos = int(input("Digite a quantia de minutos do usuário: "))
horas = int(input("Digite a quantia de horas do usuário: "))
dias = int(input("Digite a quantia de dias do usuário: "))
print("O tempo total informado foi: ", dias,"dia(s), ", horas,"h",minutos,"min e ",segundos,"s")
calculo = segundos+(60*minutos)+(60*60*horas)+(dias*24*60*60)
print("O total de segundos do usuário durante este período é: ",calculo)

