# build function that prints numbers 1 to 100
# while num is less than 101
# count = 1; count += 1 
# if num % 3 == 0 print "Fizz"
# if num % 5 == 0 print "Buzz"
# if num % 3 == 0 and num % 5 == 0 print "FizzBuzz"

def solve_fizzbuzz():
  """
  input: count = 1; count += 1 
  output: return num 1 to 100 unless divisible by 3,5,3and5
  """
  count = 0
  
  while count < 100:
    count +=1
    
    if count % 3 == 0 and count % 5 == 0:
      print "FizzBuzz"
    elif count % 3 == 0:
      print "Fizz"
    elif count % 5 == 0:
      print "Buzz"
    else:
      print count
         
    
solve_fizzbuzz()
  
  