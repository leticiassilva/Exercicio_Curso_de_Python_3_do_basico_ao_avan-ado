nome = ""
altura = 0.0
peso = 0.0
imc = 0.0

nome = input("Digite seu nome: ")
print(nome)
altura = float(input("Digite sua altura: "))
print(altura)
peso = float(input("Digite seu peso: "))
print(peso)
imc = peso / altura ** 2

linha = f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu IMC é {imc:.2f}'
print(linha)

#print(nome, 'tem', altura, 'de', 'altura,', 'pesa',
#      peso, 'quilos', 'e seu IMC é', imc)