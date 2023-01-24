from associacao import Associacao

class MapaEspalhamento:
    def __init__(self) -> None:
        self.__tabela_hash = []
        
        for _ in range (0, 30):
            self.__tabela_hash.append([])
    
        self.__tamanho = 0
    
    def calcula_indice_tabele(self, placa):
        codigo_espalhamento = self.funcao_hash(placa)
        codigo_espalhamento = abs(codigo_espalhamento)
        return codigo_espalhamento % len(self.__tabela_hash)
    
    def funcao_hash(self, placa):
        codigo = 0
        for i in range(0, len(placa)):
            codigo = 7*codigo + ord(placa[i])

        return codigo
    
    def adiciona(self, placa, carro):
        if self.contem_chave(placa):
            self.remove(placa)

        indice = self.calcula_indice_tabele(placa)
        lista = self.__tabela_hash[indice]
        associacao = Associacao(placa, carro)
        lista.append(associacao)

        self.__tamanho += 1
    
    def remove(self, placa):
        if self.contem_chave(placa):     
        
            indice = self.calcula_indice_tabele(placa)
            lista = self.__tabela_hash[indice]

            self.__tabela_hash[indice] = [associacao for associacao in lista if associacao.placa != placa]
            self.__tamanho -= 1
    
    def contem_chave(self, placa):
        indice = self.calcula_indice_tabele(placa)
        lista = self.__tabela_hash[indice]

        for associacao in lista:
            if placa == associacao.placa:
                return True
        return False
    
    def tamanho(self):
        return self.__tamanho

    def pega(self, placa):
        indice = self.calcula_indice_tabele(placa)
        lista = self.__tabela_hash[indice]

        for associacao in lista:
            if associacao.placa == placa:
                return associacao.carro
        raise ValueError('Placa não encontrada')
    
    def __repr__(self) -> str:
        return f'{self.__tabela_hash}'