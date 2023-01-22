from celula import Celula

class Pilha:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0
    
    def insere(self, elemento):
        nova_celula = Celula(elemento)
        nova_celula.proxima = self.__topo
        self.__topo = nova_celula
        self.__tamanho += 1

    def remove(self):
        if self.__tamanho > 0:
            celula = self.__topo
            self.__topo = self.__topo.proxima
            self.__tamanho -= 1
            return celula
        raise IndexError('A pilha esta vazia!!')

    def vazia(self):
        if self.__tamanho == 0:
            return True
        else:
            return False

    def __repr__(self):
        ret = ''
        atual = self.__topo
        while atual:
            ret = ret + str(atual.dado) + '\n'
            atual = atual.proxima
        return ret.strip('\n')