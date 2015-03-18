#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ben
#
# Created:     15/03/2015
# Copyright:   (c) Ben 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoVuelo
import NodoUsuario
import ListaAeropuerto
import ListaUsuario
import ArbolAvlUsuario
import ArbolAvlVuelos

class NodoUsuario:

    def __init__(self, Nombre, Contrasenia, NameUsuario, Direccion, Telefono, TarjetaCredito, DireccionActual):
      self.Nombre = Nombre
      self.Contrasenia = Contrasenia
      self.NameUsuario = NameUsuario
      self.Direccion = Direccion
      self.Telefono = Telefono
      self.Categoria="prueba"
      self.TarjetaCredito = TarjetaCredito
      self.DireccionActual = DireccionActual
      self.factorBalance=0
      self.Siguiente=None
      self.Anterior=None
      self.Izquierda = None
      self.Derecha = None

    def verNodoUsuario(self):
        ##return "Usuario: " +self.NameUsuario + " Password: " + str(self.Contrasenia)
        return {"NameUsuario": self.NameUsuario, "Contrasenia": str(self.Contrasenia), "Direccion": self.Direccion, "DireccionActual": self.DireccionActual}