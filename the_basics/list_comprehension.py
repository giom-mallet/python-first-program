temps = [99,'no_data', 95 , 94, 'no data']

print(type(temps[1]), type(temps[0]))
print(type(temps[1]) == int, type(temps[0]) == int )

def foo( one_list ):
    return [value for value in one_list if type(value) == int]

def better_foo( one_list ):
    return [value if type(value) == int else 0 for value in one_list ]

print(foo(temps))
print(better_foo(temps))



def sum_string(list_str):
    return sum([float(value) for value in list_str])

print(sum_string(['1.2','2.6','3.3']))

def double_if_pair(value) :
    """ Renvoie le double de value si value est pair, et value sinon"""
    if value % 2 ==0 :
      return value*2
    else :
        return value 

table = range(1,10)
print([double_if_pair(value) for value in table])



