from datetime import datetime
nome = input("Digite seu nome: ")
hora_atual = datetime.now().strftime("%H:%M")
print(f"Olá, {nome}! Seja bem-vindo(a).")
print(f"Horário atual: {hora_atual}")