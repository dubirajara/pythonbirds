class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Hello {self.nome}'


if __name__ == '__main__':
    joselito = Pessoa(nome='Jose')
    dalia = Pessoa(nome='Dalia')
    diego = Pessoa(joselito, dalia, nome='Diego')
    print(diego.cumprimentar())
    print(diego.nome, diego.idade)
    for filho in diego.filhos:
        print(filho.nome)
