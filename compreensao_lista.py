# numeros = [1,4,7,9,10,12,21]


# quadrados = list(map(lambda num: num**2, numeros))

# print(quadrados)

#---

# numeros = [1,4,7,9,10,12,21]


# quadrados = [num**2 for num in numeros]

# print(quadrados)

#---


# criar uma lista de numeros pares de 0 a 10


# pares = [i for i in range(1201) if  i % 2 == 0]
# print(pares)


#--

# criar um programa que conte a quantidade de vogais dentro de um texto


# frase = 'a logica de python e fantastica e e um principio'

# vogais = ['a', 'e', 'i', 'o', 'u']

# lista_vogais = [i for i in frase if i in vogais]
# print(f'\n a frase possui {len(lista_vogais)} vogais : ')

# print(lista_vogais)

## -- 


# distributiva entre valores de duas listas
 
distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)


