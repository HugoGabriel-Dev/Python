from avaliacoes import Avaliacao
class restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliações'.ljust(25)} | {'Status'}')
        for restaurant in cls.restaurantes:
            print(f'{restaurant._nome.ljust(25)} | {restaurant._categoria.ljust(25)} | {str(restaurant.media_avaliacoes).ljust(25)} | {restaurant.ativo}')

    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'Desativo'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:    
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)  

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 'Sem avaliações ainda!'
        soma_avaliacoes = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_avaliacoes = len(self._avaliacoes)
        media = round(soma_avaliacoes / quantidade_avaliacoes)
        return f'{media:.1f}'