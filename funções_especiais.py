# funções lambda (anonima)

# sintaxe 
# lambda argumentos: expressão


# # criando que retorna o numero ao quadrado

# quadrado = lambda x: x**2

# for i in range(1,12):
#     print(quadrado(i))
##### ---
# verificando se o numero é par

# par = lambda x: x %2 == 0
# print(par(9))

#---
#convertendo firehint para celsius 



# f_c = lambda f: (f- 32)* 5/9


# print(f_c(212))

# --- 
# função map
# funcão que aplica função
#sintaxe : 
# map (função, iteravel)

# numero = [4,6,8,10,12,14]


# dobro = list(map(lambda i: i*2, numero))
# print(dobro)

# -----


# lista_palavras = ['python', 'é', 'uma', 'linguagem' , 'otima']


# funcao = list(map(str.upper, lista_palavras))

# print(funcao)
              
# --- 

# funçao filter ()

# sintaxe:

# filter(função , sequencia)


# def numeros_pares(n):
#     return n % 2 == 0

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# num_par = list(filter(numeros_pares, numeros))

# print(num_par)


# ----

# praticando com lambda 

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# num_impar = list(filter(lambda i: i % 2 != 0, numeros))

# print(num_impar)


# --

# função reduce ()
# realiza operações  cumulativas em sequencia de elemento
# sintaxe 

# reduce(função, sequencia , valor inicial)


from functools import reduce


# def mult(x, y):
#     return x * y


# numeross = [1,2,3,4,5,6]

# total = reduce(mult, numeross)

# print(total)


# --- 

# soma cumulativa dos quadrados de valores,, usando expressão lambda.


numeros = [1,2,3,4]
# *(1 ao quadrado + 2 ao quadrado)ao quadrado + 3ao quadrado)ao quadrado + 4 ao quadrado

total = reduce(lambda x,y: x**2 + y**2, numeros)

print(total)






 


