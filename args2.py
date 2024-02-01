def add(*numbers_to_add):
    added = 0
    for number in numbers_to_add:
        added += number
    return added
print(add(1, 2, 3, 4, 5))


# Here sum() is a built-in function
def add(*numbers_to_add):
    return sum(numbers_to_add)
print(add(1, 2, 3, 4, 5))
