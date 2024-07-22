delimiters = ["//", "," ,";" ,"\n"]

def remove_all_greater_than_1000(lst):
    numbers = [int(num) for num in lst if num.strip().isdigit() and int(num) <= 1000]
    return numbers

def split_string(str):
    for delimiter in delimiters:
        str = str.replace(delimiter, ' ')

    lst = input_string.split()
    
    filtered_list = remove_all_greater_than_1000(lst)
    return filtered_list


# def remove_delimiters(input_string):
#     for delimiter in delimiters:
#         input_string = input_string.replace(delimiter, '')

#     input_string=input_string.
    
#     return input_string

def add(numbers):
    if not numbers:
        return 0
    
    num_list = split_string(numbers)
    return sum(int(num) for num in num_list)
