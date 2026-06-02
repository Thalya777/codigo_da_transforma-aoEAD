'''


'''



class Celular:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca 
        self.bateria = 100

    def fazer_chamada(self, duracao):
        try:
            gasto = int(duracao) * 2

            if self.bateria >= gasto:
                self.bateria -= gasto
                print(f"Chamada de {duracao} mim feita! Bateria: {self.bateria}%")

            else:
                print("Bateria insuficiente.")

        except ValueError:
            print("Erro: A Duração deve ser um numero inteiro!")


Meu_celular = Celular("Galaxy S21", "Samsung")
Meu_celular.fazer_chamada("5")                       
    