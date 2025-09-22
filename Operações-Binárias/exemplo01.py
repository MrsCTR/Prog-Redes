import sys

try:
    intvalor = int(input('Digite um número inteiro: '))
except ValueError:
    sys.exit('Valor inválido. Por favor, informe um número inteiro.')
except KeyboardInterrupt:
    sys.exit('\n Programa interrompido pelo usuário.')
except Exception as erro:
    sys.exit(f'Erro inesperado: {erro}')
else:

    print(f'\n {intvalor} em Binário.....: {bin(intvalor)}\n')

