data="from example.email@edu.co.uk sat 12 jun 2021 10:00:00 -0700"
at_index=data.find("@")
print(at_index)
space_index=data.find(" ",at_index)
print(space_index)
domain=data[at_index+1:space_index]
print(domain)

my_string="Hello World. Welcome to Python Programming."
output=my_string.split()
print(output)
join_back=" ".join(output)
print(join_back)