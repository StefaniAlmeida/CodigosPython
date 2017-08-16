from Model.Pessoa import Pessoa
class Cliente(Pessoa):
    def __init__ (self, nome):
        self.nome = nome
        super(cliente, self). __init__ (nome)
    def pagar(self):
        print("Paga de forma genérica")
