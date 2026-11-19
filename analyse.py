
mots_vides = {"le", "la", "les", "de", "des"}
punctuation=[",",":","."]
def lire_fichier():
    f = open("corpus.txt", "r")
    lignes = f.readlines()
    f.close()
    return lignes

def nettoyer_ligne(ligne):
    ligne = ligne.lower()

    for p in punctuation:
        ligne = ligne.replace(p, "")

    return ligne

def supprimer_mots_vides(ligne):
    mots = ligne.split()
    resultat = []

    for mot in mots:
        if mot not in mots_vides:
            resultat.append(mot)

    return resultat