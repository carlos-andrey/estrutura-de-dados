from pilha import Pilha

pilha = Pilha()
pilha.insere('francesco virgolini')
pilha.insere(3)
pilha.insere(3.14)
print(pilha)

pilha.remove()
print(pilha)

print(pilha.vazia())

pilha.remove()
pilha.remove()
print(pilha.vazia())