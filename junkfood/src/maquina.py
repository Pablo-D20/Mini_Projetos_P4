from src.espiral import Espiral

class Maquina:

    def __init__(self, qtdEspirais: int, maximoProdutos: int):
        self.qtdEspirais = qtdEspirais
        self.MaximoProdutos = maximoProdutos
        self.faturamento = 0
        self.saldo_cliente = 0
        self.espiral = []
        for i in range(qtdEspirais):
            self.espiral.append(Espiral())

    def getFaturamento(self) -> float:
        return self.faturamento

    def getMaximoProdutos(self) -> int:
        return self.MaximoProdutos

    def getSaldoCliente(self) -> float:
        return self.saldo_cliente

    def getSizeEspirais(self) -> int:
        return self.qtdEspirais


    def getEspiral(self, indice: int) -> Espiral:
        if 0 <= indice < self.qtdEspirais:
            return self.espiral[indice]
        else:
            print("error")
            return None


    def inserirDinheiro(self, value: float) -> bool:
        if value > 0:
            self.saldo_cliente += value
            return True
        else:
            return False

    def receberTroco(self) -> float:
        troco = self.saldo_cliente
        self.saldo_cliente = 0
        return troco

    def alterarEspiral(self, indice: int, nome: str, quantidade: int, preco: float) -> bool:
        if self.getEspiral(indice):
            espiral = self.getEspiral(indice)
            if self.MaximoProdutos >= quantidade >= 0 and preco >= 0:
                espiral.setNomeDoProduto(nome)
                espiral.setQuantidade(quantidade)
                espiral.setPreco(preco)
                return True
        return False

    def limparEspiral(self, indice: int) -> bool:
        if self.getEspiral(indice):
            self.alterarEspiral(indice, ' - ', 0, 0)
            return True
        return False

    def vender(self, indice: int) -> bool:
        if self.getEspiral(indice):
            espiral = self.getEspiral(indice)
            if self.saldo_cliente >= espiral.getPreco():
                if espiral.getQuantidade() > 0:
                    espiral.quantidade_espiral -= 1
                    self.faturamento += espiral.getPreco()
                    self.saldo_cliente -= espiral.getPreco()
                    if espiral.getQuantidade() == 0:
                        self.limparEspiral(indice)
                    return True
        return False



