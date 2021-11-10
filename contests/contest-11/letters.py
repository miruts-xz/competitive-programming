def letters():
    nm = list(map(int, input().split()))
    m = nm[1]
    dormitory = list(map(int, input().split()))
    letters_ = list(map(int, input().split()))
    prefix = [0]
    for i in range(len(dormitory)):
        prefix.append(prefix[i] + dormitory[i])
    i, j = 0, 1
    while i < m:
        letter = letters_[i]
        dorm = prefix[j]
        if letter <= dorm:
            room = letters_[i] - prefix[j - 1]
            print(j, room)
            i += 1
        else:
            j += 1

letters()
