'''
file1 = open("my file.txt","w")
writing_file = file1.write('Atul Raj ')
print(writing_file)
file1.close()

file1 = open("my file.txt","r")
reading_file = file1.read()
print(reading_file)
file1.close()

file1 = open("my file.txt","a")
appending_file = file1.write('hello world')
print(appending_file)
file1.close()

file1 = open("my file.txt","r")
reading_file = file1.read()
print(reading_file)
file1.close()
'''
# r+ ---- > read and write

file1 = open("my file.txt","r+")
writing_file = file1.write('Atul Raj ')
print(writing_file)
file1.close()

file1 = open("my file.txt","r+")
reading_file = file1.read()
print(reading_file)
file1.close()