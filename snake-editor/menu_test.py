import os
fileLocal = os.path.expanduser('~/Snake-content')
themes = os.listdir(fileLocal)
names = []
names.append(["Name","name"])
for theme in themes:
    names.append([theme,theme])

print names
