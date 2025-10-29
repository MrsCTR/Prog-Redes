'''
Extraindo informações TCP-DUMP
TCPDUMP é uma ferramenta para captura de tráfego de rede.
'''

import os, sys

strDir = os.path.dirname(__file__)

strNomeArq = f'{strDir}//'

try:
    arqLeitura = open(strNomeArq, 'rb')
except Exception as erro:
    sys.exit(erro)
else:

    headerfile = arqLeitura.read(24)

    