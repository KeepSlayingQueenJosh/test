import random
import time

def ts():
    time.sleep(1)

def optionChoose():
    while True:
        try:
            attackMethod = int(input('Choose your attack method:\n1: Sword\n2: Shield\n3: Bow\n'))
            if attackMethod < 1 or attackMethod > 3:
                raise ValueError()
            return attackMethod
            break
        except:
            print('Invalid option, try again.')

class OgreJames:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.damage = damage
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health

ogre = OgreJames('Ogre James', 500, 

monsterHealth = 500
playerHealth = 500

while monsterHealth != 0:
    chosenOption = optionChoose()

    if chosenOption is 1:
        monsterHealth = monsterHealth - 50
        print(f'You dealt 50 damage. Monster is now on {monsterHealth} health.')
        ts()
    elif chosenOption is 2:
        print('You have been shielded.')
    elif chosenOption is 3:
        print('You have taken a step back to shoot')
print('Congratulations, you killed it!')
