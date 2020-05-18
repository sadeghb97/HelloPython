class Student :
    "A test class for students"

    #var haei ke inja tarif mishavand static hastand
    created_num = 0

    #avalin arge method hay self hast
    #method haye sazande be in surat tarif mishavand
    def __init__(self, name1, age1, avg1) :
        #var haye zir moteallegh be har obj mishavand
        self.name = name1
        self._age = age1 #protected var
        self.__avg = avg1 #private var

        #baraye dastresi be var haye static name class ra minevisim
        Student.created_num += 1

    def print(self):
        print(f"Name: {self.name} | Age: {self._age} | Avg: {self.__avg}")

    #2 methode pishfarze hame class ha ke mitavan an hara override kard
    #....

    #python khod har gah niaz bashad var hara pak mikonad
    #dar in zaman methode zir anjam mishavad
    #hamin tor agar khodeman ba keyworde del an ra pak konim
    def __del__(self):
        print("Shey pak shod!!!")

    #tarife str vaghti object be str bayad tabdil shavad
    def __str__(self):
        return f"{self.name} - {self._age} - {self.__avg}"

st1 = Student("Sadegh", 24, 100)
st2 = Student("Reza", 16, 40)
st1.print()
st2.print()
print(st1)

#programmer ha nabayad var haye protected ra taghir dahand
#vaghti ghable name yek attr yek _ mizarim mikhaim neshun bedim ke protectede
#va garna hanuz ham mitavan be meghdare an az birun dastresi dasht va an ra
#taghir dad
print(st1._age)

#print(st1.__avg) -> Access Error
print("Student class created num:", Student.created_num)

#tedadi az var haye static moteallegh be har clas
print("-------------")
print(Student.__doc__)
print(Student.__name__)
print(Student.__module__)
print(Student.__base__)
print(Student.__dict__)

print("-------------")
setattr(st1, "_age", 25)
print("St1 has Age attr:", hasattr(st1, "_age"))
print("St1 Age:", getattr(st1, "_age"))
delattr(st1, "_age")
print("St1 has Age attr:", hasattr(st1, "_age"))