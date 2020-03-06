def getCount(inputStr):
    num_vowels = 0
    # your code here
    vowels = 'aeiou'
    count = {}.fromkeys(vowels,0)


    for char in inputStr:
        if char in count:
            count[char] += 1
            num_vowels += 1
    count.values()
    num_vowels = sum(count)
    print(num_vowels)
    return num_vowels


