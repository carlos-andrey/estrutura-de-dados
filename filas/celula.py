class Celula:
    def __init__(self, proxima, elemento):
        self.__proxima = proxima
        self.__elemento = elemento

    @property
    def proxima(self):
        return self.__proxima
    
    @proxima.setter
    def proxima(self, proxima):
        self.__proxima = proxima
    
    @property
    def elemento(self):
        return self.__elemento
    
    def __repr__(self):
        return f'{self.elemento}'
