#### Fonctions secondaires

"""exercice liste de syracuse"""
# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """dessine la graphique"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(p):
    """retourne la suite de Syracuse de source p

    Args:
        p (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source p
    """
    n = 0
    l=[p]

    while n < 200 and p != 1:
        #   - calcul du p suivant
        if p%2 == 0:
            p = p/2
        else :
            p = p*3 + 1
        l.append(p)
        n+=1

    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    for i, el in enumerate(l):
        if el == 1:
            return i+1
        return "erreur du programmeur"

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici
    for i,el in enumerate(l):
        if el < l[0] :
            return i
        return "erreur du programmeur"


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    return max(l)


#### Fonction principale


def main():
    """appels à la fonction secondaire ici"""
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print("temps de vol :", temps_de_vol(lsyr))
    print("temps de vol en altitude :", temps_de_vol_en_altitude(lsyr))
    print("altitude maximale :", altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
