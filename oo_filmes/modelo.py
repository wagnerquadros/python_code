class Filme:

    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:

    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


filme = Filme('Matrix', 2244, 123)
print(f'Nome: {filme.nome} - Ano: {filme.ano} - Duracao: {filme.duracao}')

serie = Serie('Atlanta', 2017, 3)
print(f'Nome: {serie.nome} - Ano: {serie.ano} - Temporadas: {serie.temporadas}')