My_Name_is= "Snake"
myVeriableName = "camel"
MyVariableName = "Pascal"

v, w, x,y,z = "first","second","third","fourth","fifth"
print(z)

s = t = u = "3rd"
print(u)

fruits = ["apple","banana","cherry"]
j, k, l = fruits
print(fruits)
print(j)

m = "python"
n = "is"
o = "great"
print(m,n,o)

p = "python "
p2 = "is "
r = "great"
print(p+p2+r)# need add space in string when u use + operator

a1 = 5
b1 = "Banna"
print(a1,b1)

# Global veriable
def myfuc():
    print("My Name is " + b1)
    print("I love ", fruits)

myfuc()

#local and Global veriable
c1 = "Good" #Global

def test():
    c1 = "Awasome" #local
    print("Python is ",c1) #local

test()
print("Python was",c1) #Global

# global keyword
d1 = "fantastic"

def mytest():
    global d1
    d1 = "Awasome"
mytest()
print(d1)