def hello(name= "Refigh") :
    print("Salam " + name)
    print("Khubi?")
    return #optional

def sum(a, b) :
    return a + b

def printNames(first, second) :
    print("First: " + first)
    print("Second: " + second)

#tabe ba tedad vorudie moshabehe namalum
def getMax(* numList) :
    max = numList[0]
    for num in numList :
        if(num > max) : max = num
    return max

#global vars
number = 0
status = "Everything OK!"

def printStatus() :
    #agar var haye global import nashavand ham mitavan meghdare an hara khand
    #ama agar vare hamname anha dar function init shavad vare jadid local khahad bud
    #va vare global taghir nakhahad kard
    global status
    global number
    number += 1
    print("Status:" + status + " || " + str(number))

#neveshtane tabe ye khati ba returne value ba lambda
multiply = lambda a, b: a *b

hello()
hello("Hamid")
print("Sum: " + str(sum(10, 20)))

#farakhani ba tartib
printNames("Hamid", "Vahid")

#farakhani ba nam
printNames(second= "Hamed", first= "Naser")

print(getMax(24, 256, 321, 788, 10, 29))

print(multiply(4, 8))

#tavabe ra ham mitavan dar moteghayyer rikht
myFunc = sum
print(myFunc(14, 15))

printStatus()
printStatus()
printStatus()