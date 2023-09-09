#for loops
for n in range(5): print ("good") #rounding off
sum=0
for i in range(10): sum+=i; print(sum)
for i in range(7,10):sum+=i; print(sum)
sum=0 
for i in range(5,11,2):
 sum+=i
 if sum==10:
   break 
 sum +=0
print(sum)

#calculation of square roots
ans=0; neg_flag=False; x=int(input('enter an integer:'))
if x<0: neg_flag=True
while ans**2<x:
 ans=ans+1
 if ans**2==x: print('square root of', x,'is', ans)
 elif ans**2>x: print(x, 'is not a perfect square')
if neg_flag:print('just checking...did you mean',-x,'?')
if x<0: print(-(x**2), 'is the imaginary perfect square but is not possible because pefect squares are always positive. ')