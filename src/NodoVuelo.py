# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

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
        self.EstadoVuelo = EstadoVuelo
        self.Izquierda = None
        self.Derecha = None
    
    def VerNodoVuelo(self):
        return " Id Unico: "+ self.IdUnico+" Llegada: " + self.LugarLlegada +" Estado: " + self.EstadoVuelo
    


