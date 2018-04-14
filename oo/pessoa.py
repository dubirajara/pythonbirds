class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Hello {self.nome}'


if __name__ == '__main__':
    joselito = Pessoa(nome='Jose')
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(joselito, renzo, nome='Luciano')
    print(luciano.cumprimentar())
    print(luciano.nome, luciano.idade, luciano.filhos)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)