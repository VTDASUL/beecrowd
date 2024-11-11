peca1 = input().split()
peca2 = input().split()

id_p1= int(peca1[0])
quantidade_p1 = int(peca1[1])
valor_p1 = float(peca1[2])
preco_p1 = quantidade_p1 * valor_p1

id_p2= int(peca2[0])
quantidade_p2 = int(peca2[1])
valor_p2 = float(peca2[2])
preco_p2 = quantidade_p2 * valor_p2

total_preco = preco_p1 + preco_p2
print(f'VALOR A PAGAR: R$ {total_preco:.2f}')
