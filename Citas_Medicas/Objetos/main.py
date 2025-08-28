class usuario:
    def __init__(self, cedula, nombre, correo):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo



class producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.id} - {self.nombre} - ${self.precio}"