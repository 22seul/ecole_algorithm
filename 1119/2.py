N = int(input())  #총 상담 가능한 날의 수 입력
t = []  #각 상담에 걸리는 일수 저장
p = []  #각 상담으로 얻는 수익 저장
dp = [0 for i in range(N+1)]  #최대 수익을 저장할 DP 테이블 초기화

# 상담 데이터 입력받기
for i in range(N):
    T, P = map(int, input().split())  #상담 일수(T)와 수익(P) 입력
    t.append(T)  #일수를 t 리스트에 추가
    p.append(P)  #수익을 p 리스트에 추가

# 뒤에서부터 거꾸로 최대 수익 계산
for i in range(N-1, -1, -1):
    if t[i] + i > N:  #상담이 퇴사일을 초과하면
        dp[i] = dp[i+1]  #다음 날의 최대 수익을 그대로 가져옴
    else:
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i])  #상담 안 할 경우와 상담할 경우 중 최대값 선택

# 최대 수익 출력
print(dp[0])
