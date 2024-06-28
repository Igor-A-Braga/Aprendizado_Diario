# trocando valores de variavel

var1 = 12
var2 = 24


# var1, var2 = var2, var1

# print(f' var 1: {var1}, var 2: {var2}')

## --------


## operador condicional ternario 

# menor = var1 if var1 < var2 else var2


# print(menor)


# ---

# # generators 

# valores = [1,3,5,7,9,11,15,20]

# quadrados = (item**2 for item in valores )
# print(quadrados)


# for valor in quadrados:
#     print(valor)

# ---- 


# função enumerate()


# bebidas = ['cafe', 'cha', 'agua', 'suco']


# for i,item  in enumerate(bebidas):
#     print(f'indice: {i}, item {item}')
## -- 


temperaturas = [-1,-5,5,10,-30,45]
total = 0


# for i, t in enumerate(temperaturas):
#     if t < 0:
#         total += 1
# print(total)
## -- 
# for i, t in enumerate(temperaturas):
#     if t < 0:
#         print(f' a temperatura em {i} é negativa, com {t} celsius')
#### --


# gerenciamento de contexto com with


with open('arquivo.txt','r',encoding='utf-8') as a:
    for linha in a:
        print(linha)