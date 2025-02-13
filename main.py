import json  
from collections import deque

def mapa_json(arquivo):  # função para ler o mapa de um arquivo JSON
    with open(arquivo, 'r') as f:  
        dados = json.load(f)  
        return dados["mapa"]  # Retorna o mapa

mapa = mapa_json("mapa.json") #função para ler o mapa do arquivo "mapa.json"

def encontrar_posicao(Mapa, X):  # função para encontrar a posição de um elemento no mapa
    for i in range(len(mapa)):  # linhas 
        for j in range(len(mapa[i])):  # colunas do mapa
            if mapa[i][j] == X:  # se o elemento foi encontrado
                return i, j  # retorna a posição (linha, coluna)
    return None  # se o elemento não foi encontrado

def mostrar_mapa(mapa):  # função para exibir o mapa
    for linha in mapa:
        print(" ".join(linha))
    print("\n\n") 

def busca_largura(mapa, inicio, objetivo):  # função para realizar a busca em largura
    #Lista de todos os movimentos possiveis
    movimentos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    fila = deque()  # Cria uma fila para a BFS
    fila.append((inicio, []))  # Adiciona a posição inicial e o caminho até ela
    visitados = set()  # Conjunto para armazenar posições já visitadas
    visitados.add(inicio)  

    while fila:
        (atual, caminho) = fila.popleft()  # Retira o primeiro da fila
        
        # Se encontramos o objetivo, retornamos o caminho
        if atual == objetivo:
            return caminho + [atual]

        # Testamos os movimentos possíveis
        for mov in movimentos:
            nova_posicao = (atual[0] + mov[0], atual[1] + mov[1])
            
            # Verifica se está dentro dos limites do mapa
            if 0 <= nova_posicao[0] < len(mapa) and 0 <= nova_posicao[1] < len(mapa[0]):
                # Verifica se não é parede ('#') e se não foi visitado
                if mapa[nova_posicao[0]][nova_posicao[1]] != '#' and nova_posicao not in visitados:
                    fila.append((nova_posicao, caminho + [atual]))
                    visitados.add(nova_posicao)
    
    return None #Caso nao tenha caminho retorna None


inicio = encontrar_posicao(mapa, 'S')  # encontra a posição inicial
objetivo = encontrar_posicao(mapa, 'T')  # encontra a posição do objetivo

caminho = busca_largura(mapa, inicio, objetivo) 


if caminho:  # Se um caminho foi encontrado
    print("Caminho encontrado:")  
    for posicao in caminho:  
        mapa[posicao[0]][posicao[1]] = '*'  # marca a posição no mapa
        mostrar_mapa(mapa)  # mapa atualizado
    print(f"Número de movimentos: {len(caminho) - 1}") # imprime o número de movimentos
else:  # Se nenhum caminho foi encontrado
    print("Não foi possível encontrar um caminho.")  