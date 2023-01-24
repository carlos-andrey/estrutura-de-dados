class Associacao:
    def __init__(self, placa : str, carro) -> None:
        self.__placa = placa
        self.__carro = carro
    
    @property
    def placa(self):
        return self.__placa 
    
    @placa.setter
    def placa(self, nova_placa):
        self.__placa = nova_placa
        
    @property
    def carro(self):
        return self.__carro
    
    @carro.setter
    def carro(self, novo_carro):
        self.__carro = novo_carro
    
    def __repr__(self) -> str:
        return f'{self.__placa} : {self.__carro}'
    