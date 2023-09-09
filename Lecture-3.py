#perfect cube-(guess and check method)
cube=int(input('enter an integer:'))
for ans in range(abs(cube)+1): 
 if ans**3>=abs(cube):
     break
if ans**3!=abs(cube): print(cube, 'is not a perfect cube')
else :
  if cube<0:
      ans=-ans 
  print('cube root of', cube, 'is', ans)
 
#approximation method
cube = int(input('type in an integer-'))
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
   guess += increment
   num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
   print('Failed on cube root of', cube, "with these parameters.")
else:
   print(guess, 'is close to the cube root of', cube)

# bisection cube root
cube =float(input('type any number and find its cube root...'))
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
   if guess**3 < cube:
       low = guess
   elif cube<1 : low=cube; high=1
   elif cube>-1 and cube<0: low=0; high=cube
   else:
       high = guess
   guess = (high + low)/2.0
   num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
 