def reverse(s) :
  if len(s) == 0:
    return s
  else :
    return reverse(s[1 :]) + s[0]
s = "1234abcd" 
print("output :" , end="")
print(reverse(s))            