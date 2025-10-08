print("Welcom to berger shop")
size=input("What size of burger do you want? M, N or L\n")
add_mushroom=input("Do you want mushroom? Y or N\n")
add_cheese=input("Do you want cheese? Y or N\n")
bill=0
if size=="M":
    bill+=5
elif size=="N":
    bill+=8
elif size == "L":
    bill+=10
if add_mushroom=="Y":
   if size=="L":
       bill+=2
   else:
       bill+=1
if add_cheese=="Y":
    bill+=1
print(f"Your final bill is {bill}")

