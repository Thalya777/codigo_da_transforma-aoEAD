'''

'''


# Sistema de Login em Python

# Credenciais corretas (em um sistema real, isso viria de um banco de dados)
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

def sistema_login():
    tentativas = 3  # número máximo de tentativas permitidas
    
    while tentativas > 0:
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")
        
        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            print("✅ Login realizado com sucesso!")
            return True
        else:
            tentativas -= 1
            print(f"❌ Credenciais inválidas. Você ainda tem {tentativas} tentativa(s).")
    
    print("🚫 Número máximo de tentativas atingido. Acesso bloqueado.")
    return False

# Executa o sistema de login
sistema_login()