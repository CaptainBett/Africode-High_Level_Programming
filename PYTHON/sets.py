
# Mutability of sets
# students = {"Benz","Nick","Naomi","Enock"}
# student1 = ["Benz","Nick","Naomi","Enock"]
# student1 [0] = "Kip"
# print(student1[0])

# Checking if there are common values in different sets
students = {"Benz","Nick","Naomi","Enock"}
# students2= {"Benz","Nick","Gladwell","Ben"}
# print(students.intersection(students2))
# Commonvalues = students = "Benz","Nick"

# DIFFERENCE
# Checking values that are not common in different sets
# print(students2.difference(students))

# UNION
# PRINTING ALL THE VALUES IN DIFFERENT SET
# print(students2.union(students))

# SUBSET
# Malestudents = {"Benz","Nick","Enock","Cheptoo"}
# # Femalestudents = {"Naomi","Gladwell"}
# if Malestudents.issubset(students):
#     print("Malestudents is a subset of students")
# else :
#     print("Malestudents is not a subset of students")

# SUPERSET
Malestudents = {"Benz","Nick","Enock","Cheptoo"}
# Femalestudents = {"Naomi","Gladwell"}
if Malestudents.issuperset(students):
    print("Malestudents is a superset of students")
else :
    print("Malestudents is not a superset of students")












































