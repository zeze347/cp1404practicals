#1.
name = input("Enter your name: ")
filename = "name.txt"
out_file = open(filename, "w")
out_file.write(name)
out_file.close()
# #2.
in_file = open(filename)
name = in_file.readline()
print(name)
in_file.close()
# 3.
with open("numbers.txt","r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)
# 4.
number_of_line = 0
with open("numbers.txt","r") as in_file:
    for line in in_file:
        number_of_line += 1
    print(number_of_line)