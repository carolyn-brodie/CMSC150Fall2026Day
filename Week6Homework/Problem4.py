# a) Write out what each line of the following program does.
# Then write the overall purpose of this program.                                                                                                   (5 points)
def mystery(n):
    total = 1
    for number in range(1, n):
         total *= number
    return total

#   (b)Add docstring with doctests to this code and test it. What situation
# is not being handled in a way that makes sens
# by this code and how would you fix it?     (5 points)



if __name__ == "__main__":
    print(mystery(3))
    print(mystery(0))