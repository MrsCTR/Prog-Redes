'''
Encontre a soma de todos os números que são iguais à soma do fatorial de seus dígitos.
145 é um número curioso, pois 1! + 4! + 5! = 1 + 24 + 120 = 145
'''
import math

# Pré-calcular e armazenar os fatoriais de 0 a 9 em uma lista
# Fatorial (i) armazena o valor de i!
Fatoriais = [math.factorial(i) for i in range(10)]

Num_Encontrados = []  # Lista para guardar os números necessários para condição.

# O limite superior 2.501.600 (7 * 9!) é um bom valor. Usar 2.500.000 é seguro.
Lim_Superior = 2500000 

# Itera por todos os números começando por 10 (pois 1 e 2 são trivialmente 1! e 2! e o problema exclui números com 1 dígito).
for n in range(10, Lim_Superior + 1):
    Soma_Fatoriais = 0
    Num_Temporario = n

    while Num_Temporario > 0:
        Digito = Num_Temporario % 10
        Soma_Fatoriais += Fatoriais[Digito]
        
        # *** LINHA QUE FALTAVA 1: Atualiza o número temporário para o próximo dígito ***
        Num_Temporario //= 10  # Divisão inteira para remover o dígito menos significativo

    # *** LINHA QUE FALTAVA 2: Verifica a condição e armazena o número ***
    if Soma_Fatoriais == n:
        Num_Encontrados.append(n)

# *** CÓDIGO FINAL: Encontra a soma dos números encontrados ***
Soma_Total = sum(Num_Encontrados)

print(f"Os números curiosos encontrados são: {Num_Encontrados}")
print(f"A soma total dos números é: {Soma_Total}")