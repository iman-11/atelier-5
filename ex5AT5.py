class Etudiant:
 def _init_(self, nom, prenom, age, cne, moyenne):
  self.nom = nom
  self.prenom = prenom
  self.age = age
  self.cne = cne
  self.moyenne = moyenne


# list de type etudiant
Etudiant = [
 {'nom': 'el harti', 'prenom': 'iman', 'age': 20, 'cne': 155223, 'moyenne': 15},
 {'nom': 'mouna', 'prenom': 'izougaghen', 'age': 19, 'cne': 123456, 'moyenne': 16},

]

# trie par age
Etudiant.sort(key=lambda x: x.get('age'))
print("liste trie par age:\n")
print(Etudiant)
# trie par moyenne
Etudiant.sort(key=lambda x: x.get('moyenne'))
print("liste trie par moyenne:\n")
print(Etudiant)

