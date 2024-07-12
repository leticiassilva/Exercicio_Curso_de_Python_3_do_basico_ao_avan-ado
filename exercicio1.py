nome = ""
sobrenome = ""
idade = 0
ano_nascimento = 0
altura_metros = 0.0

nome = input("Digite seu nome: ")
sobrenome = (input("Digite seu sobrenome: "))
idade = int(input("Digite sua idade: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
altura_metros = float(input("Digite sua altura: "))

maior_de_idade = idade >= 18

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)