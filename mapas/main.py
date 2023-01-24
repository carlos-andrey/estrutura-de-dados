from mapa_espalhamento import MapaEspalhamento
from carro import Carro

mapa = MapaEspalhamento()
carro1 = Carro('Corola', 'Toyats', 'Vermelho', 2012)
carro2 = Carro('DMC DeLorean', 'DeLorean', 'Prata', 2030)


mapa.adiciona('XLR8', carro1)
mapa.adiciona('HTML5', carro2)

print(mapa.pega('XLR8'))

mapa.remove('XLR8')

print(mapa.contem_chave('XLR8'))

print(mapa.tamanho())