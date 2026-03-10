class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
    
    def acelerar(self):
        self.velocidade += 10
        print(f"Acelerando")

    def frear(self):
        self.velocidade -= 10
        print("Freando")
    
    def mostrar_velocidade(self):
        print(f"Velocidade de {self.velocidade} KM/h")


fusca = Carro("VW", "Fusca 69", 0)
fusca.mostrar_velocidade()
fusca.acelerar()
fusca.mostrar_velocidade()
fusca.frear()
fusca.mostrar_velocidade()