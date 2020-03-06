def getCount(inputStr):
    num_vowels = 0
    # your code here
    vowels = 'aeiou'  #Set dictionary of vowels for the test
    count = {}.fromkeys(vowels,0)  #Make a dictionary with each vowel a key and value 0
    for char in inputStr:  #Count the vowels
        if char in count:
            num_vowels += 1
    print(num_vowels)
    return num_vowels
