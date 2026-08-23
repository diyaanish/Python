n = int(input())

a = 0
b = 1

while n > 0:
  if a != 0 and a != 1:
    for i in range(2,a):
      if a % i == 0:
        break
    else:
      print(a)
      n -= 1
  a,b = b,a+b
