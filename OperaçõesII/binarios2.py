# Deslocamento binário
intCIDR = 24 #255.255.255.0
intMask = 0xFFFFFFFF
intMask = intMask>>(32-intCIDR)
intMask = intMask<<(32-intCIDR)
print(intMask) # Imprime 4294967040 (4.294.967.040)
