with open("sample.txt","r") as reader:
    list=reader.readlines()
    print(list)
    print(reversed(list))
    print(list)
    with open("sample.txt","w") as writer:
        for line in reversed(list):
            writer.write(line)
