strIP = '192.168.1.10'
intCIDR = 24
intIP = int.from_bytes(bytes([int(x) for x in strIP.split('.')]) ,'big')
intMask = 0xFFFFFFFF >> (32 - intCIDR) << (32 - intCIDR)
intIP_Rede = intIP & intMask 
print(intIP_Rede) # imprime 3232235776(3.232.235.776)