from client import myClient
import os
from menu import myMenu
from my_function import menuToList,headerMain,_orderToTuples
from os import system
import datetime
from commande import myOrder


## --------------- MAIN - MENU ---------------##
def _firstMenu():
    txt = ["RESTAURANT SUPINFO", "ACCUEIL"]
    _ = system("clear||cls")
    headerMain(txt)
    menuPrincipale = ["PRISE DE COMMANDE","HISTORIQUE COMMANDE","QUITTER"]
    menu =myMenu(menuPrincipale,"MENU PRINCIPALE")
    menu.afficher_menu()
    entry = menu.choix_menu("QUE VOULEZ VOUS FAIRE ? (1-3):")
    _ = system("clear||cls")
    if (entry == '1'):
        path = orderMenu()
        L =  load_menu()
        order = myOrder()
        order.path = path
        orderOption(order, L)
    elif (entry == '2'):
        historique()
    elif (entry == '3'):
        pass
    else:
        print(entry + " n'est pas une entree valable (1-2)")







#chargez les plats depuis menu.txt
def load_menu():
    path = os.path.abspath("main.py")
    path = os.path.split(path)[0]+"/menu.txt"
    menuTxt = menuToList(path)
    print("PLATS DISPONIBLES :")
    i=0
    for x in range(0,len(menuTxt),2):
        i += 1
        print(f"{i}. {menuTxt[x].name}--{menuTxt[x].price}")
    return menuTxt
    

#generer fichier commande et saisir infos client
def orderMenu():
    txt = ["RESTAURANT SUPINFO", "CARTE RESTAURANT"]
    _ = system("clear||cls")
    headerMain(txt)
    client = myClient()
    client.saisir_client()

    path = os.path.abspath("main.py")
    path = os.path.split(path)[0]+"/orders/"+client.nomFile()+".txt"

    file = open(path, "w")
    file.write("DATE :\n")
    file.close()
    file = open(path, "a")
    file.write("(JOUR - MOIS)\n")
    file.write(str(datetime.datetime.now().day) + " - " + str(datetime.datetime.now().month) + "\n")
    file.write("PRIX TOTAL :\n")
    file.write("0\n")
    file.write("COMMANDE :\n")
    file.write("(PLAT - QUANTITE)\n")
    file.close()
    return (path) 


#options commander(remplir commande,continuer commande,valider commande)
def orderOption(order, L):
    menuPrincipale = ["SELECTIONNER UN PRODUIT","RESUME DE LA COMMANDE","Valider COMMANDE","RETOUR AU MENU PRINCIPAL"]
    menu =myMenu(menuPrincipale,"menu carte")
    menu.afficher_menu()
    entry = menu.choix_menu("QUE VOULEZ VOUS FAIRE ? (1-4) :")
    _ = system("clear||cls")
    txt = ["RESTAURANT SUP INFO", ""]
    headerMain(txt)
    load_menu()
    if (entry == '1'):
        print("QUEL PLAT VOULEZ VOUS SELECTIONNER ?")
        i = int(input())
        print("COMBIEN EN VOULEZ VOUS ?")
        count = int(input())
        plat = L[i-1]
        order.plat = plat
        order.count = count
        order.add()
        _ = system("clear||cls")
        load_menu()
        orderOption(order, L)
    elif (entry == '2'):
        show_resume_commande(order)
        orderOption(order, L)
    elif (entry  == '3'):
        _firstMenu()
    elif (entry == '4'):
        _firstMenu()


    

    
def show_resume_commande(order):
    file = open(order.path, "r")
    L = file.readlines()
    (_, _, OrdList) = _orderToTuples(L)
    s = "----------------------------------------------------\n"
    s += "   ETAT DE LA COMMANDE :\n"
    for i in OrdList:
        s += i[0] + " " * (27 - len(i[0])) + " QUANTITE " + i[1] + "\n"
    s += "   PRIX TOTAL :\n"
    s += L[4].strip("\n") + " FCFA\n"
    file.close()
    print(s)
    print(" 1. RETOUR AU MENU PRINCIPAL")
    print(" 2. Continuer")
    entry = input()
    if (entry == '1'):
        _firstMenu()
    elif entry == '2':
        L =  load_menu()
        orderOption(order, L)
    else:
        print("choix non disponible")

def historique():
        txt = ["RESTAURANT SUPINFO", "HISTORIQUE DES COMMANDES"]
        _ = system("clear||cls")
        headerMain(txt)
        orderL = os.listdir("orders")
        totalOrder, lastOrder = len(orderL),datetime.date(2000, 1, 1)
        totalPrice = 0
        s = "\nNOMBRE TOTAL DE COMMANDES PASSEES : " + str(totalOrder) + "\n"
        path = os.path.abspath("main.py")
        path = os.path.split(path)[0]+"/orders/"
        for i in orderL:
            Thispath = path + str(i)
            file = open(Thispath, "r")
            Lst = file.readlines()
            totalPrice += int(Lst[4].strip("\n"))
            (d, m, L) = _orderToTuples(Lst)
            date = datetime.date(2020, int(m), int(d))
            if (date > lastOrder):
                lastOrder = date

        s += "TOTAL PAYE : " + str(totalPrice) + " FCFA\n"
        s += "\nDERNIERE COMMANDE : " + str(lastOrder.day) + "/" + str(lastOrder.month) + "\n"
        print(s)
        input("appuyez sur n'importe quelle touche pour continuer")
        _firstMenu()
        return s


## Main ##
_firstMenu()


# build with Python 3.6.9 #
