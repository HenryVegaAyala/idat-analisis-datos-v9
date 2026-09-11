class Clientes:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def comprar(self, monto):
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
            print(f"{self.nombre} ha comprado un producto de "
                  f"${monto} y su saldo actual es ${self.saldo}")
        else:
            print(f"{self.nombre} no tiene suficiente saldo para comprar "
                  f"un producto de ${monto}. Su saldo actual es ${self.saldo}")

    def mostrar_saldo(self):
        print(f"Nombre: {self.nombre}, Saldo: ${self.saldo}")

cliente = Clientes("Juan", 1500)
cliente.comprar(500) # Comprando una mochila de $500
cliente.comprar(300) # Comprando un cuaderno de $300
cliente.mostrar_saldo()
cliente.comprar(800) # Intentando comprar un producto de $800