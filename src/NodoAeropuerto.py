#-------------------------------------------------------------------------------
# Name:        Nodo Aeropuerto
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

class NodoAeropuerto:

    def __init__(self,NombreAeropuerto,Pais,Contrasenia):
        self.NombreAeropuerto=NombreAeropuerto
        self.Pais = Pais
        self.Contrasenia = Contrasenia
        self.miArbolAvlVuelos = ArbolAvlVuelos.ArbolAvlVuelos()
        self.Siguiente = None
        self.Anterior = None

    def verNodoAeropuerto(self):
        ##return "Nombre: " + self.NombreAeropuerto + " Password: " + self.Contrasenia+" Pais: "+self.Pais
        return {"NombreAeropuerto": self.NombreAeropuerto, "Pais": self.Pais, "Contrasenia": self.Contrasenia}