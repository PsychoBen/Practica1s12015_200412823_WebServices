# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class NodoUsuario:
    
    def __init__(self, Nombre, Contrasenia, NameUsuario, Direccion, Telefono, TarjetaCredito, DireccionActual):
      self.Nombre = Nombre
      self.Contrasenia = Contrasenia
      self.NameUsuario = NameUsuario
      self.Direccion = Direccion
      self.Telefono = Telefono
      self.TarjetaCredito = TarejetaCredito
      self.DireccionActual = DireccionActual
      self.Izquierda = None
      self.Derecha = None

    def verNodoUsuario(self):
        return "Usuario: " +self.NameUsuario + " Password: " + self.Contrasenia
    
     
    
    
                    
