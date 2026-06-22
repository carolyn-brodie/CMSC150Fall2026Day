list1 = [1, 3, 5, 6, 7]
total = 0

# for number in list1:
#     total += number
# print(total)

for number in list1:
    if number % 2 == 1:
        total += number

print(total)