from pessoa import Pessoa, pessoa1, pessoa2
from carro import Carro, carro1, carro2

print("nome:",pessoa1.nome)
print("idade:",pessoa1.idade)
print("CPF:",pessoa1.cpf)

print("nome:",pessoa2.nome)
print("idade:",pessoa2.idade)
print("CPF:",pessoa2.cpf)

print(pessoa1.comer())
print(pessoa2.comer())

print(carro1.ano,carro1.modelo,carro1.placa)
print(carro2.ano,carro2.modelo,carro2.placa)