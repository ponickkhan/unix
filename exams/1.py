file = open('test.txt', 'r')
Lines = file.readlines()
for line in Lines:
    if 'java'.lower() in line.lower():
     print("{}".format(line.strip()))