thisdict = {"brand": "ford", "model": "Mustang", "year": 1964}

# EX 1
for key in thisdict:
    print(key)

# EX 2
for key in thisdict:
    print(thisdict[key])

# EX 3
for key in thisdict.keys():
    print(key)

# EX 4
for value in thisdict.values():
    print(value)

# EX 5
for key, value in thisdict.items():
    print(key, value)