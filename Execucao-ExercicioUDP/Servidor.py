# Exercício: Elaborar um cliente (UDP) que informe o nome do arquivo e o servidor (UDP) envie para o cliente o arquivo solicitado. 

# Importando a biblioteca SOCKET
import socket

# ----------------------------------------------------------------------
HOST_IP_SERVER = '10.25.1.9' # Definindo o IP do servidor
HOST_PORT      = 50000       # Definindo a porta
TUPLA_SERVER   = (HOST_IP_SERVER, HOST_PORT)


BUFFER_SIZE    = 10          # Tamanho do buffer
CODE_PAGE      = 'utf-8'     # Definindo a página de 
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

   # Enviando o tamanho da mensagem ao servidor
   bytesTamanhoMensagem = str(len(strMensagem)).encode(CODE_PAGE)
   sockClient.sendto(bytesTamanhoMensagem, TUPLA_SERVER)
   
   # Enviando a mensagem ao servidor      
   sockClient.sendto(strMensagem.encode(CODE_PAGE), TUPLA_SERVER)

   # Recebendo resposta do servidor
   bytesMensagemRetorno, tuplaCliente = sockClient.recvfrom(BUFFER_SIZE)
   intTamanhoMensagem = int(bytesMensagemRetorno.decode(CODE_PAGE))
   if intTamanhoMensagem > BUFFER_SIZE: BUFFER_SIZE = intTamanhoMensagem

   bytesMensagemRetorno, tuplaOrigem = sockClient.recvfrom(BUFFER_SIZE)
   strNomeHost = socket.gethostbyaddr(tuplaOrigem[0])[0].split('.')[0].upper()
   print(f'{tuplaOrigem} -> {strNomeHost}: {bytesMensagemRetorno.decode(CODE_PAGE)}')

# Fechando o socket
sockClient.close()

#------------------------------------------------------------------
# servidor_arquivo_buffer10.py
import socket
import os

HOST_IP   = '0.0.0.0' 
HOST_PORT = 50000
TUPLA_HOST = (HOST_IP, HOST_PORT)

BUFFER_SIZE = 10 # TAMANHO DO BUFFER FORÇADO PARA 10
CODE_PAGE   = 'utf-8'

sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockServer.bind(TUPLA_HOST)

print(f"\nServidor UDP iniciado. Buffer de {BUFFER_SIZE} bytes.")

while True:
    try:
        # Recebe a solicitação do cliente (nome do arquivo)
        bytes_nome_arquivo, endereco_cliente = sockServer.recvfrom(BUFFER_SIZE)
        nome_arquivo = bytes_nome_arquivo.decode(CODE_PAGE)
        # NOTA: O nome do arquivo pode ser maior que 10 bytes, o recvfrom irá truncar se for o caso. 
        # Em um sistema real, você precisaria de mais lógica para garantir o nome completo.
        
        print(f"Recebida solicitação de '{nome_arquivo}' de {endereco_cliente}")

        if os.path.exists(nome_arquivo) and os.path.isfile(nome_arquivo):
            try:
                with open(nome_arquivo, 'rb') as f:
                    while True:
                        # Lê exatamente 10 bytes do arquivo
                        bytes_chunk = f.read(BUFFER_SIZE)
                        if not bytes_chunk:
                            break
                        # Envia o chunk (máximo de 10 bytes)
                        sockServer.sendto(bytes_chunk, endereco_cliente)
                
                # Envia um sinal para o cliente saber que o arquivo terminou
                # 'FIM_ARQ' tem 7 bytes e cabe no buffer de 10
                sockServer.sendto(b'FIM_ARQ', endereco_cliente) 
                print(f"Arquivo '{nome_arquivo}' enviado para {endereco_cliente}")

            except IOError as e:
                print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")
                # 'NAO_ACHADO' tem 10 bytes e cabe no buffer de 10
                sockServer.sendto(b'NAO_ACHADO', endereco_cliente) 

        else:
            print(f"Arquivo '{nome_arquivo}' não encontrado.")
            sockServer.sendto(b'NAO_ACHADO', endereco_cliente)

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Ocorreu um erro geral no servidor: {e}")

print("Servidor encerrando.")
sockServer.close()