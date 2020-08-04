def solution(a, b):
    indexA = 0
    indexB = 0
    travel = 0
    location = 0
    while indexA<len(a) or indexB<len(b):
        distA = abs(a[indexA]-location) if indexA<len(a) else 100001
        distB = abs(b[indexB]-location) if indexB<len(b) else 100001
        target = distA<distB #true for a, false for b
        if(target):
            travel += distA
            location = a[indexA]
            indexA += 1
        else:
            travel += distB
            location = b[indexB]
            indexB += 1
        print(location)
    return travel

print(solution([5,3,10,6],[9,7,12]))