ar = ["c=","c-","dz=","d-","lj","nj","s=","z="]
arr = input()

for t in ar:
    arr = arr.replace(t," ")

print(len(arr))