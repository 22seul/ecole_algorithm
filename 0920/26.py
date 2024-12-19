def solution(citations):
    answer = 0
    citations.sort()                #citations를 오름차순으로 정렬
    n = len(citations)           #citations 길이 n 구하기
    for i in range(n):             #n만큼 반복
        h = n-i                       #h = n부터 0까지 역순으로
        if(citations[i] >= h):  #정렬된 배열의 수가 h보다 크거나 같으면
            answer = h           #answer에 결과값 대입
            break                    # 반복문 종료
    return answer               # 결과값 리턴