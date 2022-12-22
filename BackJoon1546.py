N = int(input())
S = list(map(int, (input()).split()))
MS = max(S)

for i in range(N):
	S[i] = S[i]/MS*100
print(sum(S)/N)