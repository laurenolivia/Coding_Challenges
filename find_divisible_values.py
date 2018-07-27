#write a program to search all nums between 2000 and 3200 (inclusive)
#return only nums divisible by 7
#but are not a multiple of 5
#between 2000 and 3200 (both included)
#print nums in a comma-separated sequence on a single line


def find_divisble_values():
    result = []

    for i in range(2000,3200 + 1):
        if i % 7 == 0 and i % 5 == 0:   #account for when i is a factor of 7 and 5
            pass
        if i % 7 == 0:                  #only print when i is a factor of 7
            result.append(i)

    return result

print find_divisble_values()
