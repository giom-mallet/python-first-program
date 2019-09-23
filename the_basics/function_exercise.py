def lengther(lst):
    return len(lst)

print("Result of the lengther function : ")
print(lengther([1,2,3,4,5.6,7,8,9]))

def areasquare(c):
    return c*c

print("Result of the area squared function: ")
print(areasquare(3))

def oz2ml(v):
    return v*29.57353

print("result of the Volume Converter : ")
print(oz2ml(5))


def pwdcheck(value):
    return len(value) > 7

print(pwdcheck("mypass1"))
print(pwdcheck("mypass12"))

def say_hi(name):
    return "Hi {}".format(name)

print(say_hi("Giom"))

def upper_say_hi(name):
    first_letter = name[0]
    rest_letters = name[1:]
    return "Hi {}{}".format(first_letter.upper(),rest_letters)

print(upper_say_hi("Giom"))
print(upper_say_hi("giom"))
