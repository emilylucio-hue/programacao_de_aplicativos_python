#A CLASSE: O modelo(a planta)
class Celular:

    def __init__(self,marca,modelo, cor, bateria = 100):
         self.marca = marca
         self.modelo = modelo
         self.cor = cor
         self.bateria = bateria
         self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria! Coloque para carregar.")
        else:
            self.ligado = True
            print(f"{self.modelo} Ligado!")

#Os objetos: Criados a partir da classe (as "casas")
celular1 = Celular ( "Iphone", "17 pro max","azul", 0)
celular2 = Celular ("Sansung", "Galaxy A26","preto")

#Acessando e alterando atributos
print(celular1.marca)

#Também podemos alterar diretamente
celular1.cor
celular1.ligar()
