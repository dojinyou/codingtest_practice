"""
Q. 완주하지 못한 선수(프로그래머스): https://programmers.co.kr/learn/courses/30/lessons/42576
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한 조건 : 
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

입출력 예 :
participant	completion	return
[leo, kiki, eden]	[eden, kiki]	leo
[marina, josipa, nikola, vinko, filipa]	[josipa, filipa, marina, nikola]	vinko
[mislav, stanko, mislav, ana][stanko, ana, mislav]	mislav
"""

def solution(p, c):
    # hash
    p_hash = {}
    c_hash ={}    
    for i in range(len(p)):
        if p[i] not in p_hash:
            p_hash[p[i]] = 1
        else :
            p_hash[p[i]] += 1
        if i == len(c):
            continue
        if c[i] not in c_hash:
            c_hash[c[i]] = 1
        else :
            c_hash[c[i]] += 1
            
    for person in p:
        if person not in c_hash:
            return person
        if c_hash[person] != p_hash[person]:
            return person
    # sort
    p.sort()
    c.sort()
    for i in range(len(p)-1):
        if p[i] != c[i]:
            return p[i]
    return p[-1]