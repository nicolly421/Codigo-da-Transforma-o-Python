agenda = {}
while True:
    op = input("1 add / 2 ver / 3 sair: ")
    if op == "1":
        nome = input("Nome: ")
        tel = input("Tel: ")
        agenda[nome] = tel
    elif op == "2":
        print(agenda)
    elif op == "3":
        break