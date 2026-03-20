
# CLASSE

class Cachorro:

    def __init__(self,nome,cor,acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        if self.acordado:
            print(f"{self.nome} está latindo")
        else:
            print(f"{self.nome} está dormindo")

    def dormir(self):
        self.acordado = False
        print(f"{self.nome} ZzZzZzZzzZ")



# OBJETO

cao_1 = Cachorro("Rex","Amarelo",False)
cao_2 = Cachorro("Bob"," Branco e Preto")

# MÉTODOS
cao_1.latir()
cao_2.latir()

cao_1.dormir()
cao_1.latir()
cao_2.latir()

"""
Expected Output:

-Rex está dormindo
-Bob está latindo
-Rex ZzZzZzZzzZ
-Rex está dormindo
-Bob está latindo
"""

