hour=input("Enter hours:\n")
try:
    hour=float(hour)
    
except:
    print("Error, please enter numeric input")
    quit()
rate=input("Enter rate:\n")
try:
    hour=float(hour)
    rate=float(rate)
except:
    print("Error, please enter numeric input")
    quit()
    
if hour<40:
    grosspay=(hour*rate,2)
else:
    overtime=hour-40
    grosspay=round(40*rate+overtime*rate*1.5,2)
print(f"Your gross pay is {grosspay}")