from vetor import Vetor
from aluno import Aluno

a1 = Aluno("Francisco")
a2 = Aluno('Angelyne')
a3 = Aluno('Junior')
a4 = Aluno('Pedro')
a5 = Aluno('Adamastor')

v1 = Vetor()

v1.adicionar(a1)
v1.adicionar(a2)
v1.adicionar(a3)
v1.adicionar(a4)
v1.adicionar(a5)
print(v1)

v1.adicionar_posicao(a3, 0)
v1.adicionar_posicao(a3, 2)
v1.adicionar_posicao(a3, 3)
print(v1)

print(v1.pegar(4))
print(v1.pegar(90))

v1.remover_ultimo_elemento()
print(v1)

v1.remover_elemento(a3)
print(v1)

v1.remover_posicao(2)
print(v1)

v1.remover_todos_elementos(a3)
print(v1)

print(v1.contem(a1))
print(v1.contem(a4))

print(v1.tamanho())
