"""
#immutable data type
-integer
-float
-string
-tuple
-frozen set
"""
a = 10
first_location = id(a)
a = 20
second_location = id(a)

print(first_location)
print(second_location)
