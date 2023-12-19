# Define two set variables
E = {0, 1, 2, 3, 4, 5, 8}
N = {2, 4, 6}

# Perform different set operations
Union = E.union(N)
Intersection = E.intersection(N)
Difference = E.difference(N)
Symmetric_Difference = E.symmetric_difference(N)

# Print the results
print("Union of E and N is", Union)
print("Intersection of E and N is", Intersection)
print("Difference of E and N is", Difference)
print("Symmetric difference of E and N is", Symmetric_Difference)