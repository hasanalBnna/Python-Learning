# import datetime
# print(datetime.datetime.now())

# from datetime import datetime,time,date
# current=date.today().year
# print(current)

# from datetime import datetime,time,date
# ##curr= datetime.now().time().minute
# curr= datetime.now().date()
# print(curr)

from datetime import datetime, timedelta
dt= datetime(
    year=2023,
    month=10,
    day=1,
    hour=12,
    minute=30,
    second=45,
)

# print(dt)

cuur = datetime.now()
diff = cuur - dt
print(diff)

print(type(diff)) #timedelta