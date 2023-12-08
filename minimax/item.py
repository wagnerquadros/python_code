class Item:
    # Esta classe é utilizada para representar cada item na mochila. Cada item tem um peso (peso) e um valor (valor).
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

def mochila_minimax(itens, capacidade, maximizando_jogador):
    # Se a capacidade for menor ou igual a zero, ou não houver mais itens, retorna zero (caso base).
    if capacidade <= 0 or not itens:
        return 0

    if maximizando_jogador:
        # Maximizador (jogador) tenta maximizar o valor
        # Se for o turno do jogador maximizador, ele tenta maximizar o valor escolhendo o item que proporciona o maior valor adicional à mochila.
        valor_maximo = float('-inf')
        for i in range(len(itens)):
            nova_capacidade = capacidade - itens[i].peso
            valor = itens[i].valor + mochila_minimax(itens[:i] + itens[i + 1:], nova_capacidade, False)
            valor_maximo = max(valor_maximo, valor)
        return valor_maximo
    else:
        # Minimizador (adversário) tenta minimizar o valor
        # o jogador minimizador (adversário), ele tenta minimizar o valor escolhendo o item que proporciona o menor valor adicional à mochila.
        valor_minimo = float('inf')
        for i in range(len(itens)):
            nova_capacidade = capacidade - itens[i].peso
            valor = itens[i].valor + mochila_minimax(itens[:i] + itens[i + 1:], nova_capacidade, True)
            valor_minimo = min(valor_minimo, valor)
        return valor_minimo

# Exemplo de uso
itens = [Item(2, 3), Item(10, 29), Item(3, 1), Item(9, 5), Item(32, 15), Item(5, 3), Item(13, 11),Item(8, 4),Item(9, 7),Item(6, 6)]
capacidade_mochila = 50

valor_maximizado = mochila_minimax(itens, capacidade_mochila, True)
print("Valor Máximo (Maximizando Jogador):", valor_maximizado)

valor_minimizado = mochila_minimax(itens, capacidade_mochila, False)
print("Valor Mínimo (Minimizando Adversário):", valor_minimizado)
