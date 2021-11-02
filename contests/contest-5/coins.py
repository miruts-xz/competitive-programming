comparisons = [input() for _ in range(3)]
ranks = {}
ranks['A'], ranks['B'], ranks['C'] = 0, 0, 0
for cmp in comparisons:
    if cmp[1] == '>':
        ranks[cmp[0]] += 1
    else:
        ranks[cmp[2]] += 1
if ranks['A'] == ranks['B'] or ranks['A'] == ranks['C'] or ranks["B"] == ranks['C']:
    print("Impossible")
else:
    print(*[k for k, _ in sorted(ranks.items(), key=lambda x: x[1])], sep='')

        


    