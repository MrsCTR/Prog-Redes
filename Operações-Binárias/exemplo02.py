import sys

try:
    strIP = int(input('Digite um endereço IP (Formato IPv4): '))
except ValueError:
    sys.exit('Valor inválido. Por favor, informe um número inteiro.')
except KeyboardInterrupt:
    sys.exit('\n Programa interrompido pelo usuário.')
except Exception as erro:
    sys.exit(f'Erro inesperado: {erro}')
else:

   lstOctetos = strIP.split('.')

   if 