"""
Q. 수 찾기(1920): https://www.acmicpc.net/problem/1920
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력: 첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1≤M≤100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력: M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""
import sys
# # hash table 이용
# N = int(sys.stdin.readline())
# N_list =list(map(int, sys.stdin.readline().split()))
# n_dic = {}
# for i in N_list:
#     n_dic[i] = 1
# M = int(sys.stdin.readline())
# M_list =list(map(int, sys.stdin.readline().split()))
# for m in M_list:
#     result = "1" if m in n_dic else "0"
#     sys.stdout.write(result+"\n")

# Binary search
# N = int(sys.stdin.readline())
# N_list =list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# M_list =list(map(int, sys.stdin.readline().split()))
# N_list.sort()

# for m in M_list:
#     l, h = 0, N
#     while True:
#         mid = (l+h)//2
#         if m == N_list[mid]:
#             print(1)
#             break
#         if l == mid :
#             print(0)
#             break
#         if m > N_list[mid]:
#             l = mid
#         else :
#             h = mid