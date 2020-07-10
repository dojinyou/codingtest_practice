"""
Q. 컴퓨터실(10755): https://www.acmicpc.net/problem/10755
CSHS(Computer Science High School)의 실습실에는 총 M대의 컴퓨터가 일렬로 놓여있다. 이 컴퓨터는 왼쪽에 있는 것부터 순서대로 1~M의 번호가 매겨져 있다.
현재, 이 실습실에는 총 N명의 학생들이 이미 앉아있으며, 각각 A1, A2, ..., AN번 컴퓨터 앞에 앉아있다. 
곧 있으면 자습시간이 시작되기 때문에 총 M-N명의 학생이 더 와서 컴퓨터를 사용할 것이다.
각 학생들은 다른 학생이 자기 컴퓨터의 모니터를 보는 것을 싫어하므로 다음과 같은 방법으로 자리를 잡을 것이다.
우선 학생이 없는 연속한 컴퓨터들의 그룹 중 가장 컴퓨터가 많은 그룹을 선택한다. 만약 이런 그룹이 여러개라면 가장 왼쪽에 있는 그룹을 선택한다.
그 다음, 선택한 그룹의 컴퓨터들 중 정 중앙에 있는 컴퓨터를 선택하여 자리를 잡는다. 
만약 학생이 선택한 그룹의 컴퓨터가 짝수개인 경우 정중앙 2개의 컴퓨터 중 왼쪽에 있는 컴퓨터에 자리를 잡는다.
진환이는 Q명의 친구들과 함께 팀 프로젝트를 해야 하기 때문에 Q명의 친구들이 어디에 앉을 지 알아야 한다. 
다행히 진환이는 각 친구가 몇 번째로 실습실에 들어갔는지 알고 있다. 진환이를 도와 각 친구들의 위치를 구하자.

입력: 첫 번째 줄에는 컴퓨터의 수 M, 이미 자리를 잡은 학생의 수 N, 친구의 수 Q가 주어진다.
두 번째 줄에는 N개의 정수가 주어지는데, 이 값은 자리를 잡은 학생의 위치 Ai를 나타낸다. 이미 자리를 잡은 학생들은 앞서 말한 방법으로 자리를 잡지 않았을 수도 있음에 유의하여라.
세 번째 줄에는 Q개의 정수가 주어지는데, 이 값은 각 친구가 실습실에 들어간 순서 Bi를 의미한다.
1 ≤ A1 < A2 < . . . < AN ≤ M, 1 ≤ B1 < B2 < . . . < BQ ≤ M.
1 ≤ Q ≤ 105, N ≤ M, 1 ≤ N ≤ 105, 1 ≤ M ≤ 1014

출력: 출력은 총 Q개의 줄로 이루어진다. 
i번째 줄에는 i번째 친구가 자리잡은 컴퓨터의 번호를 출력한다. 
처리하는 정수의 범위가 32비트 정수를 넘어가므로 64비트 정수형 변수를 사용하도록 한다.
"""
from sys import stdin
from queue import PriorityQueue
M, N, Q  = map(int, stdin.readline().split(' ')) # 전체 명수, 앉아 있는 애들 수, 친구 수
N_list = list(map(int, stdin.readline().split())) # 앉아 있는 친구들 위치
Q_list = list(map(int, stdin.readline().split())) # 친구들 순서
pq = PriorityQueue()
cnt = 0
while Q_list[cnt] <= N :    
    print(N_list[Q_list[cnt]])
    cnt += 1
Q_list = Q_list[cnt:]
prev = 1
for i in range(N):
    pq.put((-1*(N_list[i]-prev),(N_list[i]+prev)//2))
    prev = N_list[i]
    cnt += 1
pq.put((-1*(M-prev),(M+1+prev)//2))
print("cnt=",cnt)
for q in Q_list:
    print(q, "와일전")
    while cnt < M :
        cnt += 1
        info = pq.get()
        print(info)
        space = -1*info[0]
        nxt = info[1]
        pq.put((-1*((space-1)//2), nxt-((space-1)//2+1)//2))
        print((-1*((space-1)//2), nxt-((space-1)//2+1)//2))
        pq.put((-1*((space)//2), nxt+(space//2)//2))
        print((-1*((space)//2), nxt+(space//2)//2))
        if cnt == q :
            print(nxt)
            break
            
            
# 시간초과
# # 미리 앉은 친구들 출력
# for f_num in Q_list[:]:
#   if f_num <= N :
#     print(N_list[f_num-1])
#     Q_list.remove(f_num)
#   else:
#     break

# # 추가로 앉아야될 친구들 출력
# # 우선순위 큐 사용
# queue=[]
# # heapq.heappush(queue, (priority, value))
# # heapq.heappop(queue())

# # 빈칸 찾기
# prev = 0
# length = 0
# nextSeat = 0
# N_list.append(M+1)
# for n in N_list:
#   length = n - prev
#   nextSeat = (n+prev)//2
#   heapq.heappush(queue, (-1*length, (prev, nextSeat, n)))
#   prev = n

# # print("미리 앉히기 종료")
# # print("queue:",queue)
# # seat 빼고 넣으면서 출력하기.
# f_num = 0
# q =len(Q_list)
# for i in range(N+1,M+1):
  
#   # 앉히고
#   info = heapq.heappop(queue)
#   # print(info)
#   lSeat = info[1][0]
#   nSeat = info[1][1]
#   rSeat = info[1][2]
  
#   if i == Q_list[f_num]: 
#     print(nSeat)
#     f_num += 1
#   if f_num == q :
#     break
#   # 새로 넣고
#   if nSeat-lSeat > 1:
#     heapq.heappush(queue, (-1*(nSeat-lSeat), (lSeat, (lSeat+nSeat)//2, nSeat)))
#   if rSeat-nSeat > 1:
#     heapq.heappush(queue, (-1*(rSeat-nSeat), (nSeat, (nSeat+rSeat)//2, rSeat)))
#   # print("앉히고 넣고 끝")
#   # print("queue:",queue)










# # 시간 초과
# cnt = 0
# f_num = 0
# for n in N_list:
#   cnt += 1
#   if Q_list[f_num] == cnt :
#     print(n)
#     f_num += 1
#   if f_num == len(Q_list):
#     break

# N_list.append(M+1)
# for _ in range(M-N):
#   cnt += 1
#   if f_num == len(Q_list):
#     break
  
#   # print("cnt=",cnt)
#   # print("next friend number = ",Q_list[f_num])
#   prev = 0
#   length = 0
#   nextSeat = 0
#   for n in N_list:
#     if length < n - prev :
#       length = n - prev
#       nextSeat = (n+prev)//2
#     prev = n
#   # print("nextSeat=",nextSeat)
#   if Q_list[f_num] == cnt :
#     print(nextSeat)
#     f_num += 1
  
#   N_list.append(nextSeat)
#   N_list.sort()
#   # print("N_list=",N_list)
#   # print()




