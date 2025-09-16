from collections import deque

def bfs(grafo, inicio, objetivo):
    """Busca em Largura (BFS)"""
    visitados = set()
    fila = deque([[inicio]])

    while fila:
        caminho = fila.popleft()
        no = caminho[-1]

        if no == objetivo:
            return caminho

        if no not in visitados:
            visitados.add(no)
            for vizinho in grafo[no]:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)

    return None

def dfs(grafo, inicio, objetivo, caminho=None, visitados=None):
    """Busca em Profundidade (DFS)"""
    if caminho is None:
        caminho = [inicio]
    if visitados is None:
        visitados = set()

    no = caminho[-1]
    if no == objetivo:
        return caminho

    visitados.add(no)

    for vizinho in grafo[no]:
        if vizinho not in visitados:
            novo_caminho = dfs(grafo, inicio, objetivo, caminho + [vizinho], visitados)
            if novo_caminho:
                return novo_caminho

    return None

def dls(grafo, no, objetivo, profundidade, caminho, visitados):
    """Busca em Profundidade Limitada (DLS)"""
    if profundidade == 0 and no == objetivo:
        return caminho
    if profundidade > 0:
        for vizinho in grafo[no]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                resultado = dls(grafo, vizinho, objetivo, profundidade-1, caminho+[vizinho], visitados)
                if resultado:
                    return resultado
    return None

def iddfs(grafo, inicio, objetivo, profundidade_max=10):
    """Busca em Profundidade Iterativa (IDDFS)"""
    for profundidade in range(profundidade_max):
        visitados = set([inicio])
        resultado = dls(grafo, inicio, objetivo, profundidade, [inicio], visitados)
        if resultado:
            return resultado
    return None

if __name__ == "__main__":
    grafo = {
        'A': ['C', 'G', 'E'],
        'B': ['G'],
        'C': ['A', 'F'],
        'D': ['H', 'E'],
        'E': ['A', 'D', 'H'],
        'F': ['C', 'H'],
        'G': ['A', 'B', 'H'],
        'H': ['D', 'E', 'F', 'G']
    }

    print("BFS de A até H:", bfs(grafo, 'A', 'H'))
    print("DFS de A até H:", dfs(grafo, 'A', 'H'))
    print("IDDFS de A até H:", iddfs(grafo, 'A', 'H'))