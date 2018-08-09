# creating a function that simulates range() without using range()
# build function that takes 3 parameters: start,stop,step
# start_count = start
# end_count=stop
# increment_by = step
# create empty list to append values
# create while loop --> while start_count is < end_count continue to increment_by
# 1. append initial start value result 
# 2. add step to start and append to result.
# 3. repeat until start_count is greater than end_count THEN BREAK 

def find_range(start,stop,step):
  """
  input: 3 integers
  output: list of numbers with start/stop value, incremented by step
  """
  
  start_count = start
  end_count = stop
  increment_by = step
  result = []
  
  while start_count < end_count:
    result.append(start_count)
    start_count += increment_by
    
    
    
  print result
    
    
find_range(5,500,30)    


    
    
  