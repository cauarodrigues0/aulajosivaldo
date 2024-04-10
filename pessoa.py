class Pessoa():
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def comer(self):
        return f"{self.nome} está comendo!"
    
    def beber(self):
        return f"{self.nome} está bebendo!"
    
    def falar(self, mensagem):
        return f"{self.nome} está falando: {mensagem}"
    
    def correr(self):
        return f"{self.nome} está correndo!"

if __name__ == "__main__":
    pessoa1 = Pessoa("João", 33, "12345678-90")
    pessoa2= Pessoa("Maria", "23", 241241421)

print("nome:",pessoa1.nome)
print("idade:",pessoa1.idade)
print("CPF:",pessoa1.cpf)

print("nome:",pessoa2.nome)
print("idade:",pessoa2.idade)
print("CPF:",pessoa2.cpf)

print(pessoa1.comer())
print(pessoa2.comer())

print(pessoa1.beber())
print(pessoa2.beber())

print(pessoa1.falar("bom dia"))
print(pessoa2.falar("boa tarde"))

print(pessoa1.correr())
print(pessoa2.correr())


