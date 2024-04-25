class BombaDeCombustivel:
    def __init__(self,tipoDeCombustível,valorLitro,quantidadeCombustivel):
        self.__tipoDeCombustivel=tipoDeCombustível
        self.__valorLitro=valorLitro
        self.__quantidadeCombustivel=quantidadeCombustivel

    def AbastecerPorValor(self, valorAAbastecer):
        self.valorAAbastecer=valorAAbastecer
        quantidadeAbastecida = self.valorAAbastecer/self.__valorLitro
        self.__quantidadeCombustivel-=quantidadeAbastecida
        print(f'Quantidade a abastecer: ',(quantidadeAbastecida),'LITROS')

    def AbastecerPorLitro(self, quantidadeAAbastecer):
        self.quantidadeaAbastecer=quantidadeAAbastecer
        valorAPagar = self.quantidadeaAbastecer*self.__valorLitro
        self.__quantidadeCombustivel-=quantidadeAAbastecer
        print(f'Valor a pagar: ',(valorAPagar),'REAIS')

    def AlterarValor(self,novoValor):
        if novoValor:
            self.__valorLitro = novoValor

    def AlterarCombustivel(self,novoCombustivel):
        if novoCombustivel:
            self.__tipoDeCombustivel=novoCombustivel

    def AlterarQuantidadeDeCombustivel(self,novaQuantidadeCombustivel):
        if novaQuantidadeCombustivel:
            self.__quantidadeCombustivel=novaQuantidadeCombustivel

    def get_info_bomba(self):
        print('-------------------------------')
        print(' INFORMAÇÕES BOMBA COMBUSTÍVEL')
        print(self.__tipoDeCombustivel)
        print (self.__valorLitro,f'REAIS')
        print((self.__quantidadeCombustivel),f'LITROS')
        print('-------------------------------')
        
        


B1=BombaDeCombustivel('Gasolina',6.5,30)
B1.get_info_bomba()
B1.AlterarCombustivel('Alcool')
B1.AlterarValor(4.5)
B1.AlterarQuantidadeDeCombustivel(1000)
B1.get_info_bomba()
B1.AbastecerPorLitro(45)
B1.get_info_bomba()
B1.AbastecerPorValor(200)
B1.get_info_bomba()

