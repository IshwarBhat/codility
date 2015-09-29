# https://codility.com/demo/results/trainingTC7JSX-8E9/
def solution(N, A):
    counters = N * [0]
    max_counters = 0
    for elem in A:
        if elem == N+1:
            counters = N * [max_counters]
        else:
            this_elem = counters[elem-1] + 1
            counters[elem-1] = this_elem
            if this_elem > max_counters:
                max_counters = this_elem
    return counters
