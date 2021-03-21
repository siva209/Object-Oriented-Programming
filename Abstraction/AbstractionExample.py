from abc import ABC, abstractmethod


class Car(ABC):
    """
    Abstract class:A class that consists of one or more abstract method is called the abstract class.
    Abstract methods do not contain their implementation.
    Abstract class can be inherited by the subclass and abstract method gets its definition in the subclass.
    Abstraction classes are meant to be the blueprint of the other class. An abstract class can be useful when we are designing large functions.
    An abstract class is also helpful to provide the standard interface for different implementations of components.
    Python provides the abc module to use the abstraction in the Python program

    """

    @abstractmethod
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()
