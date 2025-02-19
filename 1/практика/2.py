from random import randint
class Varrior:
    def Sethp(self,value):
        self.hp = value
class Fight:
    def Checkhp(varrior1, varrior2):
        print("Количество хелфпоинтов у первого: ", varrior1.hp,"\n","Количество хелфпоинтов у второго: ", varrior2.hp,"\n")
    def kick(enemy):
        enemy.hp -=20
first = Varrior()
second = Varrior()
second.Sethp(100)
first.Sethp(100)
while(first.hp>0 and second.hp>0):
    n = randint(1,2)
    if n==1:
        print("Первый бьет второго")
        Fight.kick(second)
        print("Второй получает 20 урона")
        Fight.Checkhp(first, second)
    else:
        print("Второй бьет первого")
        Fight.kick(first)
        print("Первый получает 20 урона")
        Fight.Checkhp(first,second)
if first.hp == 0:
    print("Второй воин одержал победу")
if second.hp == 0:
    print("Первый воин одержал победу")

