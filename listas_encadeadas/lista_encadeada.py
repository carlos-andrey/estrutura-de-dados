from celula import Celula

class ListaEncadeada:
    def __init__(self):
        self.__primeira = None
        self.__ultima = None
        self.__total_de_elementos = 0
        
    def indice(self, elemento):
        ponteiro = self.__primeira
        indice = 0
        while ponteiro:
            if ponteiro.elemento == elemento:
                return indice
            else:
                ponteiro = ponteiro.proxima
                indice += 1
        raise ValueError('{} is not in list'.format(elemento))

    def adicionar_comeco(self, elemento):
        nova_celula = Celula(self.__primeira, elemento)
        self.__primeira = nova_celula
        self.__total_de_elementos += 1
    
    def adicionar_fim(self, elemento):
        if self.__primeira:
            atual = self.__primeira
            while atual.proxima:
                atual = atual.proxima
            atual.proxima = Celula(None, elemento)
            self.__total_de_elementos = self.__total_de_elementos + 1
        else:
            self.adicionar_comeco
            self.__total_de_elementos = self.__total_de_elementos + 1


    def adicionar_posicao(self, posicao, elemento):
        if posicao == 0:
            self.adicionar_comeco(elemento)
        elif posicao == self.__total_de_elementos:
            self.adicionar_fim(elemento)
        else:
            anterior = self.pegar(posicao-1)
            nova_celula = Celula(anterior.proxima, elemento)
            anterior.proxima = nova_celula
            self.__total_de_elementos +=1

    def pegar(self, posicao):
        if posicao < 0 or posicao >= self.__total_de_elementos:
            raise Exception('Posicao invalida')
        atual = self.__primeira

        for _ in range(0, posicao):
            atual = atual.proxima
        return atual

    def remover_comeco(self):
        self.__primeira = self.__primeira.proxima
        self.__total_de_elementos = self.__total_de_elementos - 1

    
    def contem(self, elemento):
        atual = self.__primeira
        while atual is not None:
            if atual.elemento == elemento:
                return True
            atual = atual.proxima

        return False

    def tamanho(self):
        return self.__total_de_elementos
    
    def remover_posicao(self, posicao):
        if posicao == 0:
            self.remover_comeco()
        elif posicao == self.__total_de_elementos:
            self.remover_fim
        else:
            anterior = self.pegar(posicao-1)
            anterior.proxima = anterior.proxima.proxima
            self.__total_de_elementos -= 1

    def remover_fim(self): 
        if self.__primeira:
            atual = self.__primeira
            while atual.proxima.proxima:
                atual = atual.proxima
            atual.proxima = None
            self.__total_de_elementos = self.__total_de_elementos - 1

    def remover_elemento(self, elemento):
        indice = self.indice(elemento)
        self.remover_posicao(indice)


    def remover_todos_elementos(self, elemento):
        for _ in range(0, self.__total_de_elementos):
            if self.contem(elemento):
                self.remover_elemento(elemento)

    def __str__(self):
        final_string = '['
        atual = self.__primeira
        
        if self.__total_de_elementos == 0:
            return '[]'
        else:
            for _ in range(0, self.__total_de_elementos -1):
                final_string = final_string + atual.elemento
                final_string = final_string + ', '
                atual = atual.proxima
        
        final_string = final_string + atual.elemento
        final_string = final_string +']'
        return final_string