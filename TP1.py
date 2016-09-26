#coding: utf-8
# Jérôme Delécluse
# TP1 ALGO - Mise en forme d’un texte divisé en sections et sous sections

# Pour lancer ce programme avec en entrée le fichier test.txt,
# en ligne de commande: python3 TP1.py < test.txt


# Importation des fonctions lire(), écrire(), et celles de sections
from lecture import *

def miseEnForme1():
    """ Fonction qui restitue un fichier texte mis en forme sur l'écran """

    # Variable a: stocke les '\' et b stocke le caractère suivant
    a = lire()
    b = lire()

    s = 1 # Numéro de section
    i = 1 # Numéro de sous-section

    while (not(a == '\\' and b == '.')):
        
        # Gestion des passages à la ligne et des sections/sous-sections
        if(a == '\\'):
            if(b == '\\'):
                a = b
                b = lire()
            elif(b == 'n'):
                nouvelle_ligne()
                a = lire()
                b = lire()
            elif(b == 's'):
                section(s, 3)
                s = s +1
                i = 1
                a = lire()
                b = lire()
            elif(b == 'i'):
                sous_section(s, i, 6)
                i = i +1
                a = lire()
                b = lire()
            else:
                ecrire(b)
                a = lire()
                b = lire()
        
        # Cas de la vigule
        elif(a == ","):
            if(b == " "):
                ecrire(a)
                ecrire(b)
                a = lire()
                b = lire()
            else:
                ecrire(a)
                ecrire(" ")
                ecrire(b)
                a = lire()
                b = lire()

        # Cas du passage à la ligne
        elif(a == "\n"):
            a = b
            b = lire()

        # Cas général
        else:
            ecrire(a)
            a = b
            b = lire()

    print()


def miseEnForme():
    """ Fonction qui restitue un fichier texte mis en forme sur l'écran """

    # Variable a: stocke les '\' et b stocke le caractère suivant
    a = lire()
    b = lire()

    s = 1 # Numéro de section
    i = 1 # Numéro de sous-section

    while (not(a == '\\' and b == '.')):
        
        # Gestion des passages à la ligne et des sections/sous-sections
        if(a == '\\'):
            if(b == '\\'):
                ecrire(a) # Pour afficher les \ qui ne font pas partie d'une instruction
                a = b
                b = lire()
            elif(b == 'n'):
                nouvelle_ligne()
                a = lire()
                b = lire()
            elif(b == 's'):
                section(s, 3)
                s = s + 1
                i = 1
                a = lire()
                b = lire()
            elif(b == 'i'):
                sous_section(s - 1, i, 6)
                i = i +1
                a = lire()
                b = lire()
            else:
                ecrire(b)
                a = lire()
                b = lire()
        
        # Cas de plusieurs espaces consécutifs
        elif(a == ' ' and b == ' '):
            a = b
            b = lire()

        # Cas de la vigule
        elif(a == ","):
            if(b == " "):
                ecrire(a)
                ecrire(b)
                a = lire()
                b = lire()
            else:
                ecrire(a)
                ecrire(" ")
                ecrire(b)
                a = lire()
                b = lire()

        # Cas du passage à la ligne
        elif(a == "\n"):
            a = b
            b = lire()

        # Cas général
        else:
            ecrire(a)
            a = b
            b = lire()

    print()


#miseEnForme1()
miseEnForme()

"""
Question 3:

- Texte avec \. (le "." du milieu ne doit pas être pris en compte)

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa, nam\.


- Texte avec toutes les instructions (vérifie aussi l'incrémentation des sections et des sous-sections):

\sLorem \iipsum \idolor \ssit \iamet \iconsectetur adipisicing elit. Mollitia 
deserunt\nlibero sed. Labore obcaecati aspernatur officiis, voluptas numquam ad, eos.\.


- Texte vérifiant des cas spéciaux:
    - \ doit afficher un \
    - \\s\\\i doit afficher \ et passer à une section, puis \ et passer à une sous-section.

\Lorem ipsum dolor sit amet, consectetur \\s\\iadipisicing elit. 
Tenetur magni quia nesciunt sint pariatur iste harum officiis debitis, rem in.\.


- \. dès le début du fichier. Rien ne doit s'afficher.


- Passer à la ligne au milieu de "\s" par exemple doit bien afficher une section

\
s\.


- Texte avec n\\n\. : doit afficher n\ et passer à la ligne (n\ ne doit pas être pris pour une instruction, contrairement
à \n). Ce cas teste aussi \\, qui ne doit pas être considéré ici comme un affichage de \.


- Cas non géré (mais vraiment très aux limites):

\ \.

n'affiche pas \

"""













