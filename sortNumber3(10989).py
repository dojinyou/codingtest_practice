"""
Q. 수 정렬하기2(10989): https://www.acmicpc.net/problem/10989
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력:첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다.
이 수는 10,000보다 작거나 같은 자연수이다.

출력: 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
import sys
N_list = [0]*10000
N = int(sys.stdin.readline())
for _ in range(N) :
    N_list[int(sys.stdin.readline())-1] += 1
for i in range(10000):
    [print(i+1) for _ in range(N_list[i])]

# # 메모리초과
# N_list = []
# for _ in range(int(sys.stdin.readline())):
#     N_list.append(int(sys.stdin.readline()))

# for i in sorted(N_list):
#     print(i)

# # 메모리초과
# for i in sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]):
#     print(i)