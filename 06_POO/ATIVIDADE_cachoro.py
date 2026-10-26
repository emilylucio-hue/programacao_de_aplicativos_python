class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
            print(f"{self.nome} diz: Au Au!")

    def mostrar_info(self):
        print(f"{self.nome}, {self.raca}, {self.idade}")


cachorro1 = Cachorro("Slinky", "Vira-lata", 5 )
cachorro2 = Cachorro("Layla", "Doberman", 7 )

cachorro1.mostrar_info()
cachorro2.mostrar_info()

cachorro1.latir()
cachorro2.latir()

cachorro1.idade = 6
cachorro1.mostrar_info()