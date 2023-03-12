def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    else:
        return a / b


while True:

    print("Calculadora Simples")
    print("*******************")
    print("Selecione a operação desejada:")
    print("--------------------")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    print("-------------------")

    operacao = input("Digite sua opção 0/1/2/3/4:  ")

    if operacao == "0":
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "1":
        resultado = soma(num1, num2)
    elif operacao == "2":
        resultado = subtracao(num1, num2)
    elif operacao == "3":
        resultado = multiplicacao(num1, num2)
    elif operacao == "4":
        resultado = divisao(num1, num2)
    else:
        print("Opção inválida")
        continue
    print("Resultado: ", resultado)
    print()


    nova_operacao = input("Deseja gerar uma nova operação com o resultado anterior? (S/N): ")
    if nova_operacao.upper() == "S":
        num1 = resultado
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite sua opção (1/2/3/4): ")
        if operacao == "1":
            resultado = soma(num1, num2)
        elif operacao == "2":
            resultado = subtracao(num1, num2)
        elif operacao == "3":
            resultado = multiplicacao(num1, num2)
        elif operacao == "4":
            resultado = divisao(num1, num2)
        else:
            print("Opção inválida")
            continue

        print("Resultado: ", resultado)
        print()


print("Calculadora encerrada.")
