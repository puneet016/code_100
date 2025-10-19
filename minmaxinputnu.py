def check_for_float(p_num):
    try:
        val=float(p_num)
        return val
    except(valueError,TypeError):
        print("Error.please enter numeric input")
        return False
input1=input("Enter a number: ")
if input1=="done":
  quit()
number=check_for_float(input1)
if not number:
   print("The first enterd has to be number to continue..")
smallest=number
biggest=number
while True:
    input1=input("Enter a number: ")
    if input1=="done":
        break
    number=check_for_float(input1)
    if number >biggest:
        biggest=number
    if number <smallest:
        smallest=number
print(f"Minimum is {smallest}")
print(f"Maximum is{biggest}")
