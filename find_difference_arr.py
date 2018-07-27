# write a function that takes an array and returns the difference between max/min val
# exception: only search for min nums indexed before max_num
# exception: if all min nums are positioned behind max num return None
# exception: if max num is [0] return None
# exception: do not use any functions or methods 


array_of_nums = [10, 14, 9, 16, 4, 2, 16]

def find_difference(arr):
    # @param: takes i array of nums, returns difference between max/min

    max_num = arr[0]    #max_num starts at [0]
    min_num = arr[0]    #min_num starts at [0]

    difference = max_num - min_num

    for num in arr:
        if i >= max_num:    #if i is greater than max_num
            max_num = i     #update max_num
            difference = max_num - min_num      #recalculate difference
        #only calculate difference if max_num is updated
        #if min_num is updated BUT max_num is not, min_num is indexed behind max

        if i < min_num:     #if i is less than min
            min_num = i     #update min

    if max_num == arr[0]:   #if greatest val is [0], there cannot be a difference
        return None         #thus return None
    return difference 

print find_difference(array_of_nums)               



