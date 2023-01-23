from conjunto import Conjunto

conjunto = Conjunto()

conjunto.adicionar('Maçã')
conjunto.adicionar('Abacaxi')
conjunto.adicionar('banana')
conjunto.adicionar('Maçã')
conjunto.adicionar('carambola')
conjunto.adicionar('damasco')
conjunto.adicionar('Maçã')
print(conjunto.pegar_todos())

conjunto.remover('Maçã')
print(conjunto.pegar_todos())

