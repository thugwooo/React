a = input()
b = input()

"""while b in a:
    a = a.replace(b, "")
if a:
    print(a)
else :
    print("FRULA")
"""    

stack = []
for ch in a:
    stack.append(ch):
    if ch == b[-1]:
        for i in range(1, len(b)+1):
            if 