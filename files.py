# l="my name is Sanya Wadhawan"
# f= open("myfile.txt",'w')
# f.write(l)
# f.close()

# f=open("myfile.txt", 'r')
# l=f.read()
# vowels=["a" ,"e","i","o","u"]
# count=0
# for i in range (l):
#     if i in vowels:
#         count+=1
#     else: 
#         i+=1

# f.close()
s="My name is Sanya.\n I am a student.\n I am 17 years old.\n"
hi=open("myfile1.txt","w")
hi.write(s)
hi.close()


hi=open("myfile1.txt","r")
s = hi.read()
vowel = 0
line = 0
character = 0
vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in s:
        if i in vowels_list:
            vowel += 1
        elif i not in vowels_list and i != "\n":
            character += 1
        elif i == "\n":
            line += 1

print("Number of vowels is = ", vowel)
print("New Lines = ", line)
print("Number of characters is = ", character)
hi.close()
  
