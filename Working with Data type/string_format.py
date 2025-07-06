a = "Good morning, Karim. How are you?"

user_input = input("Whats your Name?\n")
b = "Good morning {}, How are you? \ni am {}".format(user_input,"fine")
print(user_input)
print(b)
c = "i am also {}".format("fine")
print(c)
print("Can you tell me whats your first name?")
F_name = input("Yes,my fname is : ")
print("Can you tell me whats your last name?")
L_name = input("Yes,my lname is : ")
print("may i know your age, please?")
age = input("Yes,my age is : ")
#user_input =input("What is your name?")
d ="my name is {fname} {lname} \ni am {ag} years old".format(fname=F_name,ag=age,lname=L_name)
print(d)
e = f"my name is {F_name} {L_name} and i am {age} years old"
print(e)

