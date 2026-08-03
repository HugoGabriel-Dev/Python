from classes import restaurante

restaurante_praça = restaurante('praça', 'gourmet')
restaurante_plaza = restaurante('plaza', 'pizzaa')
restaurante_japa = restaurante('japones', 'japonesaa')

restaurante_praça.receber_avaliacao('Hugo', 2)
restaurante_praça.receber_avaliacao('Ana', 6)
restaurante_praça.receber_avaliacao('Junior', 3)

restaurante_japa.alternar_estado()

def main():
    restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()