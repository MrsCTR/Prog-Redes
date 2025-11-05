import requests, os

strDirApp = os.path.dirname(__file__)

# Definindo a URL para requisição
strURL = 'http://www.globo.com'

#Definição de cabeçalhos HTTP
Headers = { 'User-Agent': 'MeuAppPython/1.0' }

 # Fazendo a requisição GET
try:
   response = requests.get(strURL, headers=Headers)
except requests.exceptions.ConnectTimeout:
   print(f'\nERRO: A conexão demorou demais (Timeout). O servidor pode estar offline ou lento...\n')
except requests.exceptions.RequestException as e:
   print(f'\nERRO: Ocorreu um erro ao fazer a requisição: {e}\n')
except Exception as e:
   print(f'\nERRO: {e}\n')

else:
   print('\nStatus Line da Resposta')
   print(f'\nStatus HTTP: {response.status_code} -> {response.reason}') #Exibição do status da resposta (status line)

#Exibição do headers da resposta (HTTP Headers)
   print(f'\nHeaders da Resposta')
   print(response.headers)

#Exibição do conteúdo da resposta (content)
   print(f'\nContent da Resposta')
   print(response.content)

   arqSaida = open(f'{strDirApp}// Content.txt', 'wb')
   arqSaida.write(response.content)
   arqSaida.close()