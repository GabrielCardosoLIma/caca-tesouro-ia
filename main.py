import json  

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


def busca_largura(mapa, inicio, objetivo):  # função para realizar a busca em largura



inicio = encontrar_posicao(mapa, 'S')  # encontra a posição inicial
objetivo = encontrar_posicao(mapa, 'T')  # encontra a posição do objetivo


if caminho:  # Se um caminho foi encontrado
    print("Caminho encontrado:")  
    for posicao in caminho:  
        mapa[posicao[0]][posicao[1]] = '*'  # marca a posição no mapa
        mostrar_mapa(mapa)  # mapa atualizado
    print(f"Número de movimentos: {movimentos}")  # imprime o número de movimentos
else:  # Se nenhum caminho foi encontrado
    print("Não foi possível encontrar um caminho.")  