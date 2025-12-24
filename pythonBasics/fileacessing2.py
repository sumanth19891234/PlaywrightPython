file = open("sample.txt")

# print(file)
#
# line= file.readline()
#
# while line!="":
#     print(line)
#     line= file.readline()

a= file.readlines()

print(a)

for i in a:
    print(i)

cleaned_list = [item.strip() for item in a if item.strip()]

print(cleaned_list)

for j in a:
    print(j)
