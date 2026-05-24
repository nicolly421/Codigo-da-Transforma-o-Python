numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
if numero1 > numero2:
    print("Maior:", numero1)
elif numero2 > numero1:
    print("Maior:", numero2)
else:
    print("Iguais")

classificacao_idade.py
idade = int(input("Digite sua idade: "))
if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")
