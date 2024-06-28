# recursividade 


# (NUM) - VARIAVEL

# formula geral para o fatorial 
# fatorial (NUM) = 1, se (NUM) = 0 ou se (NUM) = 1(caso base.)
# fatorial (NUM) = (NUM) * fatorial(numero -1 ), para cada (N UM) > 1  'Caso Recursivo'
# 4! -> 4 * fatorial (3) = 4 * 3 * fatorial (2) = 4 * 3 * 2 * fatorial (1) - >
# 4! = 4*3*2*1 =  24 (até chegar no caso base e o valor alimenta a função.)


def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero -1)



if __name__ == '__main__':
    x = int(input('Digite um numero inteiro positivo para calcular seu fatorial : '))
    try:
        resultado= fatorial(x)
    except RecursionError:
        print('o Numero fornecido é muito grande ou negativo. ')
    else:
        print(f'o fatorial de {x} é {resultado}')