import os, socket


# ----------------------------------------------------------------------
HOST_IP_SERVER = socket.gethostbyname(socket.gethostname()) # Definindo IP do servidor

HOST_PORT      = 50000       # Definindo a porta

TUPLA_SERVER   = (HOST_IP_SERVER, HOST_PORT) # Definindo a TUPLA do servidor

BUFFER_SIZE    = 512         # Tamanho do buffer

CODE_PAGE      = 'utf-8'     # Definindo a página de codificação de caracteres

# Diretório das imagens no servidor
DIR_SERVER =  os.path.dirname(__file__) + '\\imagens\\'
# ----------------------------------------------------------------------
# Comandos válidos no servidor
COMANDOS_SERVER = [ '\\?', '\\f']