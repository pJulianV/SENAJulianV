
# Clases

# Una clase es un modelo o plantilla a partir de la cual se crean objetos. Define los atributos (propiedades) y métodos (comportamientos) que tendrán los objetos creados a partir de ella.


class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"{self.marca} {self.modelo} está acelerando.")

# Objetos

# Un objeto es una instancia de una clase. Cuando creas un objeto, estás creando una entidad basada en la definición de una clase.

mi_coche = Coche("Toyota", "Corolla")
mi_coche.acelerar()

# Encapsulamiento

# El encapsulamiento es el principio de ocultar los detalles internos de un objeto y exponer solo lo necesario. Esto se logra mediante modificadores de acceso que controlan el acceso a los atributos y métodos.

class Coche:
    def __init__(self, marca, modelo):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo

    def obtener_marca(self):
        return self.__marca

# Métodos

# Los métodos son funciones definidas dentro de una clase que describen los comportamientos que los objetos de esa clase pueden realizar.

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"{self.marca} {self.modelo} está acelerando.")

# Herencia

# La herencia permite crear nuevas clases basadas en clases existentes, heredando sus atributos y métodos. Esto promueve la reutilización de código y facilita la extensión de funcionalidades.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Coche(Vehiculo):
    def acelerar(self):
        print(f"{self.marca} {self.modelo} está acelerando.")
