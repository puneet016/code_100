names=['john','doe','alice','bob']
scores=[85,92,78,90]
print("{0:<10} {1:<5}".format("Name","Score"))
for index in range(len(names)):
    name=names[index]
    score=scores[index]
    print("{0:<10} {1:<5}".format(name,score))

 