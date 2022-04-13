from produit import produit

# Cette fonction prend en entree une liste de string qui formeront le HEADER de chaque menu #
def headerMain(txt):
    
    str = "---------------------------------------------------\n"
    for s in txt:
        str += "--------"
        for i in range (0, (36-len(s))//2):
            str +=" "
        str += s
        for i in range (0, (36-len(s))//2):
            str +=" "
        str += "--------\n"
    str += "---------------------------------------------------"
    print(str)


# Cette fonction permet de recupere une des listes de lines des fichiers textes et separe chaque mots
def tableBuild(list):
    L = []
    for s in list:
        L += s.split(" - ")
    return L


# Cette fonction va convertir un fichier texte menant au storage en liste de couples : (nom, quaitie) #
def storageToList(path):
    file = open(path, "r")
    L = tableBuild(file.readlines())
    M = []
    for i in range (0, len(L), 2):
        M.append( (L[i],L[i+1].strip('\n')) )
    return M

# Cette fonction va transformer une liste de (nom, quantite) en nouveau fichier texte storage #
def listToStorage(path, L):
    file = open(path, "w")
    s = ""
    for i in L:
        s+= i[0] + " - "+ i[1] + "\n"
    file.write(s)

# Cette fonction va convertir un fichier texte menant au menu en une liste de couples : (nom,prix) #
def menuToList(path):
    file = open(path, "r")
    L = tableBuild(file.readlines())
    M = []
    for i in range(0,len(L)-1):
        M.append(produit(L[i],L[i+1].strip('\n')))
    
    return M

# Cette fonction va transformer une liste de (nom, categorie, prix) en nouveau fichier texte menu #
def listToMenu(path, L):
    file = open(path, "w")
    s = ""
    for i in L:
        s+= i[0] + " - "+ i[1] + " - " + i[2]+ "\n"
    file.write(s)


    # L liste des ligne de la commande #
def _orderToTuples(L):
    (day, month) = ( L[2].split(" - ")[0], L[2].split(" - ")[1].strip("\n") )
    Plats = []
    for i in range (7, len(L)):
        Plats.append( ( L[i].split(" - ")[0], L[i].split(" - ")[1].strip("\n") ) )
    return (day, month, Plats)