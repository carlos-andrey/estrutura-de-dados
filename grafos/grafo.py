class Grafo:
    def __init__(self, vertices) -> None:
        self.__vertices = vertices
        self.__grafo = [[0] * self.__vertices for _ in range(self.__vertices)]
        
    def imprime(self) -> str:
        for i in self.__grafo:
            for j in i:
                print(j, end ='  ')
            print('')
            
    def adiciona_aresta(self, x, y):
        self.__grafo[x-1][y-1] = 1
        self.__grafo[y-1][x-1] = 1
    
    def tem_ligacao(self, x, y):
        if self.__grafo[x - 1][y - 1] == 1:
            return True
        return False
