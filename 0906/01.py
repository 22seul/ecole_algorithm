def solution(line):
    answer = []
    points = set() #교점(x,y)을 추가할 비어있는 집합 자료형
        
    # 교점 구하기
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            
            if (a * d) - (b * c) != 0: #평행하는 직선이 아니라면
                x = (b * f - e * d) / (a * d - b * c) # x 좌표 = BF - ED / AD - BC
                y = (e * c - a * f) / (a * d - b * c) # y 좌표 = EC - AF / AD - BC
            
            # 정수 확인
            if int(x) == x and int(y) == y:
                x = int(x)
                y = int(y)
                points.add((x, y)) #집합에 튜플(좌표) 추가
                
    # 그림 영역 구하기
    min_x = min(point[0] for point in points) # 집합에 추가된 튜플(좌표)에서 x좌표의 최소값
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    
    # 그림 그리기
    # x좌표는 왼쪽에서 오른쪽으로 증가, y좌표는 위에서 아래로 감소
    for y in range(max_y, min_y - 1, -1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                row += "*"
            else:
                row += "."
        answer.append(row)
                    
    return answer
