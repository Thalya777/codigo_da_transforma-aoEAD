'''

atividae na contruçao de um codigo que utliza objetos



'''



class Carro:
    def __init__(self,  Marca, Modelo, cor ):
        self.Marca = Marca
        self.Modelo = Modelo
        self.cor = cor
        self.ligar = False
        pass

    
    
carro1 = Carro("toyota", "supra", "preto")
carro1.ligar = ("Ligado")
print(f'O carro {carro1.Marca} {carro1.Modelo} de cor {carro1.cor} está {carro1.ligar}')



