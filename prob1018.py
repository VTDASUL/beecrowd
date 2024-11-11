valor = int(input())
list_notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)
for nota in list_notas:
    div_inteira = valor // nota
    valor = valor % nota
    print(f'{div_inteira} nota(s) de R$ {nota},00')





















# valor = int(input())
# valorprint = valor

# notas_100 = valor // 100
# valor = valor % 100

# notas_50 = valor // 50
# valor = valor % 50

# notas_20 = valor // 20
# valor = valor % 20

# notas_10 = valor // 10
# valor = valor % 10

# notas_5 = valor // 5
# valor = valor % 5

# notas_2 = valor // 2
# valor = valor % 2

# notas_1 = valor // 1

# print(valorprint)
# print(f'{notas_100} nota(s) de R$ 100,00')
# print(f'{notas_50} nota(s) de R$ 50,00')
# print(f'{notas_20} nota(s) de R$ 20,00')
# print(f'{notas_10} nota(s) de R$ 10,00')
# print(f'{notas_5} nota(s) de R$ 5,00')
# print(f'{notas_2} nota(s) de R$ 2,00')
# print(f'{notas_1} nota(s) de R$ 1,00')