# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()

# a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100

for i in range(0, 110, 10):
    print(i, end=" ")

# b. count down from 20 to 1:

for i in range(20, 0, -1) :
    print(i, end=" ")

# c. print a number of stars.

number_of_stars = int(input("Enter the number of stars:"))
i = number_of_stars
for i in range(i, 0, -1):
    print("*", end="")

# d. print lines of increasing stars.

star_lines = int(input("Enter the number of star lines:"))
i = star_lines
for i in range(1, i+1):
        print("*" * i)
