#while loops
n= input("You are lost in a maze\n*****************\n*****************\n:)\n*****************\n*****************\nGo left or right \n")
if n=="left" or n=="Left": print("you got out of the forest!")
while n=="right" or n=="Right":
 n=input("*****************\n*****************\n    :)\n*****************\n*****************\nyou are still stuck in the forest, choose again \n")
 if n=="left" or n=="Left": print("you got out of the forest!"); break
 set_counter=2; n=input("*****************\n*****************\n       :(\n*****************\n*****************\nchoose again \n")
 if n=="left" or n=="Left": print("you got out of the forest!"); break
 set_counter=3; n=input("*****************\n*****************\n          :( \n*****************\n*****************\nyou seem to be terribly lost! Choose again \n")
 if n=="left" or n=="Left": print("you got out of the forest!"); break
 set_counter=4; n=input("*****************\n*****************\n              :( *****\n*****************\n*****************\nyour path is obstructed by trees, choose again \n")
 if n=="left" or n=="Left": print("you got out of the forest!"); break
 set_counter=5; print(":( died of starvation, guess you couldn't get out in time..."); break
 if n=="left" or n=="Left": print("you got out of the forest!"); break
