def eh_solucao(estado):
    n = len(estado)
    for i in range(n):
        for j in range(i + 1, n):
            if estado[i] == estado[j]:  # Mesma linha
                return False
            if abs(estado[i] - estado[j]) == abs(i - j):  # Mesma diagonal
                return False
    return True


def mostrar_tabuleiro(estado):
    n = len(estado)
    for row in range(n):
        line = "".join('Q' if estado[col] == row else '.' for col in range(n))
        print(line)


def solucao_n_rainhas(n=8):
    solucoes = []

    def backtrack(estado=[]):
        col = len(estado)
        if col == n:
            if eh_solucao(estado):
                solucoes.append(estado[:])
            return
        for linha in range(n):
            if linha not in estado:
                estado.append(linha)
                if eh_solucao(estado):
                    backtrack(estado)
                estado.pop()

    backtrack()
    return solucoes


if __name__ == "__main__":
    solucoes = solucao_n_rainhas(8)
    print(f"Número total de soluções encontradas: {len(solucoes)}")
    print("Exemplo de solução:")
    mostrar_tabuleiro(solucoes[0])
