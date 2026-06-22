

# Write a program that asks the user
# what college they are attending and prints out a strong
# congratulations if it's Simpson, a strong condemnation if it's
# Central, a mild congratulations if it's Drake or Coe, and a neutral ' \

#'message if it's any other college.

college = input("What college do you attend: ")
if college == "Simpson":
    print("YEAH!!!!")
elif college == "Central":
    print("Ok")
elif college == "Drake" or college == "Coe":
    print("That is good")
else:
    print("HMMMM")



