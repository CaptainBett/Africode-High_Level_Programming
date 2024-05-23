
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

#     file.close()


# with open('example.txt', 'w') as f:
#     f.write("*ESSAY HAS BEEN WRITTEN BY BETT")
      #file.close()
  

# with open('example.txt', 'a') as file:
#     content = file.write("\"Added\" message\npowerbank")
#     print(content)
#     file.close



# try:
#     with open('example.txt', 'x') as file:
#         content = file.write("\"Added\" message\npowerbank")
#         print(content)
#         file.close

# except FileExistsError:
#     print("Sorry,the file already exists!")

try:
    import os
    os.remove("Home/pictures/screenshots")
except FileNotFoundError:
    print("Sorry,the file does not exist!")






















