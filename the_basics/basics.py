import datetime
mynow = datetime.datetime.now()
print(mynow)

x=13
y=" times"
z=" Hello"
print(x,y,z)

print(list(range(0,1000,100)))

rainfall = [2.5,5,"Hello",list(range(0,10))]
print(rainfall)

print("Mylist size is : ")

my_list=[1,6,8,4,94,54,54,732,7452,334,7]
print(my_list)

count54 = my_list.count(54)
print(count54)

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
count10 = student_grades.count(10.0)
print(count10)

print("Write to Lower Case")
username = "Python3"
print(username.lower())