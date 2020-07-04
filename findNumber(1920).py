"""
Q. 수 찾기(1920): https://www.acmicpc.net/problem/1920
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력:첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1≤M≤100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력: M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""
from sys import stdin
N = int(stdin.readline())
N_list =list(map(int, stdin.readline().split(' ')))
M = int(stdin.readline())
M_list =list(map(int, stdin.readline().split(' ')))

# 틀림.
# N_list.sort()
# M_sort = sorted(M_list)
# M_dict = {m:0 for m in M_list}

# nextIdx = 0
# for m in M_sort:
#     for i in range(nextIdx,N):
#         if N_list[i] > m:
#             break
        
#         nextIdx = i
#         if N_list[i] == m :
#             M_dict[m]=1
#             break

# for inNum in M_dict.values():
#     print(inNum)






# 시간초과
# N_list.sort()
# M_dict = {m:0 for m in M_list}

# for m in M_list:
#     for n in N_list:
#         if m < n :
#             break
#         if m == n:
#             M_dict[m]=1
#             break
# for inNum in M_dict.values():
#     print(inNum)

# 시간초과
# from sys
# N_list.sort()
# inNum_list = []

# for m in M_list:
#     inNum = 0
#     for n in N_list:
#         if m < n :
#             break
#         if m == n:
#             inNum = 1
#     inNum_list.append(inNum)
# for inNum in inNum_list:
#     print(inNum)