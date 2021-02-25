import re
dart = ['1S2D*3T']
db = {'S':'**1','D':'**2','S':'**T', '#':'*-1'}
def solution(dartResult):
    for i in re.sub('([SDT][*#]?)', '\g<1> ', dartResult).split():
        for j in db.key():
            i = i.replace(j, db[j])
            print(i)
    answer = 0
    return answer

solution(dart)
