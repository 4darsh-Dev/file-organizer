


# with open(filename, "rt") as f:
#     content = f.read()
    
#     print(type(content))

# f = open(filename, 'r')
# content = f.read(2)
# print(content)
# content = f.readlines()
# print(content)
# myStr =" ".join(content)
# myStr = myStr.strip()
# print(myStr)


# print(type(content))
# f.close()


import pickle

filename = "hello.dat"
f = open(filename, 'rb')
# file = {
#     "Harry": "94",
#     "Hriday" :"95",
#     "Aman" : "98",

# }
# pickle.dump(object, file_handler))

data = pickle.load(f)
# print(type(data))r
for name, number in data.items():
    print(f"{name} : {number}")
    
f.close()
