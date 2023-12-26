class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, noveo_nome):
        self.__nome = noveo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}'

#================================

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} - Duração: {self.duracao}'


#================================

class Serie(Programa):
    def __init__(self, nome, ano,  temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} - Temporadas: {self.temporadas}'

#================================

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)




# -------------------------------------------------------------------

filme = Filme('matrix', 2244, 123)
serie = Serie('atlanta', 2017, 3)
tmep = Filme('Todo mundo em panico', 2001, 120)
lost = Serie('Lost', 2005, 7)

serie.dar_like()
tmep.dar_like()
lost.dar_like()
filme.dar_like()

print(f'Nome: {filme.nome} - Ano: {filme.ano} - Duracao: {filme.duracao} '
      f'- Likes: {filme.likes}')

serie.dar_like()
print(f'Nome: {serie.nome} - Ano: {serie.ano} - Temporadas: {serie.temporadas} '
      f'- Likes: {serie.likes}')

filmes_e_series = [filme,serie, tmep, lost]
playlist_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)


print(f'Lost está na playlist? {lost in playlist_fim_de_semana}')