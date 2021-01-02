from typing import List

"""
1-2-3
4-1
2

3 - 1
3 - 5
"""


# def most_Visited_sector(n: int, rounds: List[int]) -> List[int]:
#     freq_dict = {}
#     for i in range(1, len(rounds)):
#         start = rounds[i - 1]
#         end = rounds[i]
#         if i == 1:
#             for j in range(start, end):
#                 if end > start:
#                     if j in freq_dict.keys():
#                         freq_dict[j] = freq_dict[j] + 1
#                     else:
#                         freq_dict[j] = 1
#                 else:
#                     pass
#         else:
#             for j in range(start + 1, end):
#                 if end > start:
#                     if j in freq_dict.keys():
#                         freq_dict[j] = freq_dict[j] + 1
#                     else:
#                         freq_dict[j] = 1
#                 else:
#                     pass
#
#         # for j in range(rounds[i - 1], rounds[i]):
#         #     sec = (j % n) + 1
#         #     if sec in freq_dict.keys():
#         #         freq_dict[sec] = freq_dict[sec] + 1
#         #     else:
#         #         freq_dict[sec] = 1
#
#     print(freq_dict)

#
# print(most_Visited_sector(4, [1, 3, 1, 2]))
