#sets
this_set = {1,2,3,4}
this_set.add(5)
print(this_set)
this_set.pop()
print(this_set)
this_set2 = {6,7,8,9}
result_set = this_set.union(this_set2)
print(result_set)
this_set.update(this_set2)
print(this_set)
this_set.discard(2)
this_set.remove(3)