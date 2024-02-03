class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def __str__(self):
        status = 'Ligado' if self.ligado else 'Desligado'
        return f'{self.marca} {self.modelo} - Status: {status}'