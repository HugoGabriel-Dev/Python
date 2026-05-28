class restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = True
        restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurant in restaurante.restaurantes:
            print(f'{restaurant._nome.ljust(25)} | {restaurant._categoria.ljust(25)} | {restaurant.ativo}')

    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'Desativo'

restaurante_plaza = restaurante('plaza', 'gourmet')
restaurante_pizza = restaurante('pizza', 'pizzas')

restaurante.listar_restaurantes()