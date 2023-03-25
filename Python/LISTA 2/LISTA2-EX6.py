gph = float(input('Informe seu ganho por hora: R$'))
htm = float(input('Informe o número de horas trabalhadas no mês: '))
salariob = gph * htm * 30
ir = salariob * 11/100
inss = salariob * 8/100
sindicato = salariob * 5/100
descontos = ir + inss + sindicato 
salariol = salariob - descontos
print('Seu salário bruto é de: R$',salariob)
print('Valor do imposto de renda: R$',ir)
print('Valor de inss: R$',inss)
print('Valor do sindicato: R$',sindicato)
print('Seu sálario líquido é de R$',salariol)
