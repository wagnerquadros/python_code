# Abra o arquivo para leitura
with open('dados.txt', 'r') as file:
    # Inicialize listas vazias para armazenar os valores
    segunda_coluna = []
    terceira_coluna = []

    # Itere sobre as linhas do arquivo
    for linha in file:
        # Divida a linha pelos separadores (vírgulas) e pegue a segunda e terceira colunas
        colunas = linha.strip().split(',')
        segunda_coluna.append(float(colunas[1]))
        terceira_coluna.append(float(colunas[2]))

# Exiba as listas
print("Segunda Coluna:", segunda_coluna)
print("Terceira Coluna:", terceira_coluna)


