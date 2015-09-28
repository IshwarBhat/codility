# https://codility.com/demo/results/trainingSETRFT-MKT/
def solution(A):
    N = len(A)
    B = N * [0]
    for elem in A:
        if elem > N: return 0
        if B[elem-1] == 0:
            B[elem-1] = elem
        else:
            return 0
    return 1
