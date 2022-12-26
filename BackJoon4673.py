numbers=set(range(1,10000)) #전체 숫자의 범위
remove_set=set()

for num in numbers:
    for n in str(num): #str 로 해서 num 33 일 경우에 3,3 으로 되서 33 + 3+ 3와 미침
        num+=int(n)
    remove_set.add(num) #remove_set = 생성자가 있는 숫자

self_numbers=numbers-remove_set
for self_num in sorted(self_numbers): #sorted 정렬 함수
    print(self_num)