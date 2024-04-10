class Pessoa():
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def comer(self):
        return f"{self.nome} está comendo!"

if __name__ == "__main__":
    pessoa1 = Pessoa("João", 33, "12345678-90")
    pessoa2= Pessoa("Maria", "23", 241241421)

