#module make_division.py
import csv
def make_division() :
    division = {}
    f = open('C:/Users/india/OneDrive/바탕 화면/code/파이썬/petfood_exe/데이터분류.csv','r',encoding='utf-8-sig')
    rdr = csv.reader(f)

    for line in rdr :
        n=0
        for word in line :
            word = word.replace(" ","") #띄어쓰기 제거
            if n==0 :
                name = word
                division[name] = []
            elif word != '':
                division[name].append(word)
            n=1

    f.close()
    return division