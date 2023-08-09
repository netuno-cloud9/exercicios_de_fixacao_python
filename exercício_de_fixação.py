# -*- coding: utf-8 -*-
"""Exercício de Fixação.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jqoj2n2jjRHZvs3mjSCn5lpwtYIBGT8m

1. Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.
"""

lista_numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

for posicao, numero in enumerate(lista_numeros):
    print(f"Na posição {posicao+1} está o número: {numero}")

"""2.Ler uma lista de 10 números reais e mostre-os na ordem inversa."""

lista_reais = []
for i in range(10):
    numero_real = float(input(f"Digite o {i+1}º número real: "))
    lista_reais.append(numero_real)

lista_reais.reverse()

print("Lista na ordem inversa:", lista_reais)

"""3.Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média."""

lista_notas = []
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

media = sum(lista_notas) / len(lista_notas)

print("Notas:", lista_notas)
print("Média:", media)

"""4.Ler um vetor com 20 idades e exibir a maior e menor."""

lista_idades = []
for i in range(20):
    idade = int(input(f"Digite a {i+1}ª idade: "))
    lista_idades.append(idade)

maior_idade = max(lista_idades)
menor_idade = min(lista_idades)

print("Maior idade:", maior_idade)
print("Menor idade:", menor_idade)

"""5.Utilizando o del, remova todos os elementos da lista criada anteriormente até a lista ficar vazia."""

lista_idades = [1, 2, 3, 5, 10, 32, 43, 55, 65, 12, 34, 45, 80, 12, 15, 18, 52, 82, 13, 42]

del lista_idades[0:20]
#del lista_idades

print(lista_idades)

"""6.Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e sorvete!"""

#cria uma lista de compras
lista_de_compras_do_mes = []
x = int(input("informe a quantidade de itens na lista: "))

for i in range(x):
    compras = input("adicione um objeto na lista de compras: ")
    lista_de_compras_do_mes.append(compras)
    print(lista_de_compras_do_mes)
    print("*lista_de_compras_atualizada*!")

# estrura para verificar se esqueceu algum item
if "produtos de limpeza" not in lista_de_compras_do_mes:
    print("Não esqueça de comprar produtos de limpeza!")
if "sorvete" not in lista_de_compras_do_mes:
    print("Não esqueça de comprar sorvete!")

"""7.Agora «vá ao mercado» e delete apenas os produtos de limpeza da lista."""



lista_de_compras_do_mes = ['sorvete', 'macarrao', 'cafe', 'produtos de limpeza']

del lista_de_compras_do_mes [-1]
print(lista_de_compras_do_mes)

#alternativamente, poderia remover buscando por string
#if "produtos de limpeza" in lista_de_compras_do_mes:
#    lista_de_compras_do_mes.remove('produtos de limpeza')

""":8.Agora «vá à sorveteria» e se empanturre de sorvete e tire o sorvete da lista."""

barriga = []
lista_de_compras_do_mes = ['sorvete', 'macarrao', 'cafe', 'produtos de limpeza']

while True:
    print("Quer tomar sorvete?")
    print("Digite '1' para 'sim' e '2' para 'nao'")
    pergunta = input()  # Capture user's input
    if pergunta == '1':
        barriga.append('sorvete')
        del lista_de_compras_do_mes[0]
        print()
        print("Lista de compras atualizada:", lista_de_compras_do_mes)
        print("Conteúdo da barriga:", barriga)
        break

    elif pergunta == '2':
        print("Tem certeza?")
        continue
    else:
        print("Opção inválida! Digite '1' para 'sim' ou '2' para 'nao'.")

"""9.Faça uma função que determina se um número é par ou ímpar. Use o % para determinar o resto de uma divisão.Por exemplo: 3 % 2 = 1 e 4 % 2 = 0"""

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Exemplos de uso da função
num1 = 3
num2 = 4

print(f"{num1} é {par_ou_impar(num1)}.")
print(f"{num2} é {par_ou_impar(num2)}.")

"""
10.Duas palavras são um “par inverso” se uma for o contrário da outra. Escreva uma função que dado duas palavras,retorne True caso sejam.

"""

def verdadeiro_par_inverso(word1, word2):
    word1_cleaned = ''.join(word1.split()).lower()
    word2_cleaned = ''.join(word2.split()).lower()

    return word1_cleaned == word2_cleaned[::-1]

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

par_inverso = verdadeiro_par_inverso(palavra1, palavra2)

print(par_inverso)

"""
11.Escreva uma função que imprime todos os números primos entre 1 e 50
Dica: um número é primo se ele for divisível apenas por 1 e ele mesmo, use o operador % (resto da divisão) para isso."""

#Um número primo é um número inteiro maior que 1 que possui
#apenas dois divisores positivos: 1 e ele mesmo. Em outras palavras,
#um número primo não pode ser dividido uniformemente por qualquer outro número além desses dois.

def num_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False
#O loop começa com i = 5. Isso ocorre porque o menor número primo maior que 3 é 5.
#A condição de loop i * i <= n garante que o loop seja iterado até i atingir a raiz quadrada do número que está sendo verificado
#quanto à primalidade. Esta é uma otimização para reduzir o número de iterações necessárias para verificar a divisibilidade.
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
#Após cada iteração, i é incrementado em 6. Isso ocorre porque se i for 6n - 1, o próximo candidato primo potencial é 6n + 1 e vice-versa.
    return True

#De maneira alternativa
#for i in range(2, int(number ** 0.5) + 1):
#        if number % i == 0:
#            return False


def print_primos(start, end):
    for x in range(start, end + 1):
        if num_primo(x):
            print(x)

# Chamada da função para imprimir os números primos entre 1 e 50
print_primos(1, 50)