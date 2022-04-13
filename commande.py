from calendar import c
from os import system, name

class myOrder:
    date = ""
    path = ""
    plats = None
    count = 0
    
    def afficher_commande(self):
        pass

    def add(self):
        file = open(self.path, "a")
        file.write(self.plat.name + " - " + str(self.count) + "\n")
        file.close()
        file = open(self.path, "r")
        L = file.readlines()
        file.close()
        file = open(self.path, "w")
        L[4] = str( int(L[4]) + (int(self.plat.price) * self.count) ) + "\n"
        file.writelines(L)
        file.close()


