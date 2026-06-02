'''

'''
 

def aula_tratamento_erros():
    print("---Desafio 1: divisão ---")

    try:
        numerador = int(input("Digite o numerador:"))
        denominador = int(input("digite o denominador:"))

        resultado = numerador / denominador

    except ValueError:
        print("Erro: Digite apenas numeros inteiros!")

    except ZeroDivisionError:
        print("Erro: O denominador não pode ser divido por zero!")

    except Exception as erro:
        print(f"Erro inesperado: {erro}")

    else:
        print(f"Sucesso! O resultado é: {resultado}")

    finally:
        print("--- Fim da Divisão ---")
                    

 