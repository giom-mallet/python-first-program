colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    print(color)

print("big colors only :")

for color in colors :
    if(color > 50) :
        print(color)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

print("integers only :")

for color in colors :
    if type(color) == int and color > 50:
        print(color)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
     
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for name , phone in phone_numbers.items() :
    print("{}: {}".format(name, phone))


foolist = ["toto","tata","tutu"]

def uppercase_list(*args):
    result = []
    for txt in args : 
        result.append(txt.upper())
    result.sort()
    return result




