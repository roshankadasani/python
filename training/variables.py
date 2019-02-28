counter = 100
miles   = 1000.1
name    = "Batman"

print (counter)
print (miles)
print (name)

## Numbers
a = b = c = 1
print (a, b, c)
del a
# print (a)

d, e, f = 1, 2, "Batman"
print (d, e, f)


## Strings
string = "I am Batman."

print (string)
print (string[0])
print (string[1])
print (string[2])
print (string[3:8])
print (string[2:])      # Prints string starting from 3rd character
print (string * 2)      # Prints string two times
print (string + "Do you Bleed?") # Prints concatenated string

## List
list = ["BatMobile", "BatCave", 219]
tinylist = ["Alfred"]
print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

## Tuple
tuple = ("BatMobile", "BatCave", 219)
print (tuple)            # Prints complete tuple
print (tuple[0])         # Prints first element of the tuple
print (tuple[1:3])       # Prints elements starting from 2nd till 3rd
print (tuple[2:])        # Prints elements starting from 3rd element
print (tuple * 2)        # Prints tuple two times
# print (tuple + "Alfred") # Prints concatenated tuple

## Dictionary
dict= {}
dict['one'] = "Bruce"
dict[2]     = "Wayne"

dictkv = {'firstName': 'Bruce', 'lastName': 'Wayne', 'DOB': 219}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (dictkv)          # Prints complete dictionary
print (dictkv.keys())   # Prints all the keys
print (dictkv.values()) # Prints all the values
