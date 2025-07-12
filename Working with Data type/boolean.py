# boolean data type
MyName =True
MyName =False
print(MyName)

#none data type

taka = None
print(taka)

#mapping(dicsionary data type)

person={
    'first_name':'kazi',
    'last_name':'Banna',
    'age':26,
    'isBangladeshi':True
}

print(person['first_name'])
print(person)

#set deta type -mutable
myset = {"me","my","he","my","me",2,3,5,3,2} #avoid duplicate value
print(myset)



#frozen data type- immutable

myfrize =frozenset({"me","my","he","my","me",2,3,5,3,2})
print(myfrize)