#Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se aposentar.
#As condições para aposentadoria são

idade = int(input("digite sua idade:"))
tempserviso = int(input("digite seu tempo de serviço"))

if idade > 60:
    print("APOSENTADO")

if tempserviso > 30:
    print("APOSENTADO")

if idade > 60 and tempserviso > 25:
    print("APOSENTADO")
