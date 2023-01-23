from fila import Fila

fila = Fila()

fila.adiciona('Angeline')
fila.adiciona('Zé')
fila.adiciona(10)
fila.adiciona(3.14)
print(fila)

fila.remove()
print(fila)

fila.remove()
fila.remove()
fila.remove()
print(fila)
print(fila.vazia())