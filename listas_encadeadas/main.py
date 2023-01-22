from lista_encadeada import ListaEncadeada

l1 = ListaEncadeada()

l1.adicionar_comeco('Junior')
l1.adicionar_comeco('Pedro')
l1.adicionar_comeco('Francisco')
l1.adicionar_comeco('Junior')
l1.adicionar_comeco('Junior')
l1.adicionar_comeco('Junior')
print(l1)

l1.adicionar_fim('Felipe')
print(l1)

l1.adicionar_posicao(2, 'Antonio')
print(l1)

print(l1.contem('Pedro'))

print(l1.pegar(3))

l1.remover_comeco()
print(l1)

l1.remover_fim()
print(l1)

l1.remover_posicao(2)
print(l1)

l1.remover_elemento('Junior')
print(l1)

l1.adicionar_comeco('Junior')
l1.adicionar_posicao(3, 'Junior')
print(l1)
l1.remover_todos_elementos('Junior')
print(l1)
