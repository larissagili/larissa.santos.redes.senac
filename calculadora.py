def calculadora():
    # Exibe o título da calculadora
    print("=== Calculadora Simples ===")

    # Mostra as opções de operações matemáticas
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    # Recebe a escolha do usuário (qual operação deseja)
    escolha = input("Digite o número da operação (1/2/3/4): ")

    # Recebe o primeiro número digitado pelo usuário e converte para float
    num1 = float(input("Digite o primeiro número: "))

    # Recebe o primeiro número digitado pelo usuário e converte para float
    num2 = float(input("Digite o segundo número: "))

    # Verifica se a escolha foi soma
    if escolha == '1':
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")

    # Verifica se a escolha foi subtração
    elif escolha == '2':
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")

    # Verifica se a escolha foi multiplicação
    elif escolha == '3':
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")

    # Verifica se a escolha foi divisão
    elif escolha == '4':
        # Se o segundo número não for zero, realiza a divisão
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            # Caso o usuário tente dividir por zero, mostra erro
            print("Erro: divisão por zero não é permitida!")

    # Caso o usuário digite uma opção inválida
    else:
        print("Opção inválida.")

# Executa a função calculadora
calculadora()