# given a list
# write function with two param (list, item)
# return true if item in list
# return false if item not in list
# exception: cannot use "in"

search_lst = ['hello', 'world', '1', 11, 'magic']

def search_lst(lst, item):
    # @param: takes in list and item of any object type
    # @notice: cannot use "in" to search list
    # return: true if item in list, else false
    index = 0

    for i in lst:
        if lst[index] != item:
            index += 1
            continue
        else:
            return True
    return False

print search_lst(a_list, 'happy')


