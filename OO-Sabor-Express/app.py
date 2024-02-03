from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexica', 'Pimenta')
reastaurante_burger = Restaurante('Burger', 'Burger')

bebida_suco = Bebida('Suco de uva', 5.00, 'G')
prato_massa = Prato('Macarrao', 10.00, 'Massa Top')

def main():
    print(bebida_suco)
    print(prato_massa)

if __name__ == '__main__':
    main()