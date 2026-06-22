#Write a program to compute the average of numbers entered by the user.
#The number of numbers is not known ahead of time.


#option 1
total = 0
count = 0
done = False
while done == False:
    numberStr = input("Enter a number (Press enter to quit): ")
    if numberStr == "":
        done = True
    else:
        number = float(numberStr)
        total += number
        count += 1

average = total / count

print(f"The average is {average}")
