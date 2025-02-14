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

def busca(mapa, inicio, objetivo):  # função para realizar a busca simples
    #Lista de todos os movimentos possiveis
    movimentos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    caminho = [] # guarda o caminho percorrido
    atual = inicio #busca apartir da posição inicial

    while atual != objetivo: #busca ate seu objetivo
        avancou = False #saber se avançou
        for mov in movimentos: # percorre movimentos
            nova_posicao = (atual[0] + mov[0], atual[1] + mov[1]) # nova posição
        
            # se posição esta de acordo com o limite do mapa
            if 0 <= nova_posicao[0] < len(mapa) and 0 <= nova_posição[1] < len(mapa[0]):
                if mapa[nova_posicao[0]][nova_posicao[1]] != '#': # verifica se não é parede
                    caminho.append(nova_posicao) # add nova posição
                    atual = nova_posicao 
                    avancou = True # é possivel avançar
                    break
                
        if not avancou:# não conseguiu avançar, bloqueado
            return None # não caminho possivel

    return caminho # retorna caminho encontrado

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