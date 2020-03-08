# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    newList = list(str(num)) # Make num a string and then a list
    newList.sort(reverse = True) # Sort the list and reverse
    num = int("".join(newList)) # Join the list with no spaces as string and make it int

    return num