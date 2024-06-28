# # exceção é um objeto que representa um erro que ocorreu ao executar o programa.
# # blocos try... except


# #dentro do try colocar colocar codigo que pode causar o erro
# # dentro do except pode colocar o possivel tratamento 

# numero1 = int(input('digite um numero : '))
# numero2 = int(input('digite outro numero : '))


# try:
#     r = round(numero1/numero2,2)

# except ZeroDivisionError:
#     print(f'Não é possivel dividir por zero!')

# else:
#     print(f' resultado {r}: ')


# -----


def divisao(x, y):
    return round(x / y, 2)


if __name__ == '__main__':
    while True:
        try:
            n1 = int(input(f'Digite um numero : '))
            n2 = int(input(f'Digite outro valor : '))
            break
        except ValueError:
            print('Ocorreu um erro ao tentar ler o valor, Digite novamente!')
    

    try: 
        resultado = divisao(n1,n2)
    except ZeroDivisionError:
        print(f'Não é possivel dividir o valor por zero')
    except:
        print(f'Ocorreu um erro desconhecido...')
    else: 
        print(f'Resultado {resultado}')
    finally:
        print('fim do calculo')

