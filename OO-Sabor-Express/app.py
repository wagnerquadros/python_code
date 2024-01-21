from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexica', 'Pimenta')
reastaurante_burger = Restaurante('Burger', 'Burger')

restaurante_praca.receber_avaliacao('Ademar', 10)
restaurante_praca.receber_avaliacao('Juca', 3)

def main():
    Restaurante.listar_restarantes()

if __name__ == '__main__':
    main()