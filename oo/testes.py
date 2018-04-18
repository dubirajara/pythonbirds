from unittest import TestCase

from oo.carro import Motor, Direcao


class CarroTestCase(TestCase):
    def setUp(self):
        self.motor = Motor()
        self.direcao = Direcao()

    def teste_velocidad_inicial(self):
        self.assertEqual(0, self.motor.velocidade)

    def test_acelerar(self):
        self.motor.acelerar()
        self.assertEqual(1, self.motor.velocidade)

    def test_frear(self):
        self.motor.frear()
        self.assertEqual(0, self.motor.velocidade)

    def teste_calcular_direcao(self):
        self.assertEqual('Norte', self.direcao.valor)

    def teste_girar_a_direita(self):
        self.direcao.girar_a_direita()
        self.assertEqual('Leste', self.direcao.valor)

    def teste_girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
        self.assertEqual('Oeste', self.direcao.valor)
