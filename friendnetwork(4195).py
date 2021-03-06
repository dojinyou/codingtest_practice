"""
Q. 친구 네트워크(4195): https://www.acmicpc.net/problem/4195
민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이, 
민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.
어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

입력: 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 
이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 
친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

출력: 친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
"""
from sys import stdin
for _ in range(int(stdin.readline().strip())):
    f_set = {}
    set_list = []
    for i in range(int(stdin.readline().strip())):
        f1, f2 = map(str, stdin.readline().split())
        if f1 in f_set and f2 in f_set:
            set_list[f_set[f1]] += set_list[f_set[f2]]
            set_list.pop(f_set[f2])
            for name in f_set:
                if f_set[name] == f_set[f2]:
                    f_set[name] = f_set[f1]
                if f_set[name] > f_set[f2]:
                    f_set[name] -= 1
        elif f1 in f_set:
            f_set[f2] = f_set[f1]
            set_list[f_set[f1]] += 1
        elif f2 in f_set:
            f_set[f1] = f_set[f2]
            set_list[f_set[f2]] += 1
        else :
            f_set[f1], f_set[f2] = len(set_list), len(set_list)
            set_list.append(2)
        print(set_list[f_set[f1]])




# # 시간초과
# for _ in range(int(stdin.readline().strip())):
#     set_list = []
#     for i in range(int(stdin.readline().strip())): # 친구 관계수 F < 100,000
#         f1, f2 = map(str, stdin.readline().split())
#         f1_idx, f2_idx = -1, -1
#         for i in range(len(set_list)):
#             if f1 in set_list[i]:
#                 f1_idx = i
#             if f2 in set_list[i]:
#                 f2_idx = i   
#         if f1_idx != -1 :
#             if f2_idx != -1 :
#                 min_idx = min(f1_idx,f2_idx)
#                 max_idx = max(f1_idx,f2_idx)
#                 set_list[min_idx] = set_list[min_idx].union(set_list[max_idx])
#                 set_list.pop(max_idx)
#                 print(len(set_list[min_idx]))
#             else :
#                 set_list[f1_idx].add(f2)
#                 print(len(set_list[f1_idx]))
#         else:
#             if f2_idx != -1 :
#                 set_list[f2_idx].add(f1)
#                 print(len(set_list[f2_idx]))
#             else :
#                 set_list.append(set([f1,f2]))
#                 print(len(set_list[-1]))

# # 메모리 초과
# for _ in range(int(stdin.readline().strip())):
#     f_dict ={}
#     for i in range(int(stdin.readline().strip())): # 친구 관계수 F < 100,000
#         f1, f2 = map(str, stdin.readline().split())
#         if f1 in f_dict :
#             if f2 in f_dict:
#                 f_dict[f1].update(list(f_dict[f2])+[f2])
#                 f_dict[f2].update(list(f_dict[f1])+[f1])
#             else:
#                 f_dict[f1].add(f2)
#                 f_dict[f2] = set(list(f_dict[f1])+[f1])
#         else :
#             if f2 in f_dict:
#                 f_dict[f2].add(f1)
#                 f_dict[f1] = set(list(f_dict[f2])+[f2])
#             else:
#                 f_dict[f1] = set([f1, f2])
#                 f_dict[f2] = set([f1, f2])
#         print(len(list(f_dict[f1].union(f_dict[f1]))))