from itertools import combinations

def all_variants(text):
    n = len(text)
    for i in range(n + 1):
        for combo in combinations(text, i):
            yield ''.join(combo)


a = all_variants("abc")
for i in a:
    print(i)