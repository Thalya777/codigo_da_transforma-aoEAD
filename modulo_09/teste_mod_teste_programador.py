'''



'''


class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def verificar_status(self):
        try:
            entrada = input(f"Bateria do {self.modelo}:")

            nivel = float(entrada)

            if nivel < 0 or nivel > 100:
                print("Valor inválido! digite de 0 e 100%.") 

            elif nivel < 15:
                print(f"⚠😲 Bateria em {nivel}%!. Carregue ja!")

            elif nivel > 85:
                print(f"✅ Bateria em {nivel}%. carga exelente!")

            else:
                print(f"🔋 Bateria em {nivel}%. status normal.")

        except ValueError:
            print("Erro: Digite apenas numeros!")




cel = Celular("Samsung", "Galaxy S21")
cel.verificar_status()
                              