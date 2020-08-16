"""
PEP8 - PYTHON ENHANCEMENT PROPOSAL
sÃO PROPOSTAS DE MELHORIAS PARA A LINGUAGEM PYTHON
Zem of python
import this
A ideia do PEP 8 é que possamos escrever códigos python de forma pythonica.

[1] - Utilize Camel Case para nomes de Classes;

class Caculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculos, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaçõs para identação! (Não use tab)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em Branco
- separar funções e definições de classes com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco

[5] - Imports
- Imports devem ser sempre feitas em linhas separadas;

# Errado

import sys, os

# Correto

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções

# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça

algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = lista [indice]

# Faça

dict['chave'] = lista[indice]

# Não faça:

x              = 1
y              = 3
variavel_longa = 5

# Faça:

x = 1
x = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha
"""
import this








