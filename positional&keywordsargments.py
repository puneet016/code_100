#def greet_with_location(name, location):
    #print(f"Hello, {name}!")
    #print(f"How is the weather in {location}?")
#greet_with_location("Alice", "New York")
#greet_with_location("Bob", "Paris")



import math
def calculate_can_number(height,width,coverage):
    area = height * width
    number_of_cans = math.ceil(area / coverage)
    print(number_of_cans)

input_height = int(input("Height of wall: "))
input_width = int(input("Width of wall: "))
coverage = 4
calculate_can_number(height=input_height, width=input_width, coverage=coverage)