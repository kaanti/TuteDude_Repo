# Task 1

num = int(input('Enter a number:'))

if num%2 == 0 :
    print(num, 'is an even number.')
else:
    print(num, 'is an odd number.')

# Task 2

total = 0
for n in range(1, 51):
    total += n
print('The sum of numbers 1 to 50 is:', total)
