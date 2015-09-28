#https://codility.com/demo/results/trainingWKXGGR-SN3/
def solution(A):
    N = len(A)
    B = N * [0]
    extras = 0
    for elem in A:
        if elem <= N and elem > 0:
            B[elem-1] = elem
    for i in xrange(N):
        if B[i] == 0:
            return i+1
    return N+1
