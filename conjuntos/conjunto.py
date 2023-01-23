class Conjunto:
    def __init__(self):
        self.__tabela = []
        self.__tamanho = 0
        for _ in range(0, 26):
            self.__tabela.append([])

    def calcula_indice(self, elemento):
       codigo_espalhamento = self.calcula_codigo_espalhamento(elemento)
       codigo_espalhamento = abs(codigo_espalhamento)
       return codigo_espalhamento % len(self.__tabela)

    def calcula_codigo_espalhamento(self, elemento):
        codigo = 1

        for i in range(0, len(elemento)):
            codigo = 42 * codigo + ord(elemento[i])
        return codigo

    def verificar_carga(self):
        capacidade = len(self.__tabela)
        carga = self.__tamanho / capacidade

        if carga > 0.75:
            self.redimencionar_tabela(capacidade * 2)
        elif carga < 0.25:
            self.redimencionar_tabela(max(capacidade // 2, 10))

    def redimencionar_tabela(self, nova_capacidade):
        elementos = self.pegar_todos()
        self.__tabela = []
        self.__tamanho = 0

        for _ in range(0, nova_capacidade + 1):
            self.__tabela.append([])
        
        for elemento in elementos:
            self.adicionar(elemento)

    def adicionar(self, elemento):
        self.verificar_carga()
        if not self.contem(elemento):
            indice = self.calcula_indice(elemento)
            lista = self.__tabela[indice]
            lista.append(elemento)
            self.__tamanho += 1

    def remover(self, elemento):
        if self.contem(elemento):
            indice = self.calcula_indice(elemento)
            lista = self.__tabela[indice]
            lista.remove(elemento)
            self.__tamanho -=1
            self.verificar_carga()

    def contem(self, elemento):
        indice = self.calcula_indice(elemento)
        lista = self.__tabela[indice]
        return elemento in lista

    def pegar_todos(self):
        elementos = []
        for i in range(0, len(self.__tabela)):
            elementos = elementos + self.__tabela[i]
        return elementos
    
    def tamanho(self):
        return self.__tamanho
    
    def __repr__(self) -> str:
        return f'{self.__tabela}'
