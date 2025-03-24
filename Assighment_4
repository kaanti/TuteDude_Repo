# Task 1

try:

    file = open('/home/kaanti/learn/tutedude_assignments/sample.txt', 'r+')
    text = file.write('This is a sample text file.')
    file.close()

    file = open('/home/kaanti/learn/tutedude_assignments/sample.txt', 'r+')
    text = file.read()
    print('Reading file content:')
    print('Line 1:', text)
    file.close()

    file = open('/home/kaanti/learn/tutedude_assignments/sample.txt', 'r+')
    text = file.write('It contains multiple lines.')
    file.close()

    file = open('/home/kaanti/learn/tutedude_assignments/sample.txt', 'r+')
    text = file.read()
    print('Line 2:', text)
    file.close()


except FileNotFoundError:
    print('Error: The file sample.txt not found')


# Task 2

file = open('/home/kaanti/learn/tutedude_assignments/output.txt', 'a+')
text = file.write(input('Enter text to write to the file:')+"\n")
print('Data successfully written to output.txt.')
file.close()

file = open('/home/kaanti/learn/tutedude_assignments/output.txt', 'a+')
text = file.write(input('Enter additional text to append:'))
print('Data successfully appended.')
file.close()

file = open('/home/kaanti/learn/tutedude_assignments/output.txt', 'r')
print('final content of output.txt.')
text = file.read()
print(text)
file.close()


