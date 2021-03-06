import time

from binary_search_tree import BSTNode



start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

#Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# the runtime complexity is O(n**2), or to be more specific O(len(names_1)*len(names_2))

"""solution 1"""

# bst = BSTNode("named entries")

# for name in names_1:

#     bst.insert(name)

# for name in names_2:

#     if bst.contains(name):

#         duplicates.append(name)


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.



""" solution 2: fastest solution"""

names_1 = set(names_1)
names_2 = set(names_2)

duplicates = list(names_1.intersection(names_2))

""" solution 3 """

# storage = {name:0 for name in names_1}

# for name in names_2:

#     try:

#         storage[name] += 1

#     except:

#         continue

# duplicates = [key for key in storage.keys() if storage[key] == 1]


""" solution using only lists """

# from collections import Counter

# all_names = names_1 + names_2

# cnt = Counter(all_names)

# duplicates = [k for k, v in cnt.items() if v > 1]

# this solution does not account for duplicates in lists themeselves


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



