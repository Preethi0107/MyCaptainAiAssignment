num = int(input("Enter a number:"))
n1, n2 = 0, 1
sum = 0
for i in range(0, num):
    print(sum)
    n1 = n2
    n2 = sum
    sum = n1 + n2
