# 6.	Read Code. (a) Write out what each line of the following program does.
# Then write the overall purpose of this program.                                                                                          (5 points)

def mystery2(list1, list2):
    """
    :param list1: first list of numbers
    :param list2: Second list of numbers
    :return:
    """
    out = []
    if len(list2) > len(list1):
        temp = list2[:]
        list2 = list1[:]
        list1 = temp[:]
    for index in range(len(list1)):
        if index < len(list2):
            out.append(list1[index] + list2[index])
        else:
            out.append(list1[index])
    return out


if __name__ == "__main__":
    print(mystery2([100,200,300], [1,2,3,4]))


# (b)Add docstring with doctests to this code and test it.   (5 points)
