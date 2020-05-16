list1 = [14, 256.36, "Hamid", ["yek", "Do"]]
list2 = [145, 2000]

#amalgare + dar list ha
sumList = list1 + list2
print(sumList)
print(sumList[4])

#amalgare zarb dar list ha
print(list2 * 2)

#ba keyworde del har vari ra mitavan hazf kard
anotherList = [0, 1, 2, 3, 4, 5, 6, 7]
del anotherList[4]
print(anotherList)

#ba append mitavan be list onsor ezafe kard
print(len(anotherList))
anotherList.append("val1")
print(anotherList)
print(len(anotherList))

#error (kharej az range) -> anotherList[8] = "val2"
#error (kharej az range) -> anotherList[9] = "val3"
anotherList[0] = "Sefr"
print(anotherList)

print(anotherList[:3])

#keyworde in
anotherList.append(0)
anotherList.append(0)
print(anotherList)
print(0 in anotherList)
print("0" in anotherList)
print("sefr" in anotherList)
print("Sefr" in anotherList)
print((anotherList.count(0)))

