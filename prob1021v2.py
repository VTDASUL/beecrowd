list_notas = [100, 50, 20, 10, 5, 2]
list_moedas = [100, 50, 25, 10, 5, 1]

valor = input().split('.')
reais = int(valor[0])
centavos = int(valor[1])

print('NOTAS:')
count = 0
while count < 6:
    div_inteira = reais // list_notas[count]
    reais = reais % list_notas[count]
    print(f'{div_inteira} nota(s) de R$ {list_notas[count]:.2f}')
    count += 1

centavos = (reais * 100) + centavos 
    
print('MOEDAS:')
count2 = 0
while count2 < 6:
    div_inteira2 = centavos // list_moedas[count2]
    centavos = centavos % list_moedas[count2]
    print(f'{div_inteira2} moeda(s) de R$ {list_moedas[count2]/100:.2f}')
    count2 += 1
    