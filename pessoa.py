class Pessoa():
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

if __name__ == "__main__":
    pessoa1 = Pessoa("João", 33, "12345678-90")
    pessoa2= Pessoa("Maria", "23", 241241421)

print("nome:",pessoa1.nome)
print("idade:",pessoa1.idade)
print("CPF:",pessoa1.cpf)

print("nome:",pessoa2.nome)
print("idade:",pessoa2.idade)
print("CPF:",pessoa2.cpf)