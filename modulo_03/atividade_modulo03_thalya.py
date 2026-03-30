print("Bem-vindo à Calculadora Simples!")  

num_hum = float(input("\nDigite o primeiro número: "))

num_dois = float(input("Digite o segundo número: "))

def exibir_menu():
    print("\n--- Menu de Operações ---")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. exponenciação (**)")
    print("0. Sair")

while True:
    exibir_menu()
    opção = input("\nEscolha uma operação (0-5): ")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. exponenciação (**)")
    print("0. Sair")  
    if opção == '1':
        resultado = num_hum + num_dois
        print(f"\nResultado: {num_hum} + {num_dois} = {resultado}")
    elif opção == '2':
        resultado = num_hum - num_dois
        print(f"\nResultado: {num_hum} - {num_dois} = {resultado}")
    elif opção == '3':
        resultado = num_hum * num_dois
        print(f"\nResultado: {num_hum} * {num_dois} = {resultado}")
    elif opção == '4':
        if num_dois != 0:
            resultado = num_hum / num_dois
            print(f"\nResultado: {num_hum} / {num_dois} = {resultado}")
        else:
            print("\nErro: Divisão por zero não é permitida.")
    elif opção == '5':
        resultado = num_hum ** num_dois
        print(f"\nResultado: {num_hum} ** {num_dois} = {resultado}")    
    elif opção == '0':
        print("\nSaindo da calculadora. Até mais!")
        break