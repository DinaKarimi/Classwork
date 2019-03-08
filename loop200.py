#1
for lo in range(10):
    print('hello')

#2
for num in range(101):
    if num % 3==0:
        print(num)
#or
for num in range(3, 100, 3):
    print(num)

#3)
total=0
for add in range(1, 11):
    total += add
print(f'the total is:{total}')
