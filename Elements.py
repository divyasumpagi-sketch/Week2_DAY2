# Create a student dictionary
student = {
    "Name": "Divya",
    "Branch": "BSc",
    "Year": "3rd",
    "CGPA": 8.2
}

print("Original Dictionary:")
print(student)

# 1. Add a new element
student["College"] = "KLE"
print("\nAfter Adding College:")
print(student)

# 2. Update an existing element
student["CGPA"] = 8.5
print("\nAfter Updating CGPA:")
print(student)

# 3. Delete an element
del student["Year"]
print("\nAfter Deleting Year:")
print(student)
