ta = int(input('Escreva a quantia de anos decorridos da cidade A: '))
tb = int(input('Escreva a quantia de anos decorridos da cidade B: '))
popA = 80.000 * 0.03 * ta
popB = 200.000 * 0.015 * tb
if popA > popB:
    print(f'São necessários {popA-popB:.0f} anos para a população A ser maior que a população B')
else:
    print(f'São necessários {popB-popA:.0f} anos para a população B ser maior que a população A')
if popA - popB == 0:
    print(f'Em {popA-popB:.0f} anos a população A se iguala à população B')
