x= int(input("type in the number of rows you want "))
for i in range(1, x):
    for j in range(1, x- i - 1):
        print( " ", "*", end="  ")
    for j in range(0, i+1):
        print( "*", end="  ")
    print()
