
list1 = [10, 20, 30, 40]
list2 = []
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])

# for element in list1:
#     print(element, end = " ")
#
# print("loop finished")

list1 = [10, -20, 30, 40, -1, 2]
positives = 0
negatives = 0
for number in list1:
    if number >= 0:
        # positives += number
        positives += 1
    else:
        # negatives = negatives + number
        negatives += 1

print(positives)
print(negatives)
#print("The loop is done")