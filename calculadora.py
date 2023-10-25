


while True:
    print("Calculadora Simples")
    print("Opções:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print("Resultado: ", resultado)
    elif opcao == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print("Resultado: ", resultado)
    elif opcao == "3":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print("Resultado: ", resultado)
    elif opcao == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado: ", resultado)
        else:
            print("Erro: divisão por zero")
    elif opcao == "0":
        print("Saindo da calculadora.")
        break
    else:
        print("Opção inválida. Tente novamente.")