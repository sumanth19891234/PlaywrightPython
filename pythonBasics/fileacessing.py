file = open("sample.txt")

print(file)


#read line by line
print(file.readline())
print(file.readline())
print(file.readline())

print("################################")

#read entrire content
print(file.read())

#read upto given number of letters
print(file.read(5))


#read line by line
print(file.readline())

file.close()

