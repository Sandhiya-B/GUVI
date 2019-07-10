num = int(input())
x = num%2
if num > 0 and  x == 1:
  print("Odd")
elif num > 0 and  x == 0:
  print("Even")
else:
  print("Invalid")
