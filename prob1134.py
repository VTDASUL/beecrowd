preference = int(input())
alcool = 0
gasolina = 0
diesel = 0


while preference != 4:
    if preference == 1:
        alcool += 1
    elif preference == 2:
        gasolina += 1
    elif preference == 3:
        diesel += 1
    preference = int(input())

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')