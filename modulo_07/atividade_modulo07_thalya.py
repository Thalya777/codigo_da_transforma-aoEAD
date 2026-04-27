'''
codigos utilidades, jogos e o gerador de dados

'''


import random
import math
from faker import Faker
from datetime import datetime

# -------------------------------
# Funções matemáticas
# -------------------------------
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def potencia(base, expoente):
    return base ** expoente

# -------------------------------
# Gerador de dados falsos e datas
# -------------------------------
fake = Faker("pt_BR")

def gerar_pessoas(qtd=3):
    for _ in range(qtd):
        print("Nome:", fake.name())
        print("Email:", fake.email())
        print("Endereço:", fake.address())
        print("-" * 30)

def dias_para_fim_do_ano():
    hoje = datetime.now()
    fim_ano = datetime(hoje.year, 12, 31)
    diferenca = fim_ano - hoje
    print(f"📅 Faltam {diferenca.days} dias para o fim do ano.")

# -------------------------------
# Jogo de adivinhação
# -------------------------------
def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("🎲 Adivinhe o número entre 1 e 100!")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"✅ Parabéns! Você acertou em {tentativas} tentativas.")
            break
        else:
            diferenca = abs(numero_secreto - palpite)
            dica = "quente 🔥" if diferenca <= 10 else "frio ❄️"
            print(f"Errado! Está {dica}.")

# -------------------------------
# Programa principal (menu)
# -------------------------------
def menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Usar funções matemáticas")
    print("2 - Gerar dados falsos (Faker)")
    print("3 - Calcular dias até o fim do ano")
    print("4 - Jogar adivinhação")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Soma:", soma(5, 3))
        print("Subtração:", subtracao(10, 4))
        print("Potência:", potencia(2, 5))
    elif opcao == "2":
        gerar_pessoas(2)
    elif opcao == "3":
        dias_para_fim_do_ano()
    elif opcao == "4":
        jogar_adivinhacao()
    elif opcao == "0":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida!")