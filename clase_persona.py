from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, nombre, apellidos, id_fiscal):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__id_fiscal = id_fiscal

    @property
    def id_fiscal(self):
        return self.id_fiscal
    
    @id_fiscal.setter
    def id_fiscal(self, id_fiscal):
        self.__id_fiscal = id_fiscal

    @abstractmethod
    def saludar(self):
        pass

class Cliente(Persona):
    numero_clientes = 0

    def __init__(self, nombre, apellidos, id_fiscal, id_cliente, email):
        super().__init__(nombre, apellidos, id_fiscal)
        self.id_cliente = id_cliente
        self.email = email
        Cliente.numero_clientes += 1

    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    def __del__(self):
        print(f"Cliente id: {self.id_cliente} eliminado")

    def __str__(self):
        return f"Cliente [Nombre: {self.nombre} {self.apellidos}, ID fiscal: {self.id_fiscal}, ID Cliente: {self.id_cliente}, email: {self.email}]"
    
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.id_fiscal == other.id_fiscal
        return False
    
    def saludar(self):
        return f"Hola! soy {self.nombre} {self.apellidos}"
