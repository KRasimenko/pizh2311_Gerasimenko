class Person:
    def __init__(self, name, surname,q=1 ):
        self.person_name = name
        self.person_surname = surname
        self.qualification = q
    def Getinfo(self):
        return "{0} {1} {2}".format(self.person_name, self.person_surname,self.qualification)
    
        
    def __del__(self):
        print("До свидания, мистер", self.person_name, self.person_surname)
employee1 = Person("Константин","Герасименко",16)
employee2 = Person("Алексей","Щеголев",16)
employee3 = Person("Альберт", "Жмышенко",5)

print(employee1.Getinfo())
print(employee2.Getinfo())
print(employee3.Getinfo())

del employee3
input()

