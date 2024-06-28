from math import sqrt

class NumeroNegativoError(Exception):
    def __init__(self):
        pass

if __name__ == '__main__':
    while True:
        try:
            num = int(input('Digite um numero positivo : '))
            if num < 0:
                raise NumeroNegativoError
        except NumeroNegativoError:
            print(f'Foi fornecido um numero negativo ! ')
        else:
            print(f'A raiz quadrada de {num} é {round(sqrt(num),3)}')
        finally:
            print(f' fim de calculo')
