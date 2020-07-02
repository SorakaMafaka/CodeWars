#This time no story, no theory. The examples below show you how to write function accum.

#Examples:

#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"
#The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(s):
    f = []
    for counter , letter in enumerate(s,1): #Has to start at index 1, otherwise doesn't print the first letter because of index 0
        f.append(counter * letter)
    x = "-".join(f)
    return x.title() #Easy way of making every "word" start with capital letter

