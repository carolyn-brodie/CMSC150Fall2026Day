# Using the Python code below, add statements to finish this simple 4 function integer calculator.   Your program should do the following:
# (a)	If 1 is chosen, print the sum of number
# (b)	If 2 is chosen, print the difference between number1 and number2
# (c)	If 3 is chosen, print the product of number1 and number2
# (d)	If 4 is chosen, print the quotient after dividing number1 by number2
#       Be sure to use real division.
# (e)	If anything else is chosen, print “invalid selection”                           (10 points)
#

def main():

    result = 0
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    choice =  int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, or 4 for division"))
    # write an if / elif /else structure to perform the requested
    # operation based on the users input


    print(result)

if __name__ == "__main__":
    main()

