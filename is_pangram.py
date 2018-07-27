def is_pangram(str):
  """
  input: string 
  output: True False if pangram 
  """
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  
  for char in alphabet:
    if char not in str:
      return False
  
  return True
  
is_pangram('The quick brown fox jumps over the lazy dog.')  



import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
    
is_pangram("The quick brown fox jumps over the lazy dog.")    