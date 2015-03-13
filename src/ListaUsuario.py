# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import NodoAeropuerto

class ListaAeropuerto:
    
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.longitud = 0
    
    def estaVacia(self):
        if self.inicio==None:
            return True    
        else:
             return False

    def insertarInicio(self, nammm, paais, contras):
        import NodoAeropuerto
        nuevo = NodoAeropuerto(nammm,paais,contras)
        if self.estaVacia()==True:
            self.inicio = nuevo
            self.fin = nuevo
            self.longitud = longitud + 1
        else:
            nuevo.Siguiente = self.inicio 
            self.inicio.Anterior = nuevo
            self.inicio= nuevo
            self.longitud = longitud + 1

    def mostrarListadoAeropuerto(self):
        import NodoAeropuerto
        print("***************")
        aux = self.inicio        
        while aux!=None:
            print(aux.verNodoAeropuerto())            
            aux = aux.Siguiente
            
                    
              
            
            
            
         


