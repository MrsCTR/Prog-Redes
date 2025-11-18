'''
Encontre o total máximo de cima para baixo em triangle.txt (clique com o botão direito e 'Salvar link/destino como...'), 
um arquivo de texto de 15K contendo um triângulo com cem linhas.
'''
def encontrar_caminho_maximo(caminho_arquivo):
    """
    Calcula o caminho de soma máxima em um triângulo numérico.
    
    A abordagem usada é a Programação Dinâmica de baixo para cima:
    começa-se na penúltima linha e, para cada número, soma-se 
    o maior dos dois números adjacentes abaixo. O processo se repete
    até chegar ao topo.
    """
#Carregar e parsear o triângulo do arquivo
    try:
        with open(caminho_arquivo, 'r') as f: #Lê todas as linhas, remove espaços e divide em números, em seguida transforma em inteiro
            triangulo_str = [line.strip().split() for line in f]
            triangulo = []
            for linha_str in triangulo_str:
                triangulo.append([int(num) for num in linha_str])
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"ERRO ao processar o arquivo: {e}")
        return None
#Aplicando o algoritmo de Programação Dinâmica de baixo para cima
#Começa na penúltima linha (índice len(triangulo) - 2) e vai até a primeira linha (índice 0)
    for i in range(len(triangulo) - 2, -1, -1):
        for j in range(len(triangulo[i])): #Itera sobre cada número na linha atual
            valor_atual = triangulo[i][j] #Pega o valor atual na linha i
            valor_abaixo_esq = triangulo[i+1][j] #Pega os dois valores adjacentes na linha de baixo (i+1)
            valor_abaixo_dir = triangulo[i+1][j+1]
        #Atualiza o valor na linha atual (i) somando-o ao maior dos dois valores adjacentes abaixo.
        # Este novo valor representa o caminho máximo que pode ser alcançado a partir daquele ponto.
            triangulo[i][j] = valor_atual + max(valor_abaixo_esq, valor_abaixo_dir)
    return triangulo[0][0] #O valor restante no topo do triângulo (índice [0][0]) é o caminho de soma máxima.
# Substituindo 'triangle.txt' pelo caminho correto do arquivo
caminho_do_arquivo = 'triangle.txt' 
resultado_maximo = encontrar_caminho_maximo(caminho_do_arquivo)

if resultado_maximo is not None:
    print(f"\nO total máximo de cima para baixo no triângulo é: **{resultado_maximo}**")