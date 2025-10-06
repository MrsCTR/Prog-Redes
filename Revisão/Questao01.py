'''
Encontre a soma de todos os números que são iguais à soma do fatorial de seus dígitos.
145 é um número curioso, pois 1! + 4! + 5! = 1 + 24 + 120 = 145
'''
import math

#Pré-calcular e armazenar os fatoriais de 0 a 9 em uma lista
#Fatorial (i) armazena o valor de i.
Fatoriais = [math.factorial(i) for i in range(10)]

Num_Encontrados = [] #Lista para guardar os números necessários para condição.

Lim_Superior = 250160 #Define o limite superior para que a busca não ultrapasse 7 dígitos e satisfaça a condição real é 7*9!=2.540.160.

# Itera por todos os números começando por 10 por que 1 e 2 não são considerados "somas" de acordo com o problema.
for n in range(10, Lim_Superior + 1):
    Soma_Fatoriais = 0
    Num_Temporario = n

    while Num_Temporario > 0:
        Digito = Num_Temporario % 10
        Soma_Fatoriais += Fatoriais [Digito]

