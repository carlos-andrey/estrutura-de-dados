from celula import Celula

class Arvore:
    def __init__(self):
        self.__raiz = None
    
    @property
    def raiz(self):
        return self.__raiz
    
    def vazia(self):
        if self.raiz is None:
            return True
        return False
    
    def maximo(self,  celula = None):
        if celula == None:
            celula = self.__raiz
        while celula.direita:
            celula = celula.direita
        return celula.label

    def minimo(self, celula = None):
        if celula == None:
            celula = self.__raiz
        while celula.esquerda:
            celula = celula.esquerda
        return celula.label
    
    def insere(self, label):
        nova_celula = Celula(label)
        if self.vazia():
            self.__raiz = nova_celula
        else:
            atual = self.__raiz
            pai = None
            while True:
                if atual is not None:
                    pai = atual
                    if nova_celula.label < atual.label:
                        atual = atual.esquerda
                    else:
                        atual = atual.direita
                else:
                    if nova_celula.label < pai.label:
                        pai.esquerda = nova_celula
                    else:
                        pai.direita = nova_celula
                    break
    
    def remove(self, valor, label = None):
        if label == None:
            label = self.__raiz 
        if valor < label.label:
            label.esquerda = self.remove(valor, label.esquerda)
        elif valor > label.label:
            label.direita = self.remove(valor, label.direita)
        else:
            if label.esquerda == None:
                return label.direita
            elif label.direita == None:
                return label.esquerda
            else:
                novo_valor = self.minimo(label.direita)
                label.label = novo_valor
                label.direita = self.remove(novo_valor, label.direita)
        
        return label
        
    def imprimir_pre_ordem(self, atual):
        if atual is not None:
            print(atual.label)
            self.imprimir_pre_ordem(atual.esquerda)
            self.imprimir_pre_ordem(atual.direita)
        
    def imprimir_pos_ordem(self, atual):
        if atual is not None:
            self.imprimir_pos_ordem(atual.esquerda)
            self.imprimir_pos_ordem(atual.direita)
            print(atual.label)
            

    def imprimir_intra_ordem(self, atual):
        if atual is not None:
            self.imprimir_intra_ordem(atual.esquerda)
            print(atual.label)
            self.imprimir_intra_ordem(atual.direita)
