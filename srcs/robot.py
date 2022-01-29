from math import *
import random
class robot:

    ########## appel a un autre constructeur : notion d'heritage simple
    # instanciation des attributs

    def __init__(self,positionX,positionY,dir):
        super().__init__()
        self.positionX=positionX
        self.positionY=positionY
        self.dir= 90 #direction par défaut
    def changeDir(self, dir):
        if dir >= 0 and dir <= 360:
            self.dir = dir
        else:
            print(f"La direction doit être comprise entre 0 et 360 degrés. Retour à la direction par défaut : {self.dir}°")

    def deplacerPositionRobotAvant(self):
        if (self.positionX >= 0. and self.positionY>=0.):
            self.positionX = self.positionX + random.uniform(0.0,20.0)
            self.positionY = self.positionY + random.uniform(0.0,15.0)#### facultatif, peut etre modifie avec la direction du robot
        # dans les autre cas ne rien faire
    def deplacerPositionRobotDerriere(self):
        if (self.positionX < 0. and self.positionY < 0.):
            self.positionX = self.positionX - random.uniform(0.0,20.0)
            self.positionY = self.positionY - random.uniform(0.0,15.0) #### la methode random uniform renvoie un reel compris entre a et b exclus
    def changeDirectionRobot(self):
        if self.deplacerPositionRobotAvant():
            dx = (dx + x)*cos(dir)
        elif self.deplacerPositionRobotAvant():
            dx = (dx - x)*cos(dir)
        elif self.deplacerPositionRobotDerriere():
            dy = (dy + y)*sin(dir)
        elif self.deplacerPositionRobotDerriere():
            dy = (dy - y)*sin(dir)
    ####### la fonction prend en argument l'abscisse et l'ordonee
    def deplaceRobotArgument(self):
        # deplacer le robot vers cette position (X et Y)

        ###### determiner la direction exacte de notre Robot

        if self.positionX >= 0. and self.positionY >= 0. :
            #dx = (dx + x)*cos(dir) ### on s'occupe de changernla direction du robot
            #dy = (dy + y)*sin(dir)
            self.changeDirectionRobot()
            self.deplacerPositionRobotAvant()

        elif self.positionX >= 0. and self.positionY < 0. :
            dx = (dx + x)*cos(dir)
            dy = (dy - y)*sin(dir)
            self.changeDirectionRobot()
            self.deplacerPositionRobotAvant()

        elif self.positionX < 0. and self.positionY >= 0. :
            dx = (dx - x)*cos(dir)
            dy = (dy + y)*sin(dir)
            self.changeDirectionRobot()
            self.deplacerPositionRobotAvant()
        else:
            dx = (dx - x)*cos(dir)
            dy = (dy + y)*sin(dir)
            self.changeDirectionRobot()
            self.deplacerPositionRobotAvant()
