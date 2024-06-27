import random 


# print ('Gerar cinco numeros aleatorios entre 1 e 50 \n')
#  for i in range(5):
#      n = random.randint(1,50)
#      print(f' Numero Gerado: {n} ')



# #gerando numeros de ponto flutuante
# # usand o round () e colocando uma , após a condição inicial, podemos colocar quantas casas queremos 
# # valor = random.random()
# # print(f'Numero gerado : {round(valor * 10, 2)}')


# #usando uniform n preciso adaptar com * 10 

# valor = random.uniform(1,100)
# print(f' Numero: {round(valor,2)}')



### . choice seleciona um numero aleatorio 
# lista = [2,4,6,8,10,12,14,3,6,9,12]

# n = random.choice(lista)

# print(n)

#. sample seleciona varios itens especificados a quantidade após a virgula. 
lista = [2,4,6,8,10,12,14,3,6,9,12]
#n= random.sample(lista, 3)

#print(n)


# a função random.shuffle embaralha a ordem 

embaralhando = random.shuffle(lista)

print(lista)
