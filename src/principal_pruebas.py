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

import copy
import ListaAeropuerto
import NodoAeropuerto
import NodoUsuario
import ListaUsuario
import NodoVuelo
import ArbolAvlUsuario
import ArbolAvlVuelos

def main():
##    nodo1=NodoAeropuerto.NodoAeropuerto("aurora","guate","1234566789")
##    print nodo1.verNodoAeropuerto()+"nuevo \n"
##    nodo2=NodoAeropuerto.NodoAeropuerto("salvador","salvador","1234566789")
##    print nodo2.verNodoAeropuerto()+"nuevo \n"
##    nodo3=NodoAeropuerto.NodoAeropuerto("nica","nica","1234566789")
##    print nodo3.verNodoAeropuerto()+"nuevo \n"
##    nodo4=NodoAeropuerto.NodoAeropuerto("hondur","hondura","1234566789")
##    print nodo4.verNodoAeropuerto()+"nuevo \n"
##    nodo5=NodoAeropuerto.NodoAeropuerto("ticas","ticas","1234566789")
##    print nodo5.verNodoAeropuerto()+"nuevo \n"
##    lista = ListaAeropuerto.ListaAeropuerto()
##    lista.insertarFinal(nodo1)
##    lista.insertarFinal(nodo2)
##    lista.insertarFinal(nodo3)
##    lista.insertarFinal(nodo4)
##    lista.insertarFinal(nodo5)
##    lista.mostrarListadoAeropuerto()
##    lista.eliminarAeropuerto("salvador")
##    lista.loguearAeropuerto("hondur","1234566789")
##    lista.loguearAeropuerto("aurora","1234566788")
##    lista.mostrarListadoAeropuertoAtras()
##    buscado=lista.buscarAeropuerto("ticas")
  ##  print "Este nodo es el buscado "+buscado.verNodoAeropuerto()

##  nodo1= NodoUsuario.NodoUsuario("u1","1234567","psycho1","guate","1234567890",82739462939,"jutiapa")
##  nodo2= NodoUsuario.NodoUsuario("u2","1234567","psycho2","guate","1234567890",82739462939,"jutiapa")
##  nodo3= NodoUsuario.NodoUsuario("u3","1234567","psycho3","guate","1234567890",82739462939,"jutiapa")
##  nodo4= NodoUsuario.NodoUsuario("u4","1234567","psycho4","guate","1234567890",82739462939,"jutiapa")
##  nodo5= NodoUsuario.NodoUsuario("u5","1234567","psycho5","guate","1234567890",82739462939,"jutiapa")
##  listaUser=ListaUsuario.ListaUsuario()
##  listaUser.insertarFinal(nodo1)
##  listaUser.insertarFinal(nodo2)
##  listaUser.insertarFinal(nodo3)
##  listaUser.insertarFinal(nodo4)
##  listaUser.insertarFinal(nodo5)
##  listaUser.mostrarListadoUsuario
##  listaUser.mostrarListadoAeropuertoAtras()
##  listaUser.eliminarUsuario("psycho3")
##  listaUser.mostrarListadoUsuario
##  listaUser.mostrarListadoAeropuertoAtras()
##  userBuscado= listaUser.buscarUsuario("psycho2")
##  print "El usuario buscado es: "+ userBuscado.verNodoUsuario()

##  miArbolUsuario = ArbolAvlUsuario.ArbolAvlUsuario()
##  miArbolUsuario.insertarUsuario("Pepito","12345678","rata","guate",22222222,8967543201,"Jutiapa")
##  miArbolUsuario.insertarUsuario("Pepito","12345678","ratas","guate",22222222,8967543201,"Jutiapa")
##  miArbolUsuario.insertarUsuario("Pepito","12345678","ratia","guate",22222222,8967543201,"Jutiapa")
##  miArbolUsuario.insertarUsuario("Pepito","12345678","ratAn","guate",22222222,8967543201,"Jutiapa")
##  miArbolUsuario.insertarUsuario("Pepito","12345678","rato","guate",22222222,8967543201,"Jutiapa")
##  miArbolUsuario.insertarUsuario("Pepito","7777rttRr77777paprplWffrw","rataT","guate",22222222,8967543201,"Jutiapa")
##  nodoUser= miArbolUsuario.Buscar("RATO")
##  print "**********************************"
##  print "*******Empiezan los logueos*******"
##  miArbolUsuario.loguearUsuario("ratan","12345678")
##  print "**********************************"
##  miArbolUsuario.loguearUsuario("ratAn","1234567")
##  print "**********************************"
##  miArbolUsuario.loguearUsuario("ratAn","12345678")
##  print "**********************************"
##  miArbolUsuario.loguearUsuario("rataT","7777rttRr77777paprplWffrw")
##  print "**********************************"
##  miArbolUsuario.loguearUsuario("rataT","7777rttrr77777paprplWffrw")
##  print "Este es el nodo buscado"
##  print nodoUser.verNodoUsuario()
##  print " antes de eliminar"
## ## miArbolUsuario.PostOrdenAvl(miArbolUsuario.Raiz)
## ## miArbolUsuario.InordenAvl(miArbolUsuario.Raiz)
##  miArbolUsuario.PreOrdenAvl(miArbolUsuario.Raiz)
##  print "Esta es la cantidad de nodos: " +str(miArbolUsuario.CantidadNodosAvl(miArbolUsuario.Raiz))
##  print "Esta es la Altura del arbol: " +str(miArbolUsuario.AlturaArbol(miArbolUsuario.Raiz))
##  miArbolUsuario.eliminarContacto("ratan")
##  print "Despues de eliminar"
## ## miArbolUsuario.PostOrdenAvl(miArbolUsuario.Raiz)
## ## miArbolUsuario.InordenAvl(miArbolUsuario.Raiz)
##  miArbolUsuario.PreOrdenAvl(miArbolUsuario.Raiz)
##  print "Esta es la cantidad de nodos: " +str(miArbolUsuario.CantidadNodosAvl(miArbolUsuario.Raiz))
##  print "Esta es la Altura del arbol: " +str(miArbolUsuario.AlturaArbol(miArbolUsuario.Raiz))

##    miArbolVuelos = ArbolAvlVuelos.ArbolAvlVuelos()
##    miArbolVuelos.insertarVuelo("Mexico","20:00","23/03/2015","03:00","24/03/2015",20,2000,200,850,50,1300,"Aeropuerto")
##    miArbolVuelos.insertarVuelo("Espania","20:00","23/03/2015","03:00","24/03/2015",20,2000,200,850,50,1300,"Aeropuerto")
##    miArbolVuelos.insertarVuelo("Salvador","20:00","23/03/2015","03:00","24/03/2015",20,2000,200,850,50,1300,"aterriza")
##    miArbolVuelos.insertarVuelo("Germany","20:00","23/03/2015","03:00","24/03/2015",20,2000,200,850,50,1300,"vuelo")
##    miArbolVuelos.insertarVuelo("Germany","20:00","23/03/2015","03:00","24/03/2015",20,2000,200,850,50,1300,"vuelo")
##    miArbolVuelos.insertarVuelo("Guate","20:00","23/03/2015","03:00","24/03/2015",20,2000,200,850,50,1300,"aterriza")
##    miArbolVuelos.insertarVuelo("Italia","20:00","23/03/2015","03:00","24/03/2015",20,2000,200,850,50,1300,"Aeropuerto")
##    print "************** Estos son los que estan en el aeropuerto *********"
##    nodo = miArbolVuelos.VerVuelosPorEstado("aeropuerto")
##    print "************** Estos son los que estan en vuelo ***************"
##    nodo = miArbolVuelos.VerVuelosPorEstado("vuelo")
##    print "******************* Estos son los que estan aterrizando ********************"
##    miArbolVuelos.VerVuelosPorEstado("aterriza")
##    print "************ Estos van para alemania *************"
##    miArbolVuelos.VerVuelosPorDestino("germany")

    a=1
    b=copy.copy(a)
    a=a+5
    b=b+2
    print "Esto tiene a: " + str(a)
    print "Esto tiene b: " + str(b)



if __name__ == '__main__':
    main()