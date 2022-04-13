from ast import Return


class myClient:
    def __init__(self):
        self.name = ""
        self.numero = ""
        self.adresse = ""
    def afficher_menu(self):
        i = 0
        for x in self.list:
            i+=1
            print(f"{i}-{x}")
    
    def saisir_client(self):
        self.name = input("saisir nom et prenom: ")
        self.adresse = input("saisir adresse: ")
        self.numero = input("saisir numero de telephone: ")
    def nomFile(self):
        return f"{self.name}-{self.numero}-{self.adresse}"
    