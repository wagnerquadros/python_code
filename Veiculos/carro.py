from Veiculos.veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self,  marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas


    def __str__(self):
        status = 'ligado' if self.ligado else 'Desligado'
        return f'{self.marca} {self.marca} - Portas: {self.portas} Status: {status}'
