#création d’un class rectangle
class Rectangle:
    #constructeur
    def __init__(self, L, l,nom="rectangle"):
       self.L = L
       self.l = l
       self.nom = nom
    #methode pour afficher les cotes
    def display(self):
        print(" L: %d \n l: %d \n nom:%s" % (self.L, self.l,self.nom))
    #méthode pour calculer la surface
    def surface(self,rec):
        self.x =rec.L*rec.l
        print("la surface est:%d " % (self.x))

#création un class hérite de class rectangle
class carre(Rectangle):
 print("\n")

#crée des objets
rec=Rectangle(20,10)
print("la longueur et la largeur du rectangle :")
rec.display()
"""appel du méthode surface """
rec.surface(rec)
car=carre(3,3,"carre")
print("nom:",car.nom)
car.surface(car)
