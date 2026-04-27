'''
ATIVIDADE 08

'''



class Carro:
    def __init__(self,  Marca, Modelo, cor ):
        self.Marca = Marca
        self.Modelo = Modelo
        self.cor = cor
        self.ligar = False
        pass

    
    
carro1 = Carro("Bugatti", "Chiron", "preto")
carro1.ligar = ("Ligado")
print(f"Marca: {carro1.Marca}, Modelo: {carro1.Modelo}, Cor: {carro1.cor}, Ligado: {carro1.ligar}")





