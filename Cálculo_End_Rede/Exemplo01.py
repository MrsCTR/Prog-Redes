'''
   Script para Cálculo de Faixa de Rede IPv4

   Este script realiza uma série de cálculos de rede com base em um endereço IPv4
   e uma máscara de sub-rede no formato CIDR. Ele foi projetado para ser
   educacional, demonstrando passo a passo como os cálculos são realizados
   em nível de bits.

   Variáveis de Entrada:
      - strIP: O endereço IPv4 que será analisado (ex: '192.168.1.10').
      - intCIDR: A máscara de sub-rede no formato CIDR (ex: 24).
'''

# ----------------------------------------------------------------------
# VARIÁVEIS DE ENTRADA (Altere estes valores para testar)
# Endereço IPv4 em formato string.
# Cada um dos quatro números (octetos) pode ir de 0 a 255.
strIP   = '192.168.1.10'

# Notação CIDR (Classless Inter-Domain Routing).
# Este número representa a quantidade de bits '1' no início da máscara de
# sub-rede, determinando o tamanho da porção de rede do endereço.
# Um /24, por exemplo, significa que os primeiros 24 bits são para a rede
# e os 8 bits restantes são para os hosts.
intCIDR = 24

# ----------------------------------------------------------------------
# 1 - CONVERSÃO PARA REPRESENTAÇÃO NUMÉRICA (BINÁRIA)
# Para realizar cálculos de rede, é muito mais fácil trabalhar com os
# endereços IP como números inteiros de 32 bits, em vez de strings.
# Converte a string '192.168.1.10' em um número inteiro.
# 1. `strIP.split('.')` -> Divide a string em uma lista: ['192', '168', '1', '10'].
# 2. `[int(x) for x in ...]` -> Converte cada elemento da lista para inteiro: [192, 168, 1, 10].
# 3. `bytes(...)` -> Converte a lista de inteiros em uma sequência de 4 bytes.
# 4. `int.from_bytes(..., 'big')` -> Interpreta esses 4 bytes como um único número inteiro de 32 bits.
#    O 'big' refere-se à ordem "big-endian", o padrão para redes.
intIP = int.from_bytes(bytes([int(x) for x in strIP.split('.')]), 'big')

# Calcula a máscara de sub-rede como um número inteiro.
# Cria uma sequência de 32 '1's (0xFFFFFFFF) e desloca para a esquerda
# '32 - intCIDR' vezes, preenchendo com '0's na direita.
# Ex: para /24, desloca 8 vezes para a esquerda.
intMascara = 0xFFFFFFFF << (32 - intCIDR) & 0xFFFFFFFF 

# ----------------------------------------------------------------------
# 2 - CÁLCULO DO ENDEREÇO DE REDE
# O endereço de rede é o primeiro endereço de uma sub-rede e é obtido
# aplicando a operação "E" (AND) bit a bit entre o endereço IP e a
# máscara de sub-rede. Esta operação zera a porção de host do IP.

# Operação AND bit a bit:
#   IP.....: 11000000.10101000.00000001.00001010  (192.168.1.10)
#   Máscara: 11111111.11111111.11111111.00000000  (255.255.255.0)
#   -------------------------------------------------------------
#   Rede...: 11000000.10101000.00000001.00000000  (192.168.1.0)
intIPRede = intIP & intMascara

# Converte o inteiro do endereço de rede de volta para o formato de string 'A.B.C.D'.
# `intIPRede.to_bytes(4)` -> Converte o inteiro em 4 bytes.
# `'.'.join(...)` -> Une os bytes convertidos em string com pontos.
strIPRede = '.'.join([str(x) for x in intIPRede.to_bytes(4, 'big')])

# ----------------------------------------------------------------------
# 3 - CÁLCULO DO PRIMEIRO HOST VÁLIDO
# O primeiro endereço que pode ser atribuído a um dispositivo na rede é o
# endereço de rede + 1.

# A operação "OU" (OR) bit a bit com 1 (0x00000001) garante que o último bit
# seja '1', resultando no primeiro endereço de host.
#   Rede.....: ...00000000
#   OU 1.....: ...00000001
#   ----------------------
#   Resultado: ...00000001
intIPPrimeiroHost = intIPRede | 0x00000001
strIPPrimeiroHost = '.'.join([str(x) for x in intIPPrimeiroHost.to_bytes(4, 'big')])

# ----------------------------------------------------------------------
# 4 - CÁLCULO DO ENDEREÇO DE BROADCAST
# O endereço de broadcast é o último endereço da sub-rede. Ele é usado
# para enviar dados para todos os dispositivos na mesma sub-rede.
# É calculado preenchendo a porção de host do endereço de rede com bits '1'.

# `~intMascara` inverte todos os bits da máscara, criando uma "máscara invertida"
# (wildcard mask) que isola a porção de host (ex: 00000000.00000000.00000000.11111111).
# A operação "OU" (OR) com esta máscara invertida liga todos os bits de host
# do endereço de rede.
#
#   Rede.....: 11000000.10101000.00000001.00000000
#   Mascara..: 00000000.00000000.00000000.11111111
#   -------------------------------------------------
#   Broadcast: 11000000.10101000.00000001.11111111 (192.168.1.255)
intIPBroadcast = intIPRede | (~intMascara & 0xFFFFFFFF) # '& 0xFFFFFFFF' garante que o número seja de 32 bits
strIPBroadcast = '.'.join([str(x) for x in intIPBroadcast.to_bytes(4, 'big')])

# ----------------------------------------------------------------------
# 5 - CÁLCULO DO ÚLTIMO HOST VÁLIDO
# O último endereço que pode ser atribuído a um dispositivo é o
# endereço de broadcast - 1.

# A operação "E" (AND) com `0xFFFFFFFE` (que é ...11111110 em binário)
# simplesmente desliga o último bit do endereço de broadcast.
#   Broadcast: ...11111111
#   AND      : ...11111110
#   -----------------
#   Resultado: ...11111110
intIPUltimoHost = intIPBroadcast & 0xFFFFFFFE
strIPUltimoHost = '.'.join([str(x) for x in intIPUltimoHost.to_bytes(4, 'big')])

# ----------------------------------------------------------------------
# 6 - CONVERSÃO DA MÁSCARA PARA DECIMAL
# Converte o inteiro da máscara de sub-rede de volta para o formato de
# string 'A.B.C.D' para fácil visualização (ex: 255.255.255.0).
strIPMascara = '.'.join([str(x) for x in intMascara.to_bytes(4, 'big')])

# ----------------------------------------------------------------------
# 7 - CÁLCULO DO NÚMERO DE HOSTS VÁLIDOS
# A quantidade de hosts disponíveis em uma sub-rede é calculada pela
# fórmula 2^n - 2, onde 'n' é o número de bits de host.
# O '- 2' é porque o primeiro endereço (rede) e o último (broadcast)
# são reservados e não podem ser usados por dispositivos.

# (32 - intCIDR) calcula o número de bits de host (n).
# 2 ** n calcula o total de endereços na sub-rede.
intQtHosts = 2 ** (32 - intCIDR) - 2

# ----------------------------------------------------------------------
# EXIBIÇÃO DOS RESULTADOS
# Imprime os resultados de forma organizada, mostrando tanto a representação
# decimal pontilhada quanto a representação binária de 32 bits para cada valor.

# Dados de Entrada
print('\nRESULTADOS OBTIDOS (os IPs estão no formato IPv4):\n')
# `:>15` alinha a string à direita em um espaço de 15 caracteres.
# `:032b` formata o inteiro como um número binário de 32 bits, com zeros à esquerda.
print(f'O Endereço é (IPv4).........................: {strIP:>15} -> {intIP:032b}')
print(f'O IP da Máscara para o CIDR /{intCIDR:<2} é...........: {strIPMascara:>15} -> {intMascara:032b}\n')

# Resultados dos Cálculos
print(f'O Endereço da Rede é (IPv4).................: {strIPRede:>15} -> {intIPRede:032b}')
print(f'O Endereço do 1º Host da Rede é (IPv4)......: {strIPPrimeiroHost:>15} -> {intIPPrimeiroHost:032b}')
print(f'O Endereço do Broadcast da Rede é (IPv4)....: {strIPBroadcast:>15} -> {intIPBroadcast:032b}')
print(f'O Endereço do Último Host da Rede é (IPv4)..: {strIPUltimoHost:>15} -> {intIPUltimoHost:032b}')
print(f'A Quantidade de Hosts Válidos na Rede é.....: {intQtHosts:>15}\n')