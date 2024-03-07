def find_max_number(num_list):
    max_num = 0
    for number in num_list:
        if number > max_num:
            max_num = number
    return max_num

num = [1, 2, 3, 4, 2, 1, 2, 6, 7, 3, 4, 2]
print(find_max_number(num))

digits = [1,4,5,10,16,2,4,]
print(find_max_number(digits))
