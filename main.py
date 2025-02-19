import json

def mapa_json(arquivo):  # função para ler o mapa de um arquivo JSON
    with open(arquivo, 'r') as f:  
        dados = json.load(f)  
        return dados["mapa"]  # Retorna o mapa

mapa = mapa_json("mapa.json") #função para ler o mapa do arquivo "mapa.json"

def encontrar_posicao(mapa, X):  # função para encontrar a posição de um elemento no mapa
    for i in range(len(mapa)):  # linhas 
        for j in range(len(mapa[i])):  # colunas do mapa
            if mapa[i][j] == X:  # se o elemento foi encontrado
                return i, j  # retorna a posição (linha, coluna)
    return None  # se o elemento não foi encontrado

def mostrar_mapa(mapa):  # função para exibir o mapa
    for linha in mapa:
        print(" ".join(linha))
    print("\n\n") 

def busca(mapa, inicio, objetivo):  # função para realizar a busca simples
    #Lista de todos os movimentos possiveis
    movimentos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    caminho = [inicio] # começa da posição inicial
    visitados = set([inicio]) #conjunto de visitados
    visitados.add(inicio)  # marca a posição inicial como visitada


    while caminho: 
        atual = caminho[-1] #ultima posição
        if atual == objetivo: #se atingiu o objetivo retorna o caminho
            return caminho

        for mov in movimentos: # percorre movimentos
            nova_posicao = (atual[0] + mov[0], atual[1] + mov[1]) # nova posição
        
            # se posição esta de acordo com o limite do mapa
            if 0 <= nova_posicao[0] < len(mapa) and 0 <= nova_posicao[1] < len(mapa[0]):
                if mapa[nova_posicao[0]][nova_posicao[1]] != '#' and nova_posicao not in visitados: # verifica se não é parede
                    caminho.append(nova_posicao) # add nova posição
                    visitados.add(nova_posicao) # marca como visitado
                    break
                
        else:
            caminho.pop() # não conseguiu mover

    return None # se não encontrou o objetivo

mapa = mapa_json("mapa.json") 


inicio = encontrar_posicao(mapa, 'S')  # encontra a posição inicial
objetivo = encontrar_posicao(mapa, 'T')  # encontra a posição do objetivo

caminho = busca(mapa, inicio, objetivo) 


if caminho:  # Se um caminho foi encontrado
    print("Caminho encontrado:")  
    for posicao in caminho:  
        mapa[posicao[0]][posicao[1]] = '*'  # marca a posição no mapa
        mostrar_mapa(mapa)  # mapa atualizado
    print(f"Número de movimentos: {len(caminho) - 1}") # imprime o número de movimentos
else:  # Se nenhum caminho foi encontrado
    print("Não foi possível encontrar um caminho.")  