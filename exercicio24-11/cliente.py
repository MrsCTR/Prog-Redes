# Importando a biblioteca SOCKET
import socket

# ----------------------------------------------------------------------
HOST_IP_SERVER = '' #'10.25.1.116'   # Definindo o IP do servidor
HOST_PORT       = 50000             # Definindo a porta
TUPLA_SERVER = (HOST_IP_SERVER, HOST_PORT)

BUFFER_SIZE     = 512               # Tamanho do buffer
CODE_PAGE       = 'utf-8'           # Definindo a página de 
                                    # codificação de caracteres
# ----------------------------------------------------------------------

# Criando o socket (socket.AF_INET -> IPV4 / socket.SOCK_DGRAM -> UDP)
sockClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('\n\nPara sair digite SAIR...\n\n')

while True:
   # Informando a mensagem a ser enviada para o servidor
   strMensagem = input('Digite a mensagem: ')

   # Saindo do Cliente quando digitar SAIR
   if strMensagem.lower().strip() == 'sair': break


   bytesMensagem = str(len(strMensagem)).encode(CODE_PAGE)
   sockClient.sendto(strMensagem.encode(CODE_PAGE), (TUPLA_SERVER))

   # Enviando a mensagem ao servidor      
   sockClient.sendto(strMensagem.encode(CODE_PAGE), (TUPLA_SERVER))
   
   # Recebendo mensagem do servidor
   bytesMensagem = sockClient.recvfrom(BUFFER_SIZE)

# Fechando o socket
sockClient.close()