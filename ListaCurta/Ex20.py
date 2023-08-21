#Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
#Escreva uma mensagem de erro se a opção for inválida. Escolha a opção

opcao = int(input("escolha sua opção(1:soma 2:diferença 3:produto 4:divisão)"))
vlr1 = int(input("digite um valor:"))
vlr2 = int(input("digite um valor:"))

if opcao == 1:
    vlr1 + vlr2

if opcao == 2:
    vlr1 - vlr2

if opcao == 3:
    vlr1 * vlr2

if opcao == 4:
    vlr1/vlr2

