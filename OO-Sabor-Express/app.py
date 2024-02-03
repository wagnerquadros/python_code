from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexica', 'Pimenta')
reastaurante_burger = Restaurante('Burger', 'Burger')

bebida_suco = Bebida('Suco de uva', 5.00, 'G')
prato_massa = Prato('Macarrao', 10.00, 'Massa Top')
prato_massa.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_massa)
def main():
    restaurante_praca.exibir_cardapio()

if __name__ == '__main__':
    main()