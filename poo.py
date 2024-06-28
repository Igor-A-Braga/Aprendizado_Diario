# # orientação a objetos = paradigma de programação.
# # python = multiparadigma 

# #classes e objetos 

class Veiculo: 
    def movimento(self):
        print(f'Sou um veicuilo e me desloco')
#colocando __antes do atributo, segue uma boa pratica ! 
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None


#criando Setter permite gravar um dado dentro de um elemento dentro da classe.obj.

    def set_num_registro(self, registro):
        self.__num_registro = registro



# criando getter que permite acessar atributos dentro da classe 

    def get_fabr_modelo(self):
        print(f'Modelo :{self.__modelo}, Fabricante : {self.__fabricante}. \n')
    
    def get_num_registro(self):
        return self.__num_registro


class Carro(Veiculo):
    #metodo __init__ será herdado
    def movimento(self):
        print('sou um carro andando pelas ruas')

class motocicleta(Veiculo):
    def movimento(self):
        print(f'2 rodas correm muito mais rapido que 4')

class Avião (Veiculo):
    #alterando metodo init
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        # usando super pega a referencia da classe que esta pegando heranca
        super().__init__(fabricante,modelo)

    def get_categoria(self):
        return self.__cat
    def movimento(self):
        print('sou um avião e sobrevoo lugares ')


if __name__ == '__main__':
    # meu_veiculo = Veiculo('BMW', 'X7')
    # meu_veiculo.movimento()
    # meu_veiculo.get_fabr_modelo()
    # meu_veiculo.set_num_registro(20050)
    # print(f' Registro : {meu_veiculo.get_num_registro()}\n')

    meu_carro = Carro('Mercedez', 'a350')
    meu_carro.movimento()
    meu_carro.get_fabr_modelo()

    seu_carro = Carro('audi', 'a5')
    seu_carro.movimento()
    seu_carro.get_fabr_modelo()

    minha_moto = motocicleta('honda', 'cg150')
    minha_moto.movimento()
    minha_moto.get_fabr_modelo()

    meu_aviao = Avião('Boeing', '747', 'Comercial')
    meu_aviao.movimento()
    meu_aviao.get_fabr_modelo()
    print(f'Categoria {meu_aviao.get_categoria()}')




