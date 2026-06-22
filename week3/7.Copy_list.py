
the_list = ['a', 1, 'b', 2, 'c', 3]
alias_of_list = the_list    ##This makes an alias, not a copy
copy_of_list = []
for element in the_list:
    copy_of_list.append(element)


print(the_list, alias_of_list, copy_of_list)
the_list[0] = 100
print(the_list, alias_of_list, copy_of_list)

another_copy = the_list[:]


