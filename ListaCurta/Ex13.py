#Faça 4 listas:
#a. Adicione no mínimo 2 itens em cada lista.
#b. Crie uma lista das 4 listas criadas acima.
#c. Acesse (mostrar) algum item da lista livros.
#d. Remova um item da lista esporte.




listafilme = ["rambo","O Irlandês","Roma","mumia","O Poderoso Chefão"]
listajogo = ["fifa","cod","mk","need for speed","mario"]
listalivro = ["Ulysses","Moby Dick","O Senhor dos Anéis","Harry Potter"," O Hobbit"]
listaesporte = ["futebol","basquete","handebol","natação","quemada"]

listafilme.append("rambo1","rambo2")
listajogo.append("overwatch","hollow knight")
listalivro.append("arte da guerra","outsider")
listaesporte.append("futebol americano","roquei")

listaJunto = listaesporte+listafilme+listajogo+listalivro
del listaesporte[1]

