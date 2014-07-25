import curses

mapping = {chr(i):i for i in range(256)}
mapping.update((name[4:], value) for name, value in vars(curses).items()
            if name.startswith('KEY_'))

print(mapping)
