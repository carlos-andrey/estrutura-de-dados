class Vetor:

    def __init__(self):
        self.__alunos = [None]*100
        self.__total_de_alunos = 0
        self.__fim_do_vetor = len(self.__alunos)

    def adicionar(self, aluno):
        self.__alunos[self.__total_de_alunos] = aluno
        self.__total_de_alunos = self.__total_de_alunos + 1

    def adicionar_posicao(self, aluno, posicao):
        self.__alunos.insert(posicao, aluno)
        self.__alunos.pop(self.__fim_do_vetor)
        self.__total_de_alunos = self.__total_de_alunos+1

    def pegar(self, posicao):
        if posicao >= self.__total_de_alunos:
            return 'ERROR[POSIÇÃO INVALIDA]'
        return self.__alunos[posicao]

    def remover_ultimo_elemento(self):
        self.__alunos.pop(self.__total_de_alunos - 1)
        self.__alunos.append(None)
        self.__total_de_alunos = self.__total_de_alunos-1

    def contem(self, nome):
        for index in range(0, self.__total_de_alunos):
            if self.__alunos[index] == nome:
                return True              
        return False

    def tamanho(self):
        return self.__total_de_alunos
    
    def remover_posicao(self, posicao):
        self.__alunos.pop(posicao)
        self.__alunos.append(None)
        self.__total_de_alunos = self.__total_de_alunos-1

    def remover_elemento(self, aluno):
        self.__alunos.remove(aluno)
        self.__total_de_alunos = self.__total_de_alunos-1
    
    def remover_todos_elementos(self, aluno):
        for _ in range(0,self.__total_de_alunos):
            if self.contem(aluno):
                self.remover_elemento(aluno)


    def __str__(self) -> str:
        ret = []
        for i in range(0, self.__total_de_alunos):
            ret.append(str(self.__alunos[i]))

        return f'{ret}'