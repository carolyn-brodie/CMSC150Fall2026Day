# (a) For  the  following, write both an overall purpose
# of this code and a line-by-line description.                            (5 points)
#

def for_loop_version():
    number = 0
    for count in range(1, 20, 3):
        if (count % 2 == 1):
           number += 1
    return number
#
# Put your answer here as a comment


#
# (b)	Change the for loop to a while loop so that the same
# effect is achieved.

# Write your new function here that does the same as above
# but uses a while loop instead of a for loop



def test():
    pass
    # print(for_loop_version())
    # print(while_loop_version())

if __name__ == '__main__':
    test()