height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in kg: "))
bmi=round(weight/height**2,2)
#bmi=(height**2)
#bmi_as_int=int(bmi)
#print(bmi_as_int)
if bmi<18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi<25:
    print(f"Your bmi is {bmi}, you have a normal weight")    
elif bmi<30:
    print(f"Your bmi is {bmi}, you are slightly overweight")
else:
    print(f"Your bmi is {bmi}, you are obese")