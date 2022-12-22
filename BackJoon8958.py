N = int(input()) #N이라는 O,X로 이루어진 문장을 몇번 반복할지

for i in range(N): #N번 반복한다
	B = list(input()) #예제 입력에 있는 O,X들을 list형식으로 해서 대입
	S = 0 #'O'일 때 +1을 추가하는 변수
	NS = 0 # S = 1 상태에서 'O' 연속하여 나오면 +2 만들어줌
	for u in B: #B의 값으로 반복해줌
		if ox == 'O': #ox라는 변수가 'O' 일경우에는 S += 1 연속될 경우에는 S = 2가 된다.
			S += 1
			NS += S #S의 값을 저장해두는 곳
		else:
			S = 0
	print(NS)