def solution(cacheSize, cities):
    cache = [ ]
    answer = 0
    for c in cities:
        if c in cache:
            pass
        else :
            if len(cache) < cacheSize:
                cache.append(c)
                
            else :
                cache = cache[1:] +[c]

            answer += 5
    return answer