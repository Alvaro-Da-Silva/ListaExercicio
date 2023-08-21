#Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
#utilizando as seguintes formulas (onde h corresponde à altura)

h = float(input("digite sua altura:"))
sexo = input("Qual seu sexo(M ou F)")

if sexo == "M":
    pesoM = (72.7 ∗ h) − 58 

if sexo == "F":
    pesoF =(62, 1 ∗ h) − 44, 7

else:
    print("dado nao compativel")

print(pesoF)
print(pesoM)
