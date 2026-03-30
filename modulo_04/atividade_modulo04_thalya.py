class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, fruta):
        self.itens.append(fruta)
        print(f"{fruta} adicionada ao carrinho.")

    def remover_item(self, fruta):
        if fruta in self.itens:
            self.itens.remove(fruta)
            print(f"{fruta} removida do carrinho.")
        else:
            print(f"{fruta} não está no carrinho.")

    def mostrar_carrinho(self):
        if self.itens:
            print("Itens no carrinho:", ", ".join(self.itens))
        else:
            print("Carrinho vazio.")

def main():
    print("=== Cadastro de Usuário ===")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    idade = input("Digite sua idade: ")

    usuario = Usuario(nome, email, idade)
    carrinho = Carrinho()

    frutas_disponiveis = ["banana", "maçã", "uva", "abacaxi"]

    while True:
        print("\n=== Menu de Compras ===")
        print("Frutas disponíveis:", ", ".join(frutas_disponiveis))
        print("1 - Adicionar fruta ao carrinho")
        print("2 - Remover fruta do carrinho")
        print("3 - Mostrar carrinho")
        print("4 - Finalizar compras")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            fruta = input("Digite a fruta que deseja adicionar: ").lower()
            if fruta in frutas_disponiveis:
                carrinho.adicionar_item(fruta)
            else:
                print("Fruta não disponível.")
        elif opcao == "2":
            fruta = input("Digite a fruta que deseja remover: ").lower()
            carrinho.remover_item(fruta)
        elif opcao == "3":
            carrinho.mostrar_carrinho()
        elif opcao == "4":
            print("\n=== Resumo da Compra ===")
            print(f"Cliente: {usuario.nome}, Email: {usuario.email}, Idade: {usuario.idade}")
            carrinho.mostrar_carrinho()
            print("Obrigado pela compra!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()