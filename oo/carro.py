"""
Criar uma clase carro com dois atributos composto por outras duas classe.

1 - Motor
2 - Direcao

1 - Motor tera a responsabilidade de controlar a velocidade.
ele oferece os seguintes atributos:
    1- atributo de dato velocidade
    2 - Metodo acelerar que devera imcrementar a velocidade de uma unidade
    3 - metodo frear que deverar decrementar a velocidad em duas unidades, obs nao pode baixar de zero.

2 - Direçao tera a responsabilidade de controlar a direçao, ela oferece os seguintes atributos:
    1 - Valor de direçao com os valores possiveis: Norte, Sul, Leste, Oeste
    2 - Metodo girar_a_direita
    3 - Metodo girar_a_esquerda

        N
      O   L
        S

Exemplo:
    # Testando Motor
    >>> motor = Motor()
    >>> motor = velocidad
    0
    >>> motor.acelerar()
    >>> motor = velocidad
    1
    >>> motor.acelerar()
    >>> motor = velocidad
    2
    >>> motor.acelerar()
    >>> motor = velocidad
    3
    >>> motor.frear()
    >>> motor = velocidad
    1
    >>> motor.frear()
    >>> motor = velocidad
    0

    # Testando Direçao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidad()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidad()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidad()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidad()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'

"""