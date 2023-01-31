from grafo import Grafo

g1 = Grafo(5)
g1.adiciona_aresta(2,1)
g1.adiciona_aresta(3,1)

g1.imprime()

print(g1.tem_ligacao(4, 3))
print(g1.tem_ligacao(1, 2))
print(g1.tem_ligacao(2, 1))