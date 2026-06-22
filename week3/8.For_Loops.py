## Loop through elements in a list
## remember that in print(whatever, end = " ") the end = " " replaces a new line with a space
for item in [1, 2, 3]:
    print(item, end = " ")

print()  ## Just print a blank line with a new line character

## Loop through characters in a string
for letter in "word":
    print(letter, end = " ")

print()

## Variables can be used as well
list1 = ["A", "B","C"]
for element in list1:
    print(element, end = " ")
