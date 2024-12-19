# 주어진 괄호 문자열이 올바른지 여부를 확인하는 함수
def check(s):
    stack = []  # 스택을 사용하여 '('를 저장

    for i in s:  # 문자열의 각 문자를 순회
        if i == '(':  # 여는 괄호인 경우
            stack.append(i)  # 스택에 추가
        else:  # 닫는 괄호인 경우
            if len(stack) == 0:  # 스택이 비어있다면 짝이 맞지 않음
                return False
            stack.pop()  # 스택에서 여는 괄호 '('를 제거 (짝이 맞는 경우)
    return True  # 스택이 비어 있으면 올바른 괄호 문자열이니 True출력


# 주어진 문자열을 균형잡힌 괄호 문자열 u, v로 분리하는 함수
def divide(s):
    left, right = 0, 0  # 왼쪽 괄호 '('와 오른쪽 괄호 ')'의 개수를 카운트
    for i in range(len(s)):
        if s[i] == '(':  # 여는 괄호가 나오면
            left += 1  # 왼쪽 괄호 개수 증가
        else:  # 닫는 괄호가 나오면
            right += 1  # 오른쪽 괄호 개수 증가
        
        # 여는 괄호와 닫는 괄호의 개수가 같아지는 순간, 균형잡힌 문자열을 찾음
        if left == right:
            # s[:i+1]: 0부터 i까지의 부분 문자열을 반환 (여기서 +1은 i번째 문자를 포함하기 위해서임)
            # 즉, s의 처음부터 i번째 문자까지를 u로, 나머지 부분을 v로 나누는 것
            return s[:i+1], s[i+1:]  # u, v를 반환


# 올바른 괄호 문자열로 변환하는 함수
def solution(p):
    #1
    if not p:  
        return ''

    # 2
    u, v = divide(p)  

    # 3, 3-1
    if check(u):  # u가 올바른 괄호 문자열이면
        return u + solution(v)  # u는 그대로 두고 v에 대해 재귀적으로 처리한 후 u에 붙임
    
    # 4-1 ~ 4-3
    else:
        # u가 올바르지 않은 경우
        answer = '('  # 빈 문자열에 '('를 붙임
        answer += solution(v)  # v를 재귀적으로 처리한 결과를 붙임
        answer += ')'  # 다시 ')'를 붙임

        
        # 4-4, 4-5
        for s in u[1:len(u)-1]:  # u의 첫 문자와 마지막 문자를 제외한 부분만 확인
            if s == '(':  # '('를 ')'로 바꾸고
                answer += ')'
            else:  # ')'를 '('로 바꿈
                answer += '('
        
        return answer  # 변환된 결과를 반환

