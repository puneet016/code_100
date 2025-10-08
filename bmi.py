height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in kg: "))
bmi=weight/(height**2)
bmi_as_int=int(bmi)
print(bmi_as_int)
if bmi_as_int<18.5:
    print(f"Your bmi is {bmi_as_int}, you are underweight")
elif bmi_as_int<25:
    print(f"Your bmi is {bmi_as_int}, you have a normal weight")    
elif bmi_as_int<30:
    print(f"Your bmi is {bmi_as_int}, you are slightly overweight")
else:
    print(f"Your bmi is {bmi_as_int}, you are obese")