# Try range
# print(range(10))
# print(list(range(10)))


# lst = [1,2,3,4,5,6,7,8,9,10]
#
# for item in lst:
#     print("hi")

# for number in range(10):
#     print("hi")

# for number in range(1,11):
#     print(number, end = " ")
# print()
#
# for number in range(10):
#     print(number + 1, end = " ")

## add up all the even numbers between 10 and 100
# total = 0
# for num in range(10, 101):
#     if num % 2 == 0:
#         total += num
#
# print(total)
#
# total = 0
# for num in range(10, 101,2):
#     total += num
#
# print(total)

## add square of numbers between 1 and 10
# total = 0
# for number in range(1, 11):
#     total += number ** 2
# print(total)


## Build lists
print(list(range(1, 100, 2)) + list(range(97, 0, -2)))

my_list = []
for number in range(1,100,2):
    my_list.append(number)
for number in range(97,0, -2):
    my_list.append(number)
print(my_list)


# print(list(range(3,8,2)))

# for count in range(1,11):
#     if count == 5:
#         print("bye")
#     else:
#         print("hi")