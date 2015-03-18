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
import ListaUsuario
import NodoUsuario
import NodoVuelo
import NodoUsuario
import ListaAeropuerto
import ListaUsuario
import ArbolAvlUsuario
import ArbolAvlVuelos

class NodoVuelo:

    def __init__(self, IdUnico, LugarLlegada, HoraSalida, FechaSalida, HoraLlegada, FechaLlegada, CantPrimeraClase, CostoPrimeraClase, CantTurista, CostoTurista, CantEjecutiva, CostoEjecutiva, EstadoVuelo):

        self.IdUnico = IdUnico
        self.LugarLlegada =LugarLlegada
        self.HoraSalida = HoraSalida
        self.FechaSalida = FechaSalida
        self.HoraLlegada = HoraLlegada
        self.FechaLlegada = FechaLlegada
        self.CantPrimeraClase = CantPrimeraClase
        self.CostoPrimeraClase = CostoPrimeraClase
        self.CantTurista = CantTurista
        self.CostoTurista = CostoTurista
        self.CantEjecutiva = CantEjecutiva
        self.CostoEjecutiva = CostoEjecutiva
        self.factorBalance=0
        self.EstadoVuelo = EstadoVuelo
        self.ListaUsuariosVuelo=ListaUsuario.ListaUsuario()
        self.Siguiente=None
        self.Anterior=None
        self.Izquierda = None
        self.Derecha = None

    def VerNodoVuelo(self):
        ##return " Id Unico: "+ str(self.IdUnico)+" Llegada: " + self.LugarLlegada +" Estado: " + self.EstadoVuelo
        return {"LugarSalida": self.LugarSalida, "IdUnico": unicode(self.IdUnico), "EstadoVuelo": self.EstadoVuelo, "LugarLlega": self.LugarLlegada}