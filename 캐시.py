def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache: 
            cache.remove(city)
            cache.append(city)
            answer += 1
            continue
        answer += 5
        if len(cache) < cacheSize:
            cache.append(city)
        else:
            if cache:
                del cache[0]
            if len(cache)+1 <= cacheSize:
                cache.append(city)
    return answer
print(solution(	0, ["Jeju", "Jeju"]))