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

#--------------------------------------------------------------------------
# cliente_arquivo_buffer10.py
import socket
import sys
import os

HOST_IP_SERVER = '127.0.0.1' 
HOST_PORT      = 50000       
TUPLA_SERVER   = (HOST_IP_SERVER, HOST_PORT)

BUFFER_SIZE    = 10          # TAMANHO DO BUFFER FORÇADO PARA 10
CODE_PAGE      = 'utf-8'     

sockClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f'\nCliente iniciado com BUFFER_SIZE={BUFFER_SIZE}. Digite o nome do arquivo.')

while True:
    nome_arquivo_remoto = input('Digite o nome do arquivo (ex: imagem.jpg): ')

    if nome_arquivo_remoto.lower().strip() == 'sair': 
        sockClient.sendto(b'SAIR', TUPLA_SERVER)
        break
    
    nome_arquivo_local = f"recebido_{nome_arquivo_remoto}"

    # 1. Envia o nome do arquivo solicitado ao servidor
    # (O nome do arquivo pode ser maior que 10 bytes, mas isso é uma mensagem de controle, não o chunk de dados)
    sockClient.sendto(nome_arquivo_remoto.encode(CODE_PAGE), TUPLA_SERVER)

    print(f"Solicitação enviada. Aguardando chunks de 10 bytes para '{nome_arquivo_remoto}'...")

    # --- Lógica de Recebimento do Arquivo ---
    try:
        with open(nome_arquivo_local, 'wb') as f:
            while True:
                # Recebe dados do servidor (limite de 10 bytes por recvfrom)
                bytes_dados, endereco_servidor = sockClient.recvfrom(BUFFER_SIZE)

                # Verifica as mensagens de controle
                if bytes_dados == b'FIM_ARQ': # Sinal de fim de arquivo (7 bytes)
                    print(f"\nTransferência concluída. Arquivo salvo como '{nome_arquivo_local}'")
                    break
                elif bytes_dados == b'NAO_ACHADO': # Sinal de erro (10 bytes)
                    print(f"\nErro: O servidor não encontrou o arquivo '{nome_arquivo_remoto}'.")
                    if os.path.exists(nome_arquivo_local):
                        os.remove(nome_arquivo_local)
                    break
                else:
                    # Escreve o chunk recebido no arquivo
                    f.write(bytes_dados)
        
        print("Aguardando próxima solicitação...")

    except Exception as e:
        print(f"Ocorreu um erro durante o recebimento: {e}")
        break

sockClient.close()