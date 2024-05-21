# def my_function():
#     local_var = "I am local!"
#     print(local_var)
# my_function()
# print(local_var)


global_var = 'I am global!'

def show_global():
    global global_var
    global_var = "I am superior!"
    print(global_var,"Inside a function")

show_global()
print(global_var)




























