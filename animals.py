
class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print (self.health)

catfish = Animal("litty",1000)

catfish.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__("dog",150)

    def pet(self):
        self.health += 5
        return self

men = Dog()

men.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self):
        super(Dragon,self).__init__("dragon",170)

    def fly(self):
        self.health -= 10

    def display_health(self):
        super(Dragon,self).display_health()
        print ("I am a Dragon")

crab = Animal()
crab.pet()
crab.fly()
crab.display_health()

men = Dog()
men.fly()
