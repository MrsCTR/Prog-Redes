import socket

strNomeHost = socket.gethostname()
strIpHost = socket.gethostbyname(strNomeHost)
tupDadosHost = socket.gethostbyaddr(strIpHost)
tupAllIPs = socket.getaddrinfo(strNomeHost, None)

print(f'Nome do Host..: {strNomeHost}')
print(f'IP do Host..: {strIpHost}')
print(f'Dados do Host..: {tupDadosHost}')
print(f'All IP..: {tupAllIPs}')
