class Pessoa:
    olhos = 2

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
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(renzo.olhos)
    print(luciano.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))