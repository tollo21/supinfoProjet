class myMenu:
    def __init__(self,list,name):
        self.list = list
        self.name = name


    def afficher_menu(self):
        i = 0
        print(self.name)
        for x in self.list:
            i+=1
            print(f"{i}. {x}")


            
    def choix_menu(self,message):
        check = True
        choix = ""
        while check:
            test = int(input(message))
            if(test>0 and test<=len(self.list)):
                check = False
                choix = str(test)
            else:
                print("veuillez choisir une option disponible")
        
        return choix