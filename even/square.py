def square(p_list):
    for index in range(len(p_list)):
        p_list[index] = p_list[index] ** 2
    return p_list
custom_list = [1, 2, 3, 4, 5]
print(square(custom_list))