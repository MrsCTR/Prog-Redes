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

    if intvalor < 0:
        sys.exit('Informe um valor inteiro positivo:')

    intQtbits = intvalor.bit_length()
#converte para binário retirando '0b'
    binvalor = bin(intvalor)[2:]

    if len(binvalor) % 8 != 0:

        intzeros = 8 - len(binvalor)
#exibir a saída
    print(f'\n {intvalor} em Binário.....: 0b{binvalor}\n')
