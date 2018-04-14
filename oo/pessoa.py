class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Hello {self.nome}'


if __name__ == '__main__':
    p = Pessoa('Diego')
    print(p.cumprimentar())
    print(p.nome, p.idade)
