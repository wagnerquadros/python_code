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

#================================

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao



#================================

class Serie(Programa):
    def __init__(self, nome, ano,  temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas



# -------------------------------------------------------------------

filme = Filme('matrix', 2244, 123)

print(f'Nome: {filme.nome} - Ano: {filme.ano} - Duracao: {filme.duracao} '
      f'- Likes: {filme.likes}')

serie = Serie('atlanta', 2017, 3)
serie.dar_like()
print(f'Nome: {serie.nome} - Ano: {serie.ano} - Temporadas: {serie.temporadas} '
      f'- Likes: {serie.likes}')


