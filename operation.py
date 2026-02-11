# Create two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)

# Union
union_set = set1.union(set2)
print("\nUnion:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Symmetric Difference
sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff_set)
