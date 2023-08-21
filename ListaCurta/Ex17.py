#Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
#para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
#conversão

tempC = int(input("digite a temperatura em celsius:"))
conversaoF = (tempC * 9/5) + 32
print(conversaoF)

tempF = int(input("digite a temperatura em fahrenhart:"))
conversaoC = (tempF - 32) * 5/9
print(conversaoC)
