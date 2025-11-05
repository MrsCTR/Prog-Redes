import requests

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
   
   