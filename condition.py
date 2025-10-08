#boolean
print(1 == 1)
print(type (1==1))

#conditional statements
salary=int(input("Enter your salary:\n"))
if salary>=2000:
    print("you are elegible for mortage")
    credit_score=int(input("Enter your credit score:\n"))
    if credit_score>800:
        rate=4
        print("Interest rate is 4%")
    elif credit_score>750:
        rate=6
        print("Interest rate is 6%")
    else:
        rate=8
        print("Interest rate is 8%")
    disability=input("Do you have disability? Yes or No\n")
    if disability=="Yes":
        rate-=2
        print(f"Your interest rate is {rate}%")
else:
    print("you are not elegible for mortage")
    

 
