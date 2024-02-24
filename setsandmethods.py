# Sets don't support duplicates

a1 = {5,23,3,5,45,5}
a2 = {3,5,23,67,89,9,90,76}
# a1.clear()
# print(a1.pop())
print(a1)
print(a2)
print(a1 == a2)
a1.union(a2)   # this doesn't work
print(a1.union(a2))
print(a1.intersection(a2))
print(a1)