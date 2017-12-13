import turtle

james = turtle.Turtle()
def carre(taille, couleur):
 "fonction qui dessine un carré de taille et de couleur déterminées"
 james.color(couleur)
 for c in range(4):
  james.forward(taille)
  james.right(90)
james.up() # relever le crayon
james.goto(-150, 50) # reculer en haut à gauche
# dessiner dix carrés rouges, alignés :
for i in range(10):
 james.down() # abaisser le crayon
 carre(25, 'red') # tracer un carré
 james.up() # relever le crayon
 james.forward(30) # avancer + loin 
