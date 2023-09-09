# d= {}
# s = "my name is sanya wadhawan"
# for i in s:
#         if i in d:
#             d[i]=d[i]+1
#         else: 
#             d[i]=1
# print (d)

for i in range(0, 3):
	for j in range(0, 3-i-1):
		print(end=" ")
	for j in range(0, i+1):
		print("*", end=" ")
	print()
 
 
rows= 4
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, " ", end="   ")
    for j in range(i - 1, 0, -1):
        print( j," ", end="   ")
    print()


rows=5
i = 1
while i <= rows:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i += 1

i = rows - 1
while i >= 1:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k <= 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i -= 1
    