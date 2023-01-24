class Carro:
    def __init__(self, nome : str, marca : str, cor : str, ano : int):
        self.__nome = nome
        self.__marca = marca
        self.__cor = cor
        self.__ano = ano 
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, nova_marca):
        self.__nome = nova_marca


    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, novo_cor):
        self.__nome = novo_cor

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def cor(self, novo_ano):
        self.__nome = novo_ano
    
    def __repr__(self) -> str:
        return f'{self.__nome} {self.__cor} '