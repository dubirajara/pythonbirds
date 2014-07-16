# -*- coding: utf-8 -*-

from __future__ import unicode_literals

DESTRUIDO = 'Destruido'
ATIVO = 'Ativo'


class Ator():
    _tempo_de_colisao = None
    _caracter_ativo = 'A'
    _caracter_destruido = '✝'

    def caracter(self, tempo):
        if self.status(tempo) == ATIVO:
            return self._caracter_ativo
        else:
            return self._caracter_destruido

    def __init__(self, x=0, y=0):
        self.y = y
        self.x = x

    def status(self, tempo):
        if self._tempo_de_colisao is None or self._tempo_de_colisao > tempo:
            return ATIVO
        return DESTRUIDO

    def calcular_posicao(self, tempo):
        return self.arredondar_posicao()

    def arredondar_posicao(self):
        return round(self.x), round(self.y)

    def colidir(self, outro_ator, tempo):
        if self.status(tempo) == DESTRUIDO or outro_ator.status(tempo) == DESTRUIDO:
            return
        x1, y1 = self.arredondar_posicao()
        x2, y2 = outro_ator.arredondar_posicao()

        def esta_no_intervalo(coordenada1, coordenada2, intervalo=1):
            coordenadas = sorted([coordenada1, coordenada2])
            return coordenadas[1] - intervalo <= coordenadas[0]

        if esta_no_intervalo(x1, x2) and esta_no_intervalo(y1, y2):
            self._tempo_de_colisao = tempo
            outro_ator._tempo_de_colisao = tempo


class Obstaculo(Ator):
    _caracter_ativo = 'O'
    _caracter_destruido = ' '


class Porco(Ator):
    _caracter_ativo = '☺'

class Passaro(Ator):
    _tempo_de_lancamento=None

class PassaroAmarelo(Passaro):
    _caracter_ativo = '>'







