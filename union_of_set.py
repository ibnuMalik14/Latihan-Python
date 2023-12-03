print("Finding union of two Sets")
a = set(input("Enter first set : "))
b = set(input("Enter second set : "))

c = a.union(b)
d = a.intersection(b)

print(f"The union is : {c}")
print(f"The intersection is : {d}")