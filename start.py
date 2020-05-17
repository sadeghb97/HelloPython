#typeDynamic language

"""
commente chand khati
khate dovom
khate sevom
"""

#niaz be taine noe nist va noe var mitavanad taghir konad
a = "sadegh"
print(a)
a = 10
print(a)

#nahve neveshtane do khat code dar yek khat
b = 15; b+=10
print(b)

#anvae vars
#number
#string
#list
#tuple
#dictionary

#chand entesab hamzaman
a,b,c = 1,2,"Reza"
print(a,b,c)

c = 50
print(c)
a = b = c = 40
print(c)

#reshteye chand khati
text = """khate aval
khate dovom
khate sevom"""
print(text)

#elhaghe do reshte ba operatore + va ,
#agar az virgul estefade konim yek space beine reshte ha ezafe mishavad
#ham chenin dar amalgare + amalvand ha bayad ba ham bekhanand masalan
#reshte ra ba adad nemitavan jam kard (vali virgul in moshkelo nadare)
grade = 14
print("Grade:" + str(grade))
print("Score:", grade)

#amalgare * ham baraye reshteha darim
print("Salam" * 3)

int_number = 2500
long_number = 26545646465456456464
float_number = 105.25e+6
complex_number = 16.5e-4j


#Operators
#** -> tavan
#// -> jazr
print(3 ** 3)

int_number = int("145")
c1 = 14 + 5j
c2 = complex(14, 5)
print("c1==c2: ", c1==c2)

print(max(4, 8, 52))

text2 = "Python strings is excellent!!!"
print(text2[1])
print(text2[0:4])
print(text2[:4])
print(text2[4:])
print(len(text2))
print(text2.count(" ")) #tedade space ha tuye reshte ro barmigardune
print("string" in text2)
print("string" not in text2)

print("Sadegh\nBagherzadeh")

seperator = ","
print("hamid%s reza%s mehdi" %(seperator, seperator))

text3 = "hamid be Madrese raft"
print(text3.capitalize()) #harfe avale jomle bozorg va baghie kuchik
print(text3.upper())
print(text3.split(" "))