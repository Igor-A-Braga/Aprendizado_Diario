#indica onde a variavel é visivel e acessivel
#escopo global e local


var_global = 'curso de python'


def escreve_texto():
    global var_global
    var_global = 'bancos de dados com sql'
    var_local = 'igor braga'
    print(f'Variavel global : {var_global}')
    print(f'Variavel local : {var_local}')


if __name__ == '__main__':
    print(f' executar a função escreve_texto() ')
    escreve_texto()

    print('tentar acessar as variaveis diretamente')
    print(f'Variavel global : {var_global}')