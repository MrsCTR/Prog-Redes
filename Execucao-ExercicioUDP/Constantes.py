import os, socket


# ----------------------------------------------------------------------
HOST_IP_SERVER = socket.gethostbyname(socket.gethostname()) # Definindo IP do servidor

HOST_PORT      = 50000       # Definindo a porta

TUPLA_SERVER   = (HOST_IP_SERVER, HOST_PORT) # Definindo a TUPLA do servidor

BUFFER_SIZE    = 512         # Tamanho do buffer

CODE_PAGE      = 'utf-8'     # Definindo a página de codificação de caracteres

DIR_SERVER =  os.path.dirname(__file__) + '\\imagens\\' # Diretório das imagens no servidor

COMANDOS_SERVER = [ '\\?', '\\f'] # Comandos válidos no servidor
# ----------------------------------------------------------------------
