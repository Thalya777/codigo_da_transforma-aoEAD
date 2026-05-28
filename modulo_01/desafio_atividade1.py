'''


'''

print('ola mundo')

while True:
    if print('O que deseja fazer?'):
        print('1 - entrar')
        print('0 - sair')
        escolha = input('digite sua escolha: ')
        if escolha == '1':
            print('Bem-vindo a calculadora')
            print('qual operação deseja ralizar?')
            print('1 - adição')
            print('2 - subtração')
            print('3 - multiplicação')
            print('4 - divisão')
            operacao = input('digite sua escolha: ')
            if operacao == '1':
                num1 = float(input('digite o primeiro número: '))
                num2 = float(input('digite o segundo número: '))
                resultado = num1 + num2
                print(f'O resultado da adição é: {resultado}')
            elif operacao == '2':
                num1 = float(input('digite o primeiro número: '))
                num2 = float(input('digite o segundo número: '))
                resultado = num1 - num2
                print(f'O resultado da subtração é: {resultado}')
            elif operacao == '3':
                num1 = float(input('digite o primeiro número: '))
                num2 = float(input('digite o segundo número: '))
                resultado = num1 * num2
                print(f'O resultado da multiplicação é: {resultado}')
            elif operacao == '4':
                num1 = float(input('digite o primeiro número: '))
                num2 = float(input('digite o segundo número: '))
                if num2 != 0:
                    resultado = num1 / num2
                    print(f'O resultado da divisão é: {resultado}')
                else:
                    print('Erro: divisão por zero não é permitida.')
            else:
                print('Operação inválida. Por favor, escolha uma operação válida.')
        elif escolha == '0':
            print('Saindo da calculadora. Até mais!')
            break   