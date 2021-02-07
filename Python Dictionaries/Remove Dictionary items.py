# EX 1
thisdict = {"brand": "ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)
# Output: {'brand': 'Ford', year': 1964}

# EX 2
thisdict = {"brand": "ford", "model": "Mustang", "year": 1964}
thisdict.popitem()
print(thisdict)
# Output: {'brand': 'ford', 'model': 'Mustang'}

# EX 3
thisdict = {"brand": "ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)
# Output: {'brand': 'ford', 'year': 1964}

# EX 4
thisdict = {"brand": "ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)
# Output: 'brand': 'ford', 'year': 1964}
