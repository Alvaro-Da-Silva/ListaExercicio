#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre ele 
dado = input("digite pelo teclado:")
print(" o dado e uma letra?:", dado.isalpha())
print("o dado é numerico?", dado.isnumeric())
print("o dado é so um espaço?", dado.isspace())
print("o dado é alfanumerico?", dado.isalnum())
print("o dado é Maiusculo?", dado.isupper())
print("o dado é Minusculo?", dado.islower())
print("o dado é capitalizada?", dado.istitle())
