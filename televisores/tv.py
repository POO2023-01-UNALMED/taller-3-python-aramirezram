class TV:
    numTV=0
    def __init__ (self,marca,estado):
        self.canal=1
        self.volumen=1
        self.precio=500
        self.marca=marca
        self.estado=estado
        self.control=None
        TV.numTV+=1
    def setMarca (self,marca):
        self.marca=marca
    def getMarca (self):
        return self.marca

    def setControl (self,control):
        self.control=control
    def getControl (self):
        return self.control

    def setPrecio (self,precio):
        self.precio=precio
    def getPrecio (self):
        return self.precio

    def setVolumen(self,volumen):
        if volumen>7 or volumen<0 or self.estado==False: return
        self.volumen=volumen
    def getVolumen(self):
        return self.volumen

    def setCanal (self,canal):
        if canal>120 or canal<1 or self.estado==False: return
        self.canal=canal
    def getCanal (self):
        return self.canal

    def getNumTV(self):
        return TV.numTV
    def setNumTV(self):
        TV.numTV=self
        
    def turnOn(self):
        self.control=True
    def turnOff(self):
        self.control=False
  
    def canalUp(self):
        if self.canal==120: return
        self.canal=self.canal+1
    def canalDown(self):
        if self.canal==0: return
        self.canal=self.canal-1
  
    def volumenUp(self):
        if self.volumen==7: return
        self.volumen=self.volumen+1
    def volumenDown(self):
        if self.volumen==0: return
        self.volumen=self.volumen-1
    
    def getEstado(self):
        return self.estado
