class Celula:
    def __init__(self, label) -> None:
        self.__label = label
        self.__esquerda = None
        self.__direita = None

    @property
    def label(self):
        return self.__label 
    
    @label.setter
    def label(self, label):
        self.__label = label

    @property
    def esquerda(self):
        return self.__esquerda 
    
    @esquerda.setter
    def esquerda(self, esquerda):
        self.__esquerda = esquerda

    @property
    def direita(self):
        return self.__direita 
    
    @direita.setter
    def direita(self, direita):
        self.__direita = direita

    def __repr__(self):
        f"{self.__label}"
    