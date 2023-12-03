m = 200
n = 3

triples = []

for a in range(1, m+1):
    for b in range(1, m+1):
        c = b + n
        if a**2 + b**2 == c**2:
            triples.append((a, b, c))

print(triples)