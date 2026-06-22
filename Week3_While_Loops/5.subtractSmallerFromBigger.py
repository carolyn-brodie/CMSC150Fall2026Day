##Write a program that inputs 2 integers, repeatedly subtracts the
##smaller from the larger until the result is smaller than the smaller one,
##and displays the number of subtractions.

# Input integer1 and integer2.
# 		Make sure integer1 is the bigger number.
# 		While integer1 >= integer2
# 			Subtract integer2 from integer1
# 			Increase counter by 1
# 		Display counter


integer1 = int(input("Enter the first number: "))
integer2 = int(input("Enter the second number: "))
count = 0

integer1 = abs(integer1)
integer2 = abs(integer2)

if integer1 < integer2:
    temp = integer1
    integer1 = integer2
    integer2 = temp

while integer1 >= integer2:
    # if integer2 < 0:
    #     integer1 = integer1 + integer2
    # else:
    integer1 = integer1 - integer2
    count += 1

print(count)


#       Another method

integer1 = abs(int(input("Enter an integer: ")))
integer2 = abs(int(input("Enter another integer: ")))
counter = 0
if integer2 > integer1:
    temp = integer1
    integer1 = integer2
    integer2 = temp
while integer1 >= integer2:
    integer1 -= integer2
    counter += 1
print(counter)






    

