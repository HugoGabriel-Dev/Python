class restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = True
        restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurant in restaurante.restaurantes:
            print(f'{restaurant.nome} | {restaurant.categoria} | {restaurant.ativo}')

    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'Desativo'

restaurante_plaza = restaurante('plaza', 'gourmet')
restaurante_pizza = restaurante('pizza', 'pizzas')

restaurante.listar_restaurantes()