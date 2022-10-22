xs = [None, 'This', 'is', 'a', 'filler', 'test', 'string', None]

d = {None: '', 'filler': 'manipulated'}

res = [d.get(x, x) for x in xs]

print(res)
