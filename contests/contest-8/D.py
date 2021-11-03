from collections import defaultdict
from typing import List


def get_song(songs, moments)->List[int]:
    n = len(songs)
    i = 1
    song_info = defaultdict(list)
    prev = 0
    for sno, dur in songs:
        song_info[i] = [prev, prev+sno*dur]
        prev += sno*dur
        i += 1
    cur = 1
    ans = []
    j = 0
    while j < len(moments) and cur <= n:
        m = moments[j]
        if song_info[cur][0] <= m <= song_info[cur][1]:
            ans.append(cur)
            j += 1
        else:
            cur += 1
    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    songs = []
    for _ in range(n):
        songs.append(list(map(int, input().split())))
    moments = list(map(int, input().split()))
    # print(moments)
    print(*get_song(songs, moments), sep='\n')