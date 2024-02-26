class Person:
    def __init__(self,given_name,family_name) -> None:
        self.given_name = given_name
        self.family_name = family_name
        pass
    @property
    def given_name(self):
        return self.__given_name
    @given_name.setter
    def given_name(self,name):
        self.__given_name = name
        return
    @property
    def family_name(self):
        return self.__family_name
    @family_name.setter
    def family_name(self,name):
        self.__family_name = name
        return 
    @property 
    def name(self):
        names = [
            self.given_name,
            self.family_name
        ]
        return " " .join(names)
    pass
p = Person("lou May","Law")
print(p.name)
p = Person("john macharia", "Njenga")
print(p.name)
