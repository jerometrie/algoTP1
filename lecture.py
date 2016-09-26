class lecture:
    ch = input()
    index = -1
    def __init__(self):
        if self.__class__.index >= len(self.__class__.ch)-1:
            self.__class__.ch = input()
            self.__class__.index = 0
        else :
            self.__class__.index += 1
    def getChar(self):
        if len(self.__class__.ch) == 0:
            return "\n"
        return self.__class__.ch[self.__class__.index]


# fonction lire sans parametre, retourne et consomme un caractere
# saisi au clavier a chaque appel
def lire():
    lect = lecture()
    return lect.getChar()
        
# procedure qui ecrit le caractere c sur la sortie standard
def ecrire(c) :
    print(c, end="")

# procedure qui effectue un passage a la ligne sur la sortie   
def nouvelle_ligne() :
    print("")
# nombre d'espaces avant une section
espace = 3 


# procedure qui affiche e espaces et le numero de section sous la forme (s)
# s : numero de section
# e : nombre d'espaces correspondant a l'indentation d'un titre de section
def section(s,e) :
    nouvelle_ligne()
    i = 1
    while i <= e :
        ecrire(" ")
        i = i+1
    print("(",s,") ", end="")

# procedure qui affiche e espaces et le numero de sous section sous la forme s.i
# s : numero de section
# i : numero de sous section
# e : nombre d'espaces correspondant a l'indentation d'un titre de sous section
def sous_section(s,i,e) :
    nouvelle_ligne()
    j = 1
    while j <= e :
        ecrire(" ")
        j=j+1
    print("",s,".",i," ", end="")
