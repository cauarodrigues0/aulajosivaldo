class Carro():
    def __init__(self, placa, modelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
if __name__ == "__main__":
    carro1 = Carro("ABC-1234", "Gol", 2010)
    carro2 = Carro("WAD-4721", "Fusca", 1980)

print(carro1.ano,carro1.modelo,carro1.placa)
print(carro2.ano,carro2.modelo,carro2.placa)
