def check_for_float(p_num):
    try:
        val=float(p_num)
        return val
    except(valueError,TypeError):
        print("Error.please enter numeric input")
        return False
   
count=0
total=0.0
average=0.0
while True:
    input_number=input("Enter a number: ")
    if input_number=="done":
    
     break
    number =check_for_float(input_number)
    if not number:
        continue
   
    count+=1
    total=total_input_number
    average=total/count
    print(total,count,average)

