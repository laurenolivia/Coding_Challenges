#Write a function that takes two string args
#Return True if they are anagrams of the other, otherwise False

def is_anagram(s1,s2):
  s1 = s1.replace(" ", "").lower()
  s2 = s2.replace(" ", "").lower()

  compare_chars = {}

  #edge class
  if len(s1) != len(s2):
    return False

  #map chars to dict and count chars
  for char in s1:
    if char in compare_chars:
      compare_chars[char] +=1
    else:
      compare_chars[char] = 1
  
  #reduce dict char count for every char in s2
  for char in s2:
    if char in compare_chars:
      compare_chars[char] -= 1
    else:
      compare_chars[char] = 1

  #check if each value == 0
  for key in compare_chars:
    if compare_chars[key] != 0:
      return False

  return True    