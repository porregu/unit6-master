def add_numbers(nums):
    total=0
    for x in nums:
        total = x+ total
    return total
print(add_numbers([1, 2, 3, 4, 5, 6,100,123])," this is the toalt sum of the list ")