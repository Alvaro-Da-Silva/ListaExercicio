#Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
#tela dizendo se está “quente”, “frio” ou “agradável”

temp = float(input("qual temperatura esta agora?"))

if temp >= 25:
    print("esta quente")

if temp <= 24 and >=18:
    print("esta agradavel")

if temp < 17:
    print("esta frio")