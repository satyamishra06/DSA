def solve(n,A,q):
n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))
q = int(input())
answer = 0
for _ in range(q):
    i, l, r = map(int, input().split())

    if i == 1:
        value = A[l]
        for i in range(l, r + 1):
            A[i] = (i - l + 1) * value

    else:
        current_sum = 0
        for i in range(l, r + 1):
            current_sum += A[i]
            answer =(answer + current_sum) % (109 + 7)
        return answer    
    

        