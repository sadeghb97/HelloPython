from first_class import Student

class Collegian(Student) :
    "A test class for collegians"

    def __init__(self, name1, age1, avg1, code1):
        super().__init__(name1, age1, avg1) #sazande clase super bayad seda zade shavad
        self.__code = code1

    #override kardane print
    def print(self):
        #avg be ers borde nashode pas nemitavan az an estefade kard
        print(f"Daneshju: ({self.name}, {self._age}, {self.__code})")

print("***********************")
c1 = Collegian("Hamid", 22, 100, 53211125)
c1.print()

