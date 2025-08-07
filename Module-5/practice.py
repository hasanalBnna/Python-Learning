# for x in range(5):
#     for y in range(1, 10):
#         print(y, end=" ")
#     print()
# -----------------------------
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter number of symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()
