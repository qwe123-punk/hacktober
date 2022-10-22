xs = [None, 'This', 'is', 'a', 'filler', 'test', 'string', None]

d = {None: '', 'filler': 'manipulated'}

res = [d.get(x, x) for x in xs]
my_str = ' '.join(str(item) for item in res)
print(my_str)
