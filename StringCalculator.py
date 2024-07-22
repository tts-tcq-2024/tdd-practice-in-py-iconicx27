delimiters = ["//", "," ,";" ,"\n"]

def remove_all_greater_than_1000(lst):
    numbers = [int(num) for num in lst if int(num) <= 1000]
    return numbers

def split_string(str):
    for delimiter in delimiters:
        str = str.replace(delimiter, ' ')

    lst = str.split()
    
    filtered_list = remove_all_greater_than_1000(lst)
    return filtered_list

def add(numbers):
    if not numbers:
        return 0
    
    num_list = split_string(numbers)
    return sum(int(num) for num in num_list)
