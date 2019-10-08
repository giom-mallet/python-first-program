file = open("the_basics/files/bear.txt")
beartext = file.read()
print (beartext[0:90])

def searchFile(path , character) :
    file = open(path)
    text = file.read()
    file.close()
    return text.count(character)

print(searchFile("the_basics/files/bear.txt","a"))

with open("the_basics/files/file.txt","w") as writingfile : 
    writingfile.write("snail") 

with open("the_basics/files/bear.txt") as bearfile : 
    first90 = bearfile.read()[0:90]

with open("the_basics/files/first.txt", "w") as firstfile : 
    firstfile.write(first90)

with open("the_basics/files/bear1.txt") as bear1file :
    bearcontent = bear1file.read()

with open("the_basics/files/bear2.txt", "a") as bear2file :
    bear2file.write("\n" + bearcontent)

with open("the_basics/files/data.txt", "r+") as datafile:
    content = datafile.read()
    datafile.write(content)

