"""
Q. 수 정렬하기2(2751): https://www.acmicpc.net/problem/2751
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력:첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다.
이 수는 10,000보다 작거나 같은 자연수이다.

출력: 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
import sys
N_list = []
N = int(sys.stdin.readline())
for _ in range(N) :
    n = int(sys.stdin.readline())
    N_list.append(n)
for n in sorted(N_list):
    print(n)
# N_list = [False]*1000000
# N = int(sys.stdin.readline())
# for _ in range(N) :
#     n = int(sys.stdin.readline())
#     N_list[n-1] = True
# for i in range(1000000):
#     if N_list[i]:
#         print(i+1)