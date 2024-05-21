# def name_function():
#     print("Captain")
# name_function()


# def sum(num1=0,num2=0):
#     if num1 is not int or num2 is not int:
#         return
        
#     return num1 + num2
# result = sum("aha",1)
# print(result)



# def multiple_items(*students):
#     print(students)
#     print(type(students))
# multiple_items("Doreen","Benz","Naomi","Nick")



# def multiple_items(**students):
#     print(students)
#     # print(type(students))
# multiple_items(first="Captain",Last="Bett")


# def multiple_items (name,age,admission):
#     print(name,admission)
# multiple_items("Benz")

def data_types_inFunc(*args):
    print(args)
data_types_inFunc("Ben",{"Language":"Python","Framework":"Flask","Semester":1},3,["Morning lesson","Midday lesson","Evening lesson"])

split1 = data_types_inFunc.splitlines(",")
print(split1)



























