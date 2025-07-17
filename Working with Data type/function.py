# def make_tea():
#     print("1. Boil water")
#     print("2. Add tea leaves")
#     print("3. pour into cup")
#     print("4. Add milk and suger")
#     print("5. stir well")
#     print("6. Tea is ready")


# print("YO, Good Morning")
# make_tea() # function call

# print("nice, make it again.")

# make_tea()
# make_tea()
# make_tea()

#perameter/argument
# def calculate_suare():
#     a = 5

#     print(a * a)

# calculate_suare()
# calculate_suare()
# calculate_suare()

#-----------

# def calculate_suare(n):

#     print(n * n)

# calculate_suare(7)
# calculate_suare(3)
# calculate_suare(12)
#--------------
# def make_tea(tea_type):
#     print(f"Making {tea_type} tea")

# make_tea("Green")
# make_tea("Milk")
# make_tea("Masala ")
#----------------
# def calculate_suare(n): #perameter
#     res = n * n
#     return res

# x = calculate_suare(7) # argument

# print(f"the result is: {x}")
#--------
# def calculate_suare(n): #perameter
#     res = n * n
#     # return res

# calculate_suare(7)

# print(f"the result is: {res}")
#-----------------
# a = 5
# b = 7

# def hi():
#     x = 5

# hi()
#--------------
# def hi():
#     print("hi")

# def welcome():
#     hi()
#     print("welcome to my world")

# welcome()
#-------------

# def hi():
#     a = 5
#     print("hi")
#     return a

# def welcome():
#     b = hi()
#     print(b)
#     print("welcome to my world")

# welcome()
#-----------
# def welcome():
#     b = hi()
#     print(b)
#     print("welcome to my world")

# abc = welcome()
# print(abc)
#----------
# def welcome():
#     b = hi()
#     print(b)
#     print("welcome to my world")
#     return "wow, nice"

# abc = welcome()
# print(abc)
#----------
# def welcome():
#     b = hi()
#     print(b)
#     print("welcome to my world")
#     return "wow, nice"

# abc = welcome
# print(abc)
#-------
# def welcome():
#     b = hi()
#     print(b)
#     print("welcome to my world")
#     return "wow, nice"

# abc = welcome
# abc()
#-----------------
# def welcome():
#     b = hi()
#     print(b)
#     print("welcome to my world")
#     return "wow, nice"

# abc = welcome

# def execute_the_func(the_function):
#     the_function()

# execute_the_func(hi)
#-----------
# def welcome():
#     b = hi()
#     print(b)
#     print("welcome to my world")
#     return "wow, nice"

# abc = welcome

# def execute_the_func(the_function):
#     the_function()

# execute_the_func(hi)
#------------
#lamda function
# def sum_of_two(a,b):
#     return a + b
# res = sum_of_two(10,20)
# print(res)
# #----
# sum_of_two=lambda a, b: a + b
# res = sum_of_two(10,20)
# print(res)

#---------
# x = 6
# def sum_of_two(a,b):
#     s = a + b
#     print(x)
#     return s
# sum_of_two(10,20)
# print(s)
#---------
# x = 6
# def sum_of_two(a,b):
#     s = a + b
#     x=20
#     print("inside:",x)
#     return s
# sum_of_two(10,20)
# print("outside:",x)
#-----------
# x = 6
# def sum_of_two(a,b):
#     s = a + b
#     global x
#     x=20
#     print("inside:",x)
#     return s
# sum_of_two(10,20)
# print("outside:",x)

#------------------
#interator
# fruits = ["apple","mango","Banana"]
# fruite_iter = iter(fruits)
# print(next(fruite_iter))

#----------
#generator
# def hi():
#     yield "hi"
#     yield "wassup"
#     yield "Great"

# for text in hi():
#     print(text)
#---------
def pet_generator():
    pets = ["fluffy", "spike","Luna"]
    for pet in pets:
        yield f"{pet} is ready for adoption"

for message in pet_generator():
    print(message)
