def solution(new_id):
    one = new_id.lower()
    two = ""
    for c in one:
        if c.isalnum() or c =="-" or c=="_" or c==".":
            two +=c
    three = two.replace("..",".")
    if three[0] == ".":
        three.pop(0)
    if three[-1] ==".":
        three.pop()
    four = three

    if four:
        pass
    else : 
        five = "a"
    

    answer = ''
    return answer