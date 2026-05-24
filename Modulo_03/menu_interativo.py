while True:
    print("\n1 - Soma")
    print("2 - Subtração")
    print("3 - Sair")
    opcao = input("Escolha: ")
    if opcao == "1":
        a = int(input("Número 1: "))
        b = int(input("Número 2: "))
        print(a + b)
    elif opcao == "2":
        a = int(input("Número 1: "))
        b = int(input("Número 2: "))
        print(a - b)
    elif opcao == "3":
        break