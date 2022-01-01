"""crée un class"""
class Vecteur2D:
    #déclaration d’un constructeur
    def __init__(self, x=0, y=0):
       self.x = x
       self.y = y
   #méthode display pour afficher les coordonnées
    def display(self):
        print("X: %d \n Y: %d" % (self.x, self.y))

   #méthode pour calculer la somme
    def somme(self,vect1,vect2):
        self.x=vect2.x+vect1.x
        self.y=vect2.y+vect1.y

#crée des objet de type vecteur
vec1=Vecteur2D(4,6)
vec2=Vecteur2D(2,5)
vec3=Vecteur2D()
print("les coordonnées de vect1:")
#appel méthode display
vec1.display()
print("les coordonnées de vect2:")
vec2.display()
#calculer somme des deux vecteurs
vec3.somme(vec1,vec2)
print("la somme des deux vecteurs:")
vec3.display()




