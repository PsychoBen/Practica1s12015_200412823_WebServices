#-------------------------------------------------------------------------------
# Name:        Arbol AVL Usuarios
# Purpose:
#
# Author:      Ben
#
# Created:     15/03/2015
# Copyright:   (c) Ben 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoUsuario
import NodoVuelo
import NodoAeropuerto
import ListaAeropuerto
import ListaUsuario

class ArbolAvlUsuario:

    def __init__(self):
        self.Raiz=None
        self.cantidad=0
        self.nodito=None
        self.Altur = False

    def getRaiz(self):
        return self.Raiz


    def getNodito(self):
        return self.nodito


    def arbolEstaVacio(self, nodoR):
        return (nodoR==None)


    def setNodito(self,noditor):
        self.nodito=noditor


    ##recibe el nick a buscar y el nodo raiz
    def verificarNick(self, nickname, nodorr):

        Aux=nodorr
        seudonimo=False
        nickname= nickname.upper()
        while Aux!=None:
            userNombre= Aux.NameUsuario
            userNombre= userNombre.upper()
            if nickname==userNombre:
                seudonimo=True
                Aux=None
            else:
                if nickname>userNombre:
                    Aux = Aux.Derecha
                else:
                    Aux = Aux.Izquierda
                    if Aux==None:
                        seudonimo = False
        return seudonimo


    def insertarUsuario(self, Nombre, Contrasenia, NameUsuario, Direccion, Telefono, TarjetaCredito, DireccionActual):

        if (self.verificarNick(NameUsuario,self.Raiz)==False):
            info = NodoUsuario.NodoUsuario(Nombre, Contrasenia, NameUsuario, Direccion, Telefono, TarjetaCredito, DireccionActual)
            self.Raiz = self.insertarBalanceado(self.Raiz,info)
            print "Ingresado con exito!!!"
        else:
            print "Error Nickname repetido"


    def insertarBalanceado(self,nodoRaiz, nodoInsertar):

        N1 = None
        info = nodoInsertar
        if self.arbolEstaVacio(nodoRaiz):
            nodoRaiz = info
            print "Se inserto un nuevo Usuario"
            self.Altur = True
        else:
            if nodoInsertar.NameUsuario < nodoRaiz.NameUsuario:
                nodoRaiz.Izquierda = self.insertarBalanceado(nodoRaiz.Izquierda,nodoInsertar)
                if self.Altur:
                    if nodoRaiz.factorBalance==1:
                        nodoRaiz.factorBalance=0
                        self.Altur = False
                    elif nodoRaiz.factorBalance==0:
                        nodoRaiz.factorBalance=-1
                    ## aca reestructuro porque sino pasaria a valer -2
                    ## y se desequilibra por la izquierda
                    elif nodoRaiz.factorBalance==-1:
                        N1 = nodoRaiz.Izquierda
                        if(N1.factorBalance==-1):
                            nodoRaiz = self.RotacionIzquierdaIzquierda(nodoRaiz,N1)
                        else:
                            nodoRaiz = self.RotacionIzquierdaDerecha(nodoRaiz,N1)
                        self.Altur = False
            else:
                if nodoInsertar.NameUsuario > nodoRaiz.NameUsuario:
                    nodoRaiz.Derecha = self.insertarBalanceado(nodoRaiz.Derecha,nodoInsertar)
                    if self.Altur:
                        if nodoRaiz.factorBalance==-1:
                            nodoRaiz.factorBalance=0
                            self.Altur=False
                        elif nodoRaiz.factorBalance==0:
                            nodoRaiz.factorBalance=1
                        elif nodoRaiz.factorBalance==1:
                            N1 = nodoRaiz.Derecha
                            if N1.factorBalance==1:
                                nodoRaiz = self.RotacionDerechaDerecha(nodoRaiz,N1)
                            else:
                                nodoRaiz = self.RotacionDerechaIzquierda(nodoRaiz,N1)
                            self.Altur=False
                else:
                    print "Error: No pueden haber 2 nickname iguales"
                    self.Altur = False
        return nodoRaiz


    def RotacionIzquierdaIzquierda(self, nodoN, nodoN1):

        nodoN.Izquierda = nodoN1.Derecha
        nodoN1.Derecha = nodoN

        if nodoN1.factorBalance==-1:
            nodoN.factorBalance =0
            nodoN1.factorBalance=0
        else:
            nodoN.factorBalance=-1
            nodoN1.factorBalance=1

        nodoN = nodoN1

        return nodoN


    def RotacionDerechaDerecha(self, nodoN, nodoN1):

        nodoN.Derecha = nodoN1.Izquierda
        nodoN1.Izquierda = nodoN

        if nodoN1.factorBalance==1:
            nodoN.factorBalance =0
            nodoN1.factorBalance=0
        else:
            nodoN.factorBalance=1
            nodoN1.factorBalance=-1

        nodoN = nodoN1

        return nodoN


    def RotacionIzquierdaDerecha(self, nodoN, nodoN1):

        nodoN2 = None
        nodoN2 = nodoN1.Derecha
        nodoN.Izquierda = nodoN2.Derecha
        nodoN2.Derecha = nodoN
        nodoN1.Derecha = nodoN2.Izquierda
        nodoN2.Izquierda = nodoN1

        if nodoN2.factorBalance==1:
            nodoN1.factorBalance=-1
        else:
            nodoN1.factorBalance=0
        if nodoN2.factorBalance==-1:
            nodoN.factorBalance=1
        else:
            nodoN.factorBalance=0

        nodoN2.factorBalance =0
        nodoN=nodoN2

        return nodoN


    def RotacionDerechaIzquierda(self, nodoN, nodoN1):

        nodoN2 = None
        nodoN2 = nodoN1.Izquierda
        nodoN.Derecha = nodoN2.Izquierda
        nodoN2.Izquierda = nodoN
        nodoN1.Izquierda = nodoN2.Derecha
        nodoN2.Derecha = nodoN1

        if nodoN2.factorBalance==1:
            nodoN.factorBalance=-1
        else:
            nodoN.factorBalance=0
        if nodoN2.factorBalance==-1:
            nodoN1.factorBalance=1
        else:
            nodoN1.factorBalance=0

        nodoN2.factorBalance =0
        nodoN=nodoN2

        return nodoN


    def CantidadNodosAvl(self, nodoA):

        cont = 0
        if nodoA==None:
            cont=0
        else:
            cont = cont + 1 + self.CantidadNodosAvl(nodoA.Izquierda) + self.CantidadNodosAvl(nodoA.Derecha)
        return cont


    def AlturaArbol(self, nodoRaiz):
        if nodoRaiz==None:
            return 0
        else:
            return 1 + max(self.AlturaArbol(nodoRaiz.Izquierda),self.AlturaArbol(nodoRaiz.Derecha))


    def PreOrdenAvl(self,Nodo):
        if Nodo==None:
            return
        else:
            ##aca lo puedo meter en un arraylist
            print Nodo.NameUsuario + " \n"
            self.PreOrdenAvl(Nodo.Izquierda)
            self.PreOrdenAvl(Nodo.Derecha)


    def InordenAvl(self, Nodo):
        if Nodo==None:
            return
        else:
            self.InordenAvl(Nodo.Izquierda)
            print Nodo.NameUsuario +" \n"
            ##aca lo puedo meter en un arraylist
            self.InordenAvl(Nodo.Derecha)


    def PostOrdenAvl(self,Nodo):
        if Nodo==None:
            return
        else:
            self.PostOrdenAvl(Nodo.Izquierda)
            self.PostOrdenAvl(Nodo.Derecha)
            print Nodo.NameUsuario +" \n"
            ##aca lo puedo meter a u arraylist


    def LocalizarUsuario(self, nodoRaiz, nickk):
        nickk=nickk.upper()
        nic2 = ""
        nic2 = nodoRaiz.NameUsuario
        nic2 = nic2.upper()
        if nodoRaiz==None:
            return None
        elif nickk==nic2:
            return nodoRaiz
        elif nickk < nic2:
            return self.LocalizarUsuario(nodoRaiz.Izquierda,nickk)
        else:
            return self.LocalizarUsuario(nodoRaiz.Derecha,nickk)


    def Buscar(self, nickBuscado):
        dato =""
        dato = nickBuscado
        if self.Raiz==None:
            return None
        else:
            return self.LocalizarUsuario(self.Raiz,dato)


    def filtrarUsuariosCategoria(self, Nodo, clasi):
        clasi =clasi.upper()
        if Nodo!=None:
            clas = ""
            clas = Nodo.Categoria
            clas=clas.upper()
            if clasi==clas:
                self.setNodito(Nodo);
                self.filtrarUsuariosCategoria(Nodo.Derecha,clasi)
                self.filtrarUsuariosCategoria(Nodo.Izquierda, clasi)

            else:
                self.filtrarUsuariosCategoria(Nodo.Derecha,clasi)
                self.filtrarUsuariosCategoria(Nodo.Izquierda,clasi)


    def verContactos(self, tipoUsuario):
        while(self.getNodito()!=None):
            self.filtrarUsuariosCategoria(self.getRaiz(),tipoUsuario)
            print "Este nodo esta en esa categoria "+ self.getNodito.verNodoUsuario


    def eliminarContacto(self, nickEliminar):
        nickEliminar= nickEliminar.upper()
        valor = nickEliminar
        flag = True
        ##raiz = self.borrarAvl(self.Raiz,valor,flag)
        self.Raiz = self.borrarAvl(self.Raiz,valor,flag)


    def borrarAvl(self, nodoR, clave, cambiarAltura):
        cla =""
        cla = nodoR.NameUsuario
        cla=cla.upper()
        clave=clave.upper()
        if nodoR==None:
            print "Nodo no encontrado"
        elif clave < cla:
            izq = self.borrarAvl(nodoR.Izquierda, clave, cambiarAltura)
            nodoR.Izquierda = izq
            if cambiarAltura:
                nodoR = self.Equilibrar1(nodoR, cambiarAltura)

        elif clave > cla:
            dere = self.borrarAvl(nodoR.Derecha,clave,cambiarAltura)
            nodoR.Derecha = dere
            if cambiarAltura:
                nodoR = self.Equilibrar2(nodoR,cambiarAltura)
        else: ##nodo encontrado
            nodoQ = nodoR
            if nodoQ.Izquierda==None: ##solo tiene rama derecha
                nodoR=nodoQ.Derecha
                cambiarAltura = False
            elif nodoQ.Derecha==None: ##solo tiene rama izquierda
                nodoR = nodoQ.Izquierda
                cambiarAltura = False
            else: ##si tiene rama izquierda y derecha
                iz = self.Reemplazar(nodoR,nodoR.Izquierda,cambiarAltura)
                nodoR.Izquierda = iz
                if cambiarAltura:
                    nodoR = self.Equilibrar1(nodoR,cambiarAltura)
            nodoQ = None
        return nodoR


    def Reemplazar(self, N, actual, cambiarAltur):
        if actual.Derecha!=None:
            de = self.Reemplazar(N,Actual.Derecha,cambiarAltur)
            actual.Derecha = de
            if cambiarAltur:
                actual = self.Equilibrar2(actual,cambiarAltur)
        else:
            N.NameUsuario = actual.NameUsuario
            N = actual
            actual = actual.Izquierda
            N = None
            cambiarAltur =False
        return actual


    def Equilibrar1(self, N, cambiaAlturr):

        N1 = None
        if N.factorBalance==-1:
            N.factorBalance=0

        elif N.factorBalance==0:
            N.factorBalance =1
            cambiaAlturr=False

        elif N.factorBalance==1:
            N1 = N.Derecha
            if N1.factorBalance>=0:
                if N1.factorBalance==0:
                    cambiaAlturr=True
                N = self.RotacionDerechaDerecha(N,N1)
            else:
                N = self.RotacionDerechaIzquierda(N,N1)
        return N


    def Equilibrar2(self, N,cambioAlturrr):
        N1=None
        if N.factorBalance ==-1:
            N1 = N.Izquierda
            if N1.factorBalance<=0:
                if N1.factorBalance==0:
                    cambioAlturrr=False
                N=self.RotacionIzquierdaIzquierda(N,N1)
            else:
                N=self.RotacionIzquierdaDerecha(N,N1)
        elif N.factorBalance==0:
            N.factorBalance=-1
            cambioAlturrr=True
        elif N.factorBalance==1:
            N.factorBalance=0
        return N


    def loguearUsuario(self, nickn, clavee):
        seEncontro=False
        datoss = nickn
        if self.Raiz==None:
            seEncontro=False
        else:
            nodoooo = self.LocalizarUsuarioLoguear(self.Raiz,datoss,clavee)
            if nodoooo==None:
               seEncontro=False
            else:
                seEncontro=True
        if seEncontro==False:
            print "No se pudo loguear con los datos nickname: "+ nickn +" Password:" +clavee
        else:
            print "Felicidades se a podido loguear con user: "+nickn + " y Password: " + clavee

        return seEncontro


    def LocalizarUsuarioLoguear(self, nodoRaiz, nickk, claveee):

        if nodoRaiz==None:
            return None
        else:
            nic2 = nodoRaiz.NameUsuario
            codd = nodoRaiz.Contrasenia
        if nodoRaiz==None:
            return None
        elif nickk==nic2 and claveee==codd:
            print "*************************************************************************************"
            print "*************Felicidades aca se comprobo el nickname y la clave**********************"
            print "**** Te logueaste con NickName:  "+nickk+"  y Password: "+claveee +"  ***************"
            print "*************************************************************************************"
            return nodoRaiz
        elif nickk < nic2:
            return self.LocalizarUsuarioLoguear(nodoRaiz.Izquierda,nickk,claveee)
        else:
            return self.LocalizarUsuarioLoguear(nodoRaiz.Derecha,nickk,claveee)

