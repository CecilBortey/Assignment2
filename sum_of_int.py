count = 0
num = int(input("Enter number: "))
sum = num
while num > 0:
    num = int(input("Enter number: "))
    if num < 0:
        break
    count = count + 1
    sum = sum + num
print("the sum of all positive numbers entered =", sum)