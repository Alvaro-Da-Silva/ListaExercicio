#Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
#peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
#aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.

nota1 = int(input("digite a primeira nota(peso 10)"))
nota2 = int(input("digite a segunda nota(peso 05)"))
nota3 = int(input("digite a terceira nota(peso 05)"))
media = nota1 + nota2 + nota3 / 3

if media >= 6:
    print("APROVADO")

else:
    print("REPROVADO")
