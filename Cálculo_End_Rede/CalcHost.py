# Letra C
# Calculando primeiro Host de rede
# Entre IPv4 e máscara Sub-rede
# Define a variável 'strIP' com o endereço IP em formato de string 

IPv4   = '192.168.1.10'
print(f'O Endereço IPv4 é...........................: {IPv4}\n')

# Define a variável 'intCIDR' com o valor 24, que representa a quantidade 
# de bits da máscara de sub-rede (CIDR)
intCIDR = 24
print(f'Valor CIDR (bits na máscara)................: /{intCIDR}\n')

# Converte o endereço IP de string para um número inteiro, utilizando 
# 'big-endian'. A função 'int.from_bytes()' converte a sequência de bytes 
# gerada a partir do IP (convertido para inteiros) para um número inteiro, 
# respeitando a ordem 'big-endian' (byte mais significativo primeiro).
intIP      = int.from_bytes(bytes([int(x) for x in IPv4.split('.')]), 'big')
print(f'O Endereço IPv4 em binário é (32 bits)......: {intIP:032b}\n')  

# Calcula a máscara de sub-rede com base no valor de 'intCIDR', deslocando 
# os bits da máscara de 32 bits. O valor 0xFFFFFFFF tem todos os bits como 1. 
# O deslocamento à direita e à esquerda cria a máscara correspondente a 'CIDR'.
intMascara = 0xFFFFFFFF >> (32 - intCIDR) << (32 - intCIDR)
print(f'Máscara de sub-rede em binário é (32 bits)..: {intMascara:032b}\n')  

# Calcula o endereço de rede aplicando a operação bitwise 'AND' entre o IP e a 
# máscara de sub-rede. Isso resulta no endereço de rede (primeiro endereço da 
# sub-rede), pois todos os bits do host são zerados.
intIPRede  = intIP & intMascara
print(f'Endereço IPv4 da Rede em binário é (32 bits): {intIPRede:032b}\n')  

# Converte o endereço de rede (em formato inteiro) de volta para uma string de IP,
# dividindo em 4 partes (octetos) e unindo essas partes com pontos ('.'). 
# A função 'to_bytes(4)' converte o inteiro de volta para uma sequência de 4 bytes.
strIPRede = '.'.join([str(x) for x in intIPRede.to_bytes(4)])
print(f'O Endereço IPv4 da Rede é...................: {strIPRede}\n')