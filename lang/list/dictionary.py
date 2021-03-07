d = {'a': 1, 'b': 2, 'c': 3}
for key, value in d.items():
    print('there are {} files with the .{} extension'.format(key, value))

print(d.keys())
print(d.values())

for k, v in d.items():
    print(k, v)

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

