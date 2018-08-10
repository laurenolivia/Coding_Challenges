#create a loop that compares one int to the next 
#start at [0]
#if [0] == [1], append [0] to new list
# if [1] == [2] append [1] to new list
# and so forth (only consecutives integers append to new list)
# sum all values that were appended to new list
#ex: if you printed the integers that should all be summed, it would be 6+7+8+8

a = [1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8]


def sum_consecutives(lst):
  """
  input: list of int
  output: return list of consecutive ints
  """
  index = 0
  result = []
  while index < len(lst)-1:
    if a[index] == a[index+1]:
      result.append(a[index])
    index += 1
  sum_result = sum(result)
  
  return result, sum_result
    
print sum_consecutives(a) 