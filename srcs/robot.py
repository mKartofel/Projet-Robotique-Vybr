from math import cos,sin,pi

class Robot:

    ########## appel a un autre constructeur : notion d'heritage simple
    # instanciation des attributs

    def __init__(self,positionX,positionY):
        """
        :positionX: int
        :positionY: int
        Représente un robot avec une position initiale (positionX, positionY)
        """
        super().__init__()
        self.positionX=positionX
        self.positionY=positionY
        self.dir= 90 #direction par défaut

    def changeDir(self, dir):
        """
        :dir: int
        fonction qui change la direction du robot selon l'angle 'dir'
        """
        if dir >= 0 and dir <= 360:
            self.dir = dir
        else:
            print(f"La direction doit être comprise entre 0 et 360 degrés. Retour à la direction par défaut : {self.dir}°")

    def deplacerPositionRobotAvant(self,distance):
        """
        :positionX: int
        :positionX: int
	    :dir: int
        :distance: int
        fonction qui deplace  le robot depuis les coordonnées(positionX,positionY) vers l'avant selon l'angle 'dir' et une distance
        """
        dir = self.dir * pi / 180 #conversion des degrés en radians
        dx = distance * cos(dir)
        dy = distance * sin(dir)
        self.positionX = self.positionX + dx
        self.positionY = self.positionY - dy 

    
    def deplacerPositionRobotArriere(self,distance):
        """ 
        :positionX: int
        :positionX: int
	    :dir: int
        :distance: int
        fonction qui déplace  le robot depuis les coordonnées(positionX,positionY) vers l'arriere selon l'angle 'dir' et une distance
	    """
        opposite_dir = (self.dir * pi / 180) + pi #conversion des degrés en radians + on ajoute pi pour obtenir la direction inverse
        dx = distance * cos(opposite_dir)
        dy = distance * sin(opposite_dir)

        self.positionX = self.positionX + dx
        self.positionY = self.positionY - dy

    def deplacerRobotVersPosition(self,positionX,positionY,dir,distance):
        if dir < 0 and dir > 180:
            self.changeDir(dir)
            # on dirige notre robot vers l'avant
            self.deplacerPositionRobotAvant(positionX,positionY,dir,distance)
        else: # le robot se deolacera en position arriere
            self.deplacerPositionRobotDerriere(positionX,positionY,dir,distance)
