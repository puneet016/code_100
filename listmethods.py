#index
animal=['doh','cat','bat','rat']
index=animal.index('bat')
print(index)

animal=['doh','cat','bat','rat','bat']
index=animal.index('bat',3,5)
print(index)


#Append Method
animal=['dog','cat','bat']
animal.append('rat')
print(animal)

#Extend Method
animal=['dog','cat','bat']
animal.extend(['rat','elephant'])
print(animal)
#Insert Method
animal=['dog','cat','bat']
animal.insert(1,'rat')
print(animal)

#Remove Method
animal=['dog','cat','bat']
animal.remove('cat')
print(animal)

#Pop Method
animal=['dog','cat','bat']
animal.pop(1)
print(animal)

#Clear Method
animal=['dog','cat','bat']
animal.clear()
print(animal)

#Sort Method
animal=['dog','cat','bat']
animal.sort()
print(animal)

#Reverse Method
animal=['dog','cat','bat']
animal.reverse()
print(animal)

#Copy Method
animal=['dog','cat','bat']
animal1=animal.copy()
print(animal1)      
#Count Method
animal=['dog','cat','bat','dog']    
count=animal.count('dog')
print(count)
#Join Method
animal=['dog','cat','bat']
result=' '.join(animal) 
print(result)
#Split Method
text="dog cat bat"
result=text.split()
print(result)   
#Length Method
animal=['dog','cat','bat']
length=len(animal)
print(length)
