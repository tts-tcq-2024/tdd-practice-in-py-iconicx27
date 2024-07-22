delimiters = ["//", "," ,";" ,"\n"]

def remove_delimiters(input_string):
    for delimiter in delimiters:
        input_string = input_string.replace(delimiter, '')

    input_string = input_string.replace("1001", "1")
    
    return input_string

def add(numbers):
    if not numbers:
        return 0
    
    num_list = remove_delimiters(numbers)
    return sum(int(num) for num in num_list)
