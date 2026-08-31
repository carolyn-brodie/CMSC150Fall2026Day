# 1.	List Indexing and Membership. Assume
# list1 is [5, 2, 24, 1, 7, 0] and
# list2 is [7, -2, list1, 6].
# What are each of the following?

def main():
    list1 = [5, 2, 24, 1, 7, 0]
    list2 = [7, -2, list1, 6]
    print(f"{list1[0] + list2[1]} returns ____")
    print(f"{list2[2][2]} returns ____")
    print(f"{list1[len(list1)  - 3]} returns ____")
    print(f"{list1[: 5 : 3]} returns ______________")
    print(f"{list1[4 : 2]} returns ______________")
    print(f"{list1[:]} returns ______________")
    print(f"{list2[ :  : -1]} returns ______________")
    print(f"{2 in list1} returns ____")
    print(f"{2 in list2} returns ____")
    print(f"{2 in list2[2]} returns ____")


if __name__ == "__main__":
    main()