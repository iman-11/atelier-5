"""classe de vecteur."""
class Vecteur2D:
    """constructeur pour initialiser les coordonnees """
    def __init__(self, x=0, y=0):
       self.x = x
       self.y = y
       print(" les coordonnees de vecteur2D : \n X: %d \n Y: %d" % (self.x, self.y))


"""cree un objet de type vecteur2d """
vec1=Vecteur2D()
vec2=Vecteur2D(2,5)


