import requests
import tokensLLM

# ----------------------------------------------------------------------
def obterResultados (data: dict) -> str:
   try: 
      strResposta = data["choices"][0]["message"]["content"].strip()
   except Exception as e:
      print ("Erro na resposta do modelo ", e)
      strResposta = ""
   else:
      return strResposta
         

# ----------------------------------------------------------------------
def solicitarServico (servico: str, prompt: str) -> str:
   try:
      tokensLLM.DICT_HEADERS["Authorization"]          = f'Bearer {tokensLLM.DICT_SERVICES[servico]["token"]}'
      tokensLLM.DICT_PAYLOAD["model"]                  = tokensLLM.DICT_SERVICES[servico]["model"]
      tokensLLM.DICT_PAYLOAD["messages"][1]["content"] = prompt

      reqEnvio = requests.post("https://"+ 
                               tokensLLM.DICT_SERVICES[servico]["host"]+
                               tokensLLM.DICT_SERVICES[servico]["endpoint"], 
                               headers=tokensLLM.DICT_HEADERS, 
                               json=tokensLLM.DICT_PAYLOAD)
      
      reqEnvio.raise_for_status()
      data = reqEnvio.json()
      return obterResultados(data)
   except Exception as e:
      return f"\nERRO: {e}..."


# ----------------------------------------------------------------------
def selecionarServico() -> str:
   for id, strServico in enumerate(tokensLLM.DICT_SERVICES):
      print (f"{id+1} - {strServico}")

   try:
      intServico = int(input("Informe o nº do serviço LLM: "))
      strServico = tuple(tokensLLM.DICT_SERVICES.items())[intServico-1][0]
   except ValueError:
      strServico = "gemini"
      print (f"ERRO: LLM inválida. Usando a LLM default: {strServico}")

   return strServico
# ----------------------------------------------------------------------
