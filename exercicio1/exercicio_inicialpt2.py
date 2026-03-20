"""
João tem uma bicicletaria e gostaria de registrar as vendas de
suas bicicletas. Crie um programa onde João informe: cor,
modelo, ano e valor da bicicleta vendida. Uma bicicleta pode:
buzinar, parar e correr. Adicione esses comportamentos!
"""

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo # Atributo
        self.ano = ano
        self.valor = valor

    def buzinar(self): # Método
        print("Plim Plim ..")
    
    def parar(self):
        print("Parando bicicleta..")
        print("Bicicleta parada")
    
    def correr(self):
        print("Vrummmmm...")
        print("Bicicleta correndo")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Vermelha","Caloi",2022,600)
b1.buzinar()
b1.parar()
b1.correr()

print(f"Bicicleta: {b1.cor} {b1.modelo} {b1.ano} {b1.valor}")

# b1.buzinar() é equivalente a eu fazer Bicicleta.buzinar(b1)

print(b1)   


"""
output:

Plim Plim ..
Parando bicicleta..
Bicicleta parada
Vrummmmm...
Bicicleta correndo
Bicicleta: Vermelha Caloi 2022 600
Bicicleta: cor=Vermelha, modelo=Caloi, ano=2022, valor=600
"""