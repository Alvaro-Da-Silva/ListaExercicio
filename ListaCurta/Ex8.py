#Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
#quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input("digite a altura da parede em M"))
largura = float(input("digite a largura da parede em M"))
area = altura * largura
tinta = area / 2
print("altura da parede"altura)
print("largura da parede"largura)
print("A area da parede e de"area)
print("para pintar a parede será preciso de"tinta"litros de tinta")