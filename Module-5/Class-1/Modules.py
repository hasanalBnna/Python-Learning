# pick up the whole
# import greetings

# greetings.say_hi()

# print(greetings.name)

#  import specific part
# from greetings import ( 
#     say_hi,
#     name,
# )
# say_hi()

# print(name)

# if u have .py file into a folder, u must tell the import (folder).(.py file) then import will understand which file u want.
# import ghorer_dim.expence

# ghorer_dim.expence.expence()

# if u have .py file into a folder, u must tell the import (folder).(.py file) then import will understand which file u want.
# import ghorer_dim.hatir_dim.nothing
# print(ghorer_dim.hatir_dim.nothing.a)

# use of init into a folder 
# import ghorer_dim
# print(ghorer_dim.hello)

# 
# import ghorer_dim
# ghorer_dim.expence()

# 
# import math
# n = 25
# res = math.sqrt(n)
# print(res)

# datetime module
# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now().strftime('%d-%m-%y'))

# # random module
# import random
# print(random.randint(4,20))

#  python -m pip install requests
import requests

res = requests.get("https://google.com")
print(res.text)

