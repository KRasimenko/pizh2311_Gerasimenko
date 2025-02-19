from random import randint
class Person:
    count = 0
    def __init__(self,t):
        self.id = Person.count
        Person.count +=1
        self.team = t

class Hero(Person):
    def __init__(self,t):
        Person.__init__(self,t)
        self.lvl = 1
    def lvlUp(self):
        self.lvl+=1

class Solider(Person):
    def __init__(self,t):
        Person.__init__(self,t)
        self.myHero = None
    def follow(self,hero):
        self.myHero = hero.id

Arthas = Hero("people")
Traal = Hero("orcs")

people_army = []
orcs_army = []
for i in range (10):
    n = randint(1,2)
    if n==1:
        people_army.append(Solider("people"))
    else:
        orcs_army.append(Solider("orcs"))
print(len(people_army), len(orcs_army), "\n")
if len(people_army)>len(orcs_army):
    Arthas.lvlUp()
else:
    Traal.lvlUp()
people_army[0].follow(Arthas)
print(people_army[0].id, Arthas.id)
