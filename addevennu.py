def add_even_numbers(start, end):
    # TODO
    total=0
    for number in range(start,end+1):
        if number % 2==0:
          total+=number
       
    return total
print(add_even_numbers(1,100))