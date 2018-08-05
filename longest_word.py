# write a function that takes in a string of words
# return the longest word
# loop through string and find characters between spaces
# if character between space, append to list
# max_word = list[0]
# loop again and compare each index to max_num and replace if len is greater
# return max_num


def find_longest_word(string):
    """
    input: string of words
    output: longest words
    """
    word = ""    #use var to add characters until you run into a space
                 #or use .split() method
    result = []    #append word to result list

    for char in string:
        if char != " ":    #if char is not a space add the char to word string
            word += char
        else:               #if char is space do nothing except append word to list
            result.append(word)
            word = ""       #start word over as empty string

    max_word = result[0]    #save first item in list to compare other items in loop

    for word in result:
        if len(word) >= len(max_word):
            max_word = word

    return max_word

print find_longest_word("life is so awesome and cool.")
