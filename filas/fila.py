from celula import Celula

class Fila:
    def __init__(self):
        self.__começo = None
        self.__fim = None
        self.__tamanho = 0
    

    def vazia(self):
        if self.__tamanho == 0:
            return True
        else:
            return False

    def adiciona(self, elemento):
        nova_celula = Celula(None, elemento)
        if self.__fim is None:
            self.__fim = nova_celula
        else: 
            self.__fim.proxima = nova_celula
            self.__fim = nova_celula
        if self.__começo is None:
            self.__começo =nova_celula
        self.__tamanho += 1
    
    def remove(self):
        if self.vazia() == False:
            self.__começo = self.__começo.proxima
        else:
            raise IndexError('Fila vazia')
        self.__tamanho -= 1

    def tamanho(self):
        return self.__tamanho

    def __repr__(self):
        if self.vazia() == False:
            ret = ''
            atual = self.__começo
            while atual:
                ret = ret + str(atual) + ' '
                atual = atual.proxima
            return ret
        else:
            return 'Fila vazia !!'
    
    