class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar (self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

p1 = Pessoa("Maria", 25)
p1.apresentar()

p2 = Pessoa("Joao", 19)
p2.apresentar()

SELECT *
  FROM NOTAFISCAL
 WHERE NUMNOTAFISCAL = :pNOTAFISCAL





class Veiculo:
    def __init__(self, modelo, ano, cor, carburador):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.carburador = carburador

    def acelerar(self):
        print("Vrum vrum 250km/h")

    def exibirInfoCarro(self):
        print(f"Modelo: {self.modelo} / Ano: {self.ano} / Cor: {self.cor} / Carburador: {self.carburador}")
    

fusca = Veiculo("quadrado", 64, "azul", "fudeu")
fusca.acelerar()
fusca.exibirInfoCarro()



class NotaFiscal
    def __init__(self, modelo, serie, numnota, chavenf):
        self.modelo = modelo
        self.ano = serie
        self.cor = numnota
        self.carburador = chavenf


    def insert

    def delete

    def update

    def select(numNota)
        string Select = "SELECT * FROM DUAL WHERE NUMNOTA = :pNUMNOTA"
    def select()
    

nf = NotaFiscal(modelo, serie, numnota, chavenf)
nf.select()

