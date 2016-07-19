class Hitac:
  hici=[]
  def __init__(self,pravac):
    self.pravac=pravac
  def dodaj_hitac(self,pravac):
    a=Hitac(pravac)
    self.hici.append(a)
