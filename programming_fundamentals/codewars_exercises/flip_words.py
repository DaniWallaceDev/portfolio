def solution(s):
    l = []
    for i in s:
        l=[i]+l
    return "".join(l)

print(solution("hola"))