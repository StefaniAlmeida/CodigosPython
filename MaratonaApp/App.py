from Model.Funcionario import Funcionario
from Model.Cliente import Cliente
from Model.Maratona import Maratona

def main():
    funcionario = Funcionario("Maria")
    cliente = Cliente("Jose")
    maratona = Maratona()
    maratona.correr(cliente)
    maratona.correr(Funcionario)


if __name__ == "__main__":
    main()
