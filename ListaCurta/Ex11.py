#Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
#trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
#ao final mostrar seu nome e salário final calculado.

nome = input("digite seu nome:")
nmrhoras = int(input("digite suas horas de trabalho:"))
valorhora = float(input("digite valor da sua hora de trabalho"))
salariobruto = nmrhoras * valorhora
inss = salariobruto - salariobruto * 0.02
salariofinal = salariobruto - inss
print("salario final de:"salariofinal)