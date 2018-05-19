def solution(N):
    str = format(N, 'b')
    import re
    matches = re.findall(r'(?=(10+1))', format(N, 'b'))
    return len(max(matches, key= lambda x: len(x))) - 2 if len(matches) != 0 else 0