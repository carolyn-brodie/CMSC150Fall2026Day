# (a) For the following, write both the overall
# purpose of this code and a line-by-line description.                            (5 points)
#
def while_loop_version(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 2

    return total

# Write your answer in comments here

#
#
# (b)	Change the above program by replacing the while loop
# with a for loop. The program should have exactly the same
# results as before. It should work for ANY value of n
# (assuming n is a positive integer).

# Write your do_loop_version here


def test():
    # print(while_loop_version(5))
    # print(do_loop_version(5))
    pass

if __name__ == "__main__":
    test()

