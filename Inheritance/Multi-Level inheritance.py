class Animal:
    def speak(self):
        print("Animal Speaking")


class Dog(Animal):
    def bark(self):
        print("Dog barking")


class Cat(Dog):
    def dance(self):
        print("cat danceing")


c = Cat()
c.speak()
c.bark()
c.dance()
