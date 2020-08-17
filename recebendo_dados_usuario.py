"""
Recebendo dados do usuário
input() -> Todo dado recebido via input é do tipo String

Em Python, string é Tudo que estiver entre:
- Aspas Simples;
- Aspas duplas,
- Aspas simples triplas;
- Aspas duplas triplas;

"""
# Entrada de dados
# print("Qual seu nome? ")
# nome = input()  # input - Entrada

nome = input('Qual o seu nome? ')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print("Qual sua idade? ")
# idade = input()

idade = int(input('Qual sua idade? '))

# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos' % (nome, idade))
# print('A {0} tem {1} anos'.format(nome, idade))
print(f'A {nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""

print(f'A {nome} nasceu em {2020 - idade}')



