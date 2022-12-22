C = int(input()) #테스트케이스

for i in range(C):
    N = list(map(int, input().split())) #점수, 학생수를 N에 받는다
    M = sum(N[1:])/N[0] #한 묶음만 슬라이싱 점수, 학생수 평균이 나옴
    cnt = 0
    for score in N[1:]: #점수를 돌린다
        if score > M: #평균보다 높다면
            cnt += 1 #cnt +1
    B = cnt/N[0] * 100 #N[0] = 5    B = 50
    print(f'{B:.3f}%') #B:.3f = B의 소수점 3번째 까지 표현해준다



