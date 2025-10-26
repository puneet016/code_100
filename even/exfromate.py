custom_string='X-MAPDS-Confidence:0.8475'
index-col=custom_string.find(':')
number=custom_string[index_col+1:]
number=float(number)
print(index_col)
print(number)