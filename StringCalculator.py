def add(numbers):
    if numbers == "":
        return 0
    elif numbers == "0":
        return 0
    else:
        num_list = numbers.split(",")
        ans=0
        for num in num_list:
            ans+=int(num)
        return ans
