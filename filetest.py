f = open("files/vegetables.txt","a+")
f.write("\nokra")
f.seek(0)
print(f.read())
f.close()

# with open("./files/vegetables.txt","r") as f:
#     content = f.read()
# print(content)