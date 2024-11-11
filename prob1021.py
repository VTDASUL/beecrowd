valores = input().split('.')
notas = int(valores[0])
moedas = int(valores[1])
list_notas = [ 100, 50, 20, 10, 5, 2]
list_moedas = [100, 50, 25, 10, 5, 1]
print('NOTAS:')
for nota in list_notas:
    div_notas = notas // nota 
    notas = notas % nota
    print(f'{div_notas} nota(s) de R$ {nota:.2f}')
    
moedas += notas * 100
print('MOEDAS:')
for moeda in list_moedas:
    div_moedas = moedas // moeda
    moedas = moedas % moeda
    print(f'{div_moedas} moeda(s) de R$ {moeda/100:.2f}')


