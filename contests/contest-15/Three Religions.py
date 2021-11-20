
def solve(n, q, universe, queries):
    ans = []
    pos_dict, ind_dict = [set() for _ in range(26)], [0 for _ in range(4)]
    for ind,c in enumerate(universe):
        if len(pos_dict[ord(c)-97]) == 250: continue
        pos_dict[ord(c)-97].add(ind)
    for q in queries:
        if q[0] == '-':
            rel = int(q[2])
            if ind_dict[rel]: 
                ans.append('YES')
                ind_dict[rel] -= 1
            else:
                ans.append("NO")
        else:
            _, rel, char = q.split()
            rel = int(rel)
            char_index = ord(char)-97
            if not pos_dict[char_index]:
                ans.append('NO')
                continue
            if not ind_dict[rel]:
                temp = min(pos_dict[char_index])
                ans.append('YES')
                ind_dict[rel] += 1
                pos_dict[char_index].remove(temp)
                continue
            cur_index = ind_dict[rel][-1]
            next_index = float('inf')
            for index in pos_dict[char_index]:
                if index > cur_index:
                    next_index = min(next_index, index)
            if next_index == float('inf'):
                ans.append('NO')
            else:
                ans.append('YES')
                pos_dict[char_index].remove(next_index)
    return ans

if __name__ == '__main__':
    n, q = map(int, input().split())
    word = input()
    queries = [input() for _ in range(q)]
    print(*solve(n, q, word, queries), sep='\n')