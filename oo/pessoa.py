class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Hello {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_clase(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homen(Pessoa):
    pass

if __name__ == '__main__':
    joselito = Pessoa(nome='Jose')
    renzo = Homen(nome='Renzo')
    luciano = Homen(joselito, renzo, nome='Luciano')
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
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_clase(), luciano.nome_e_atributos_de_clase())
    pessoa = Homen('Anonimo')
    print(isinstance(pessoa, Pessoa))