from abc import ABC, abstractmethod


class Company(ABC):
    @abstractmethod
    def developer(self):
        pass


class jr_developer(Company):
    def developer(self):
        return "jr developer developes small application"


class sr_developer(Company):
    def developer(self):
        return "sr developer developes large applications"


# Note:An Abstract cannot be instantiated; we cannot create objects for the abstract class.

obj1 = jr_developer()
obj2 = sr_developer()
print(obj1.developer())
print(obj2.developer())
