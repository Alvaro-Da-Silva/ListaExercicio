#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
#de aumento

produto = float(input("digite o preço do produto:"))
aumento = produto * 0.15
desconto = produto - produto * 0.05 
print("o produto com um aumnetto de 15%:"aumento)
print("o produto com um desconto de 5%:"desconto)

