import random

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def tabuleiro_cheio(tabuleiro):
    return all(tabuleiro[i][j] != ' ' for i in range(3) for j in range(3))

def minimax(tabuleiro, profundidade, maximizando):
    if verificar_vitoria(tabuleiro, 'X'):
        return -1
    elif verificar_vitoria(tabuleiro, 'O'):
        return 1
    elif tabuleiro_cheio(tabuleiro):
        return 0

    if maximizando:
        melhor_valor = float('-inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = 'O'
                    valor = minimax(tabuleiro, profundidade + 1, False)
                    tabuleiro[i][j] = ' '
                    melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        pior_valor = float('inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = 'X'
                    valor = minimax(tabuleiro, profundidade + 1, True)
                    tabuleiro[i][j] = ' '
                    pior_valor = min(pior_valor, valor)
        return pior_valor

def fazer_jogada_computador(tabuleiro):
    melhor_valor = float('-inf')
    melhor_jogada = None

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = 'O'
                valor = minimax(tabuleiro, 0, False)
                tabuleiro[i][j] = ' '
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = (i, j)

    tabuleiro[melhor_jogada[0]][melhor_jogada[1]] = 'O'

def main():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        exibir_tabuleiro(tabuleiro)

        linha = int(input("Digite a linha (0, 1 ou 2): "))
        coluna = int(input("Digite a coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = 'X'
        else:
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        if verificar_vitoria(tabuleiro, 'X'):
            exibir_tabuleiro(tabuleiro)
            print("Você ganhou!")
            break

        if tabuleiro_cheio(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        fazer_jogada_computador(tabuleiro)

        if verificar_vitoria(tabuleiro, 'O'):
            exibir_tabuleiro(tabuleiro)
            print("O computador ganhou!")
            break

        if tabuleiro_cheio(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

if __name__ == "__main__":
    main()
