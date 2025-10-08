try:
    salary=int(input("Enter your salary:\n"))
except :
    print("Ther was an error in input")
else:
    if salary>2000:
        print("you are elegible for mortage")
    else:
        print("you are not elegible for mortage")
finally:
    print("Thank you for using our service")


    
