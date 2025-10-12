year=int(input("Enter a year:\n"))
def leapyear(p_year):
     
 
 
 
    if p_year%4==0:
        if p_year%100==0:
            if p_year%400==0:
                print(" is a leap year")
            else:
                print(" is not a leap year")
        else:
            print(f"is a leap year")
    else:
        print(f" is not a leap year")
leapyear(year)