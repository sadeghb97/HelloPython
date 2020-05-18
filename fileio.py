import io
import os

#be mahze inke file ra ba mode w baz konim tamame mohtavaye an pak mishavad
#sepas ba methode write mitavanim mohtavaye jadid ra dar an benevisim
#agar file vojud nadashte bashad an ra misazad
fileObj = open("texts.txt", "w")
fileObj.write("Hello Python ...............")
print("File writing finished!")

#be positione 13 miravim
fileObj.seek(13)

#az khane 13 be bad pak mishavad va mohtavaye jadid dar an neveshte mishavad
fileObj.write("\n!!!!!!!!!!!!!!\n")
fileObj.close()

"""Note that if the file is opened for appending using either 'a' or 'a+', 
any seek() operations will be undone at the next write."""
fileObj = open("texts.txt", "a")
fileObj.write("New Line :)))))))))))))")
print("Current Pos:", fileObj.tell())
fileObj.close()

fileObj = open("texts.txt", "r")
contents = fileObj.read()
print("--------------")
print(contents)
print("---------------")

#hazf va rename file ha
#os.rename("texts.txt", "newname.txt")
#os.remove("newname.txt")

#sakhte dir
#os.mkdir("texts")

print("Current dir: ")
print(os.getcwd())