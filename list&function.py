list=[10,15,20,35,40,55,60]
print(max(list))
print(min(list))
print(sum(list))
print(len(list))    
print(sorted(list))
print(sorted(list,reverse=True))
print(list.count(10))
print(list.index(35))
list.append(70)
print(list)
list.insert(2,25)
print(list)
list.remove(15)
print(list)



numlist=[5,2,9,1,5,6]
while True:
    inp=input("Enter a number:")
    if inp=='done':
        break
    value=int(inp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print('Average:',average)
