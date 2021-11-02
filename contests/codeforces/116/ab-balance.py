tests = [input() for _ in range(int(input()))]

for t in tests:
    cab = t.count('ab')
    cba = t.count('ba')
    str_list = [c for c in t]
    if cab == cba:
        print(t)
    else:
        if cab > cba:
            idx = t.index('ab')
            if idx > 0 and t[idx-1] == 'a':
                str_list[idx-1] = 'b'
            else:
                str_list[idx] = 'b'
        else:
            idx = t.rindex('ba')
            if idx < len(t)-2 and t[idx+2] == 'a':
                str_list[idx+2] = 'b'
            else:
                str_list[idx+1] = 'b'
        print(''.join(str_list))