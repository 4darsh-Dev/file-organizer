# name = "harry"

# def change(name):
#     # name = "raju"
#     globals()['name'] = 'raju'
#     print('org  '+ name)

# change(name)
# print(name)

import json

with open('numbers.json', 'r') as f:
    value = {
        "Name": "harry",
        "class": "XII",
        "Roll No" : "24",

    }
    # json.dump(value, f)
    content = json.load(f)
    print(type(content))
    print(content)

