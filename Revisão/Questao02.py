'''
Pode-se observar que o número, 125874, e seu duplo, 251748, contêm exatamente os mesmos dígitos, mas em uma ordem diferente.
Encontre o menor inteiro positivo, x, de modo que 2x,3x,4x,5x, e 6x, contêm os mesmos dígitos.
'''
def mesmos_digitos(n1, n2):
    """
    Verifica se dois números contêm exatamente os mesmos dígitos,
    independentemente da ordem. Isso é feito comparando as strings
    de dígitos ordenadas de cada número.
    """
    return sorted(str(n1)) == sorted(str(n2))

def Euler_52():
    """
    Encontra o menor inteiro positivo, x, tal que 2x, 3x, 4x, 5x,
    e 6x contenham os mesmos dígitos.
    """
    x = 1
#O loop principal continua indefinidamente até que a solução seja encontrada
    while True:
        #Pega a representação ordenada dos dígitos de x para comparação
        digitos_x_ordenados = sorted(str(x))
        todos_iguais = True
        for i in range(2, 7): #Verifica todos os múltiplos de 2x a 6x
            multiplo = i * x
#Se a string ordenada de dígitos de qualquer múltiplo for diferente da de x,a condição falha e passamos para o próximo x
            if sorted(str(multiplo)) != digitos_x_ordenados:
                todos_iguais = False
                break
        if todos_iguais:  #Se a condição for satisfeita para todos os múltiplos, x é a resposta
            return x
        
        x += 1 #Passa para o próximo inteiro para testar

resultado = Euler_52()
print(f"O menor inteiro positivo, x, é: {resultado}")
print(f"Os múltiplos são: 2x={2*resultado}, 3x={3*resultado}, 4x={4*resultado}, 5x={5*resultado}, 6x={6*resultado}")