delimiters = ["//", "," ,";" ,"\n"]

def split_string(s):
    for delimiter in delimiters:
        s = s.replace(delimiter, delimiters[0])
    filtered_list = [s for s in string_list if int(s) <= 1000]
    return s.split(delimiters[0])


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
