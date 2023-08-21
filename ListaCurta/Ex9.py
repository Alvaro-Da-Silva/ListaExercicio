#Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
#mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para Euros

nome = input("digite seu nome:")
dinheiro = float(input("digite seu montatante em reais:"))
dolar = dinheiro/4.98
euro = dinheiro/5.43
print("seu valor em dolares é de: "dolar)
print("seu valor em euros é de: "euro)
