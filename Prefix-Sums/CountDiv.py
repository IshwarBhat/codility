# https://codility.com/demo/results/trainingHEUY32-ZQM/
def solution(A, B, K):
    result = 0;

    if (A%K == 0) :
        result = ((B-A)/K)+1
    else:
        result = (B/K - ((A/K)+1))+1
    return result;
