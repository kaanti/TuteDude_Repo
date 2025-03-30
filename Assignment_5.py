# Task 1

marks_dict = {'Alice': 85}

name = input("Enter student's mame:")

if name in marks_dict:
    print(f"{name}'s marks:",marks_dict[name])

else:
    print('Student not found')


# Task 2

l = list(range(1,11))
l1 = l[:5]
l2 = list(reversed(l1))
print('Original list:', l)
print('Extracted first five elements:', l1)
print('Reversed extracted numbers:', l2)