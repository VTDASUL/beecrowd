id = input()
salario = float(input())
vendas = float(input())

bonificacao = (vendas * 15)/100 

print(f'TOTAL = R$ {salario + bonificacao:.2f}')
