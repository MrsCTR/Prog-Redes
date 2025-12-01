# Importando a biblioteca SOCKET
import socket

import Constantes

# Criando o socket (socket.AF_INET -> IPV4 / socket.SOCK_DGRAM -> UDP)
sockClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
strMsgEntrada = socket.gethostbyname(socket.gethostname()) + 'Conectado...'
sockClient.sendto(strMsgEntrada.encode(Constantes.CODE_PAGE), Constantes.TUPLA_SERVER)

print('\n\nPara sair digite SAIR...\n\n')

while True:
   # Informando a mensagem a ser enviada para o servidor
   strMensagem = input('Digite a mensagem: ').lower().strip() 

   # Saindo do Cliente quando digitar SAIR
   if strMensagem == 'sair': break

   # Enviando a mensagem ao servidor      
   sockClient.sendto(strMensagem.encode(Constantes.CODE_PAGE), Constantes.TUPLA_SERVER)

''' # Recebendo resposta do servidor
   bytesMensagemRetorno, tuplaCliente = sockClient.recvfrom(Constantes.BUFFER_SIZE)
   intTamanhoMensagem = int(bytesMensagemRetorno.decode(Constantes.CODE_PAGE))
   if intTamanhoMensagem > Constantes.BUFFER_SIZE: Constantes.BUFFER_SIZE = intTamanhoMensagem

   bytesMensagemRetorno, tuplaOrigem = sockClient.recvfrom(Constantes.BUFFER_SIZE)
   strNomeHost = socket.gethostbyaddr(tuplaOrigem[0])[0].split('.')[0].upper()
   print(f'{tuplaOrigem} -> {strNomeHost}: {bytesMensagemRetorno.decode(Constantes.CODE_PAGE)}')
'''
# Fechando o socket
sockClient.close()