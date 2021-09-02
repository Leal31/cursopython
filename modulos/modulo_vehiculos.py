class Vehiculo():

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frenar = False

    def arrancar(self):

        self.enmarcha = True
    
    def acelerar(self):
        
        self.acelera = True

    def frenar(self):

        self.frenar = True

    def estado(self):
        print("Marca: ", self.marca)
        print('Modelo: ', self.modelo)
        print('En Marcha: ', self.enmarcha)
        print('Acelerando: ', self.acelera)
        print('Frenando: ', self.frenar)

class Furgoneta(Vehiculo):
    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            return 'La furgoneta esta cargada'
        else:
            return 'La furgoneta no esta cargada'

class Moto(Vehiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):

        self.cargando = True



