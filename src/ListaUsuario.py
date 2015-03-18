#-------------------------------------------------------------------------------
# Name:        Lista doble Usuarios
# Purpose:
#
# Author:      Ben
#
# Created:     15/03/2015
# Copyright:   (c) Ben 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoUsuario

class ListaUsuario:

    def __init__(self):
        self.inicio = None
        self.fin = None
        self.longitud = 0


    def estaVacia(self):
        if self.inicio==None:
            return True
        else:
             return False

    def insertarInicio(self, nombre,contrasenia,nameusuario,direcion,telefono,tarjetacredito,direccionactual):
        nuevo = NodoUsuario.NodoUsuario(nombre,contrasenia,nameusuario,direcion,telefono,tarjetacredito,direccionactual)
        if self.estaVacia()==True:
            self.inicio = nuevo
            self.fin = nuevo
            self.longitud = self.longitud + 1
        else:
            nuevo.Siguiente = self.inicio
            self.inicio.Anterior = nuevo
            self.inicio= nuevo
            self.longitud = self.longitud + 1


    def insertarFinal(self, nuevo):
        if self.estaVacia()==True:
            self.inicio=nuevo
            self.fin=nuevo
            self.longitud=self.longitud +1
        else :
            nuevo.Anterior=self.fin
            self.fin.Siguiente=nuevo
            self.fin=nuevo
            self.longitud=self.longitud +1


    def mostrarListadoUsuario(self):

        print("***************")
        aux = self.inicio
        while aux!=None:
            print(aux.verNodoUsuario()+" ")
            aux = aux.Siguiente


    def mostrarListadoAeropuertoAtras(self):
        print("***************")
        aux = self.fin
        while aux!=None:
            print(aux.verNodoUsuario()+" ")
            aux = aux.Anterior


    def borrarInicio(self):
        if self.estaVacia()==False:
            self.inicio = self.inicio.Siguiente
            self.inicio.Anterior=None


    def borrarFinal(self):
        if self.fin.Anterior==None:
            self.inicio=None
            self.fin=None
        else:
            self.fin = self.fin.Anterior
            self.fin.Siguiente=None


    def buscarUsuario(self, nomm):
        encontrado=None
        auxxx = self.inicio
        nomm=nomm.upper()
        while auxxx!=None:
            nomm1 = auxxx.NameUsuario
            nomm1=nomm1.upper()
            if nomm1==nomm:
                encontrado=auxxx
                break
            else :
                auxxx=auxxx.Siguiente
        if encontrado==None:
            print "No se encontro el Usuario"
        return encontrado


    def eliminarUsuario(self,naa):
        userEliminar = self.buscarUsuario(naa)
        if userEliminar!=None:
            anterr = userEliminar.Anterior
            poster=userEliminar.Siguiente
            anterr.Siguiente=poster
            if poster!=None:
                poster.Anterior = anterr

            self.longitud=self.longitud - 1
        else:
            print("No se pudo borrar")