user_input = ""
resultstring = []

while user_input != "/end" : 
    if user_input != "" :
        resultstring.append(user_input)
        print ("appending : {}".format(user_input))
    print(resultstring)
    user_input = input("Say Something : ")
    

final_string = ""
for sentences in resultstring :
    final_string = final_string + sentences.title().rstrip()
    if final_string[-1:] == "?" or final_string[-1:] == "." or final_string[-1:] == "!":
        continue
    final_string = final_string + ". "
    
print (final_string)

