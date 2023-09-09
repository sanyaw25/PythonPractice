print("Hello World"); print("I am such a hardworker")
pi = 3.14; radius=2; print("value of pi is 3.14 and radius is 2")
area = pi*(radius**2); print("value of area is given by pi(r)^2") # area of a circle
print(area)
radius = radius+2; print(radius); print("value of new radius"); print(area)
print("no change to area unless we run the command again") # area doesn't change
area = pi*(radius**2); print("value of new area"); print(area)
this_is_a_variable=0; this_is_a_variable=1; print(this_is_a_variable)
#strings
hi='greetings'; name='san'; greet=hi +" "+name; print(greet)
silly= (hi+ " ")*3 + name; print(silly)
#output 
x=1; print(x); x_str= str(x)
print("my fav number is", x,".","x =", x_str)
#unnecessary spacing-use + for no spacing
print("my fav number is",x_str+ "."+" "+"x =", x_str)
# input #multiplication and to repeat a chain of words
print("get your word repeated 5 times, type a word and hit enter")
text=input('type anything...'); print(5*(text+" "))
print("get your number multiplied by 5, type a number and hit enter")
num=float(input('type a number...')); print(5*num)
#conditionals
print('comparing the two numbers')
x=float(input('type the 1st number...')); y=float(input('type the 2nd number...')) 
if x==y:
    print("x and y are equal")
    print('thanks for playing') 
    if y!=0: print('therefore, x compared to y is', x/y) 
elif x<y: print ('1st number is smaller')
elif x>y: print('2nd number is smaller')
print ('thanks for playing')
#remainder
num=float(input('type a number...'))
if num%2 ==0:
    print("number is even") 
else: 
    print("number is odd")