# funções
# modularização - Reuso de codigo, Legibilidade do programa.


#def nome_função ([argumentos]):
#    instruções

# def mensagem():
#     print('Igor, Cientista de dados')
#     print('Aprendendo python')


# mensagem()
#---------


#função com argumentos

# def soma(a, b):
#     print(a+b)

# soma(10, 9)

#------


# def multiplicacao (x, y):
#     return x * y

# a = 5
# b = 8

# c = multiplicacao(a, b)

# print(f' O  produto de {a} e {b} resulta em {c}')

#---

# def divisao (x, y):
#     return (x / y)


# a = 10
# b = 5
# c = divisao(a, b)


# print(f' O valor de {a} dividido por {b} resulta em {c}')

# -------

# def funcao_que_dividi (x, y):
#     if y !=0:
#         return x/y
#     else:
#         return('impossivel dividir numero por zero!')



# if __name__ == '__main__':

#     a = int(input('Digite um valor : '))
#     b = int(input('Digite outro valor : '))

#     resultado = funcao_que_dividi(a, b)

#     print(f'o resultado de {a} dividido por {b} é igual a {resultado}')


#----
#for - para cada i ou x dentro do valor(colocado na função) 

# def funcao_xx2 (f1):
#     lista_vazia = []
#     for i in f1:
#         lista_vazia.append(i **2)
#     return lista_vazia


# if __name__ == '__main__':
#     lista_de_valores_pelo_user = [4,8,12,16,20]
#     meu_resultado = funcao_xx2(lista_de_valores_pelo_user)
#     for x in meu_resultado:
#         print(x)

# ----------------------



# def funcao_contagem(numero=11, caractereee='+'):
#     for i in range(1, numero):
#         print(caractereee)

# if __name__ == '__main__':
#     funcao_contagem(numero=7,caractereee='$')
# #posso colocar os padrões na ordem por exemplo funcao contagem (7,'$')


####-------------


x = 5
y = 6 
z = 3

def soma_ou_mult(a,b,c=0):
    if c == 0:
        return a*b
    else:
        return a + b + c

if __name__ == '__main__':
    resultado = soma_ou_mult(x,y,z)
    print(resultado)



