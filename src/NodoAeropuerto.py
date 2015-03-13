# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class NodoAeropuerto:
   
    def __init__(self,NombreAeropuerto,Pais,Contrasenia):
        self.NombreAeropuerto=NombreAeropuerto
        self.Pais = Pais
        self.Contrasenia = Contrasenia
        self.Siguiente = None
        self.Anterior = None
        
    def verNodoAeropuerto(self):
        return "Nombre: " + self.NombreAeropuerto + " Password: " + self.Contrasenia+" Pais: "+self.Pais         


