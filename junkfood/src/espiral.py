class Espiral:
    def __init__(self):
        self.nome = " - "
        self.quantidade_espiral = 0
        self.preco = 0

    def getNomeDoProduto(self):
        return self.nome

    def getQuantidade(self):
        return self.quantidade_espiral

    def getPreco(self):
        return self.preco

    def setNomeDoProduto(self, nome):
        self.nome = nome
        return self.nome

    def setPreco(self, valor):
        self.preco = valor
        return self.preco

    def setQuantidade(self, numero):
        self.quantidade_espiral = numero
        return self.quantidade_espiral