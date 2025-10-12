def formate_name(first, last):
   if first == "" or last == "":
      return "You didn't provide valid inputs."
   print(first.title())
   print(last.title())
   return(f"{first.title()} {last.title()}")

input_first_name = input("What is your first name? ")
input_last_name = input("What is your last name? ")

output=formate_name(input_first_name, input_last_name)

print(output)