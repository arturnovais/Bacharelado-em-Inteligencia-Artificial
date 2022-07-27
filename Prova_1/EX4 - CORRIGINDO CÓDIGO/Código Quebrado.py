import matplotlib.pyplot as plt
import numpy as np
# Código funcional

import random


def ordenacao_selecao(A):
    # Verificar o tamanho dinamicamente do vetor A.
    cont = 0
    for item in A:
        cont += 1
        n = cont

    # Percorre o arranjo A.
    for i in range(n):
        # Encontra o elemento mínimo em A.
        minimo = i

        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j

        # Coloca o elemento mínimo na posição correta.
        A[i], A[minimo] = A[minimo], A[i]



A = random.sample(range(-10, 10), 10)
aux = A[:]
print("Arranjo não ordenado: ", A)

# Plotagem desordenada

array = np.array([n for n in range(1, len(A) + 1)])

plt.title('NÃO ORDENADO')
plt.rcParams.update({'font.size': 15})

plt.bar(array, A, color='red')
plt.show()

# Ordenando o arranjo
ordenacao_selecao(A)

# Plotagem ordenada
plt.title('ORDENADO')
array = np.array([n for n in range(1, len(A) + 1)])

plt.rcParams.update({'font.size': 14})

plt.bar(array, A, color="green")
plt.show()

print("Arranjo ordenado:", A)

# Plotagem de ordenados e desordenados juntos
data1 = A
data2 = aux

linha = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

fig, ax = plt.subplots(2, 1, figsize=(10, 8))

ax[0].bar(linha, data1, color="green")
ax[0].legend(["Ordenado"])
ax[1].bar(linha, data2, color="red")
ax[1].legend(["Desordenado"])

plt.show()


# Correção código
'''
O indivíduo utilizou null, o parâmetro é inexistente no python, este parâmetro é da linguagem C, e indica que o ponteiro 
não está apontando para nenhum valor na memória, ou seja a variável está "vazia", então irei trocar pelo parâmetro correspondente
no Python, o 'None'.

No primeiro loop o indivíduo quer percorrer o vetor e verificar seu tamanho, para isso ele deve incrementar a variável contador,
o que ele não está fazendo. Além disso o while True não é necessário, já que sabemos o que iremos percorrer, que nesse caso
é o vetor A.

Dito isso irei apagar a condicional dentro do loop, pois ela não se satisfaz em nenhum caso, e também trocar o while por for,
para percorrer toda lista, e incremetar ao valor do contador toda vez que ele passar por um novo elemento, assim ele irá
me retornar o valor do tamanho da lista

dado o Valor do tamanho da lista o resto do código está funcional, ele funciona ordenando por seleção, jogando o menor 
número no início da lista, e consequentemente os ordenando em ordem crescente.  

'''

# SOLUÇÃO 2
'''

import random


def ordenacao_selecao(A):
    # Verificar o tamanho dinamicamente do vetor A.
    cont = 0
    while True:
        try:
            if A[cont] is None:
                n = cont

        except IndexError:
            n = cont
            break
        cont += 1

    # Percorre o arranjo A.
    for i in range(n):
        # Encontra o elemento mínimo em A.
        minimo = i

        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j

        # Coloca o elemento mínimo na posição correta.
        A[i], A[minimo] = A[minimo], A[i]
        # ???? (como posso colocar ele na posição corretapara a saída?)


A = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: ", A)

ordenacao_selecao(A)
print(A)

'''


# Código antigo
'''import random
def ordenacao_selecao(A):
    # Verificar o tamanho dinamicamente do vetor A.
    cont = 0
    while true:
        if A[cont] == null:
            n = cont
    # Percorre o arranjo A.
    for i in range(n):
        # Encontra o elemento mínimo em A.
        minimo = i

        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j

        # Coloca o elemento mínimo na posição correta.
        A[i], A[minimo] = A[minimo], A[i]
        #???? (como posso colocar ele na posição corretapara a saída?)

A = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: ", A)

ordenacao_selecao(A)

print("Arranjo ordenado:", A)'''
