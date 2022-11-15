a = {'a': 2, 'b': 3, 'c': 1}
r = a.items()
p = sorted(a.items(), key=lambda x: x[1], reverse=True)

for k, v in p:
    print(f'{k}-{v}')
