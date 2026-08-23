n = int(input())

a = 0
b = 1
while True:
    if n == 0:
        break
    print(a)
    a,b = b, a + b
    n -= 1
