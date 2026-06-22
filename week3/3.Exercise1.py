
###
### Assume that list1 is a list of integers.  Create list2 which is the same as list1 except that the value 
# stored at a particular index is not in the new list.  
### For example, if list1 = [1,3,5,7,9] and the index is 1 then list2 should be [1,5,7,9].                                      
###


list1 = [1,3,5,7,9]
list2 = []
index = 3

if index >= 0:
    list2 = list1[:index] + list1[index+1:]
    print(list2)

