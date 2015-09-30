# https://codility.com/demo/results/training4DKVMD-3KM/
def solution(N, A):
    counters = N * [0]
    max_counters = 0
    last_update = 0
    for elem in A:
        if elem == N+1:
            last_update = max_counters
        else:
            if counters[elem-1] < last_update:
                counters[elem-1] = last_update
            counters[elem-1] += 1
            if counters[elem-1] > max_counters:
                max_counters = counters[elem-1]
    for i in xrange(N):
        if counters[i] < last_update:
            counters[i] = last_update
    return counters


