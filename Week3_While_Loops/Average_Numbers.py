## Compute average:

count = 0
total = 0
done = False

while not done:    ## while done == False:
    number_string = input("Enter an integer or enter to quit: ")
    if number_string == "":
        done = True
    else:
        number = int(number_string)
        total += number
        count += 1
if count == 0:
    print("average = 0")
else:
    print(f"average = {total / count}")

