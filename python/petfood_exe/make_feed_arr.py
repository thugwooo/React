####################
#사료데이터 읽어와서 dic arr 로 저장하기
import csv

def make_feed(division) :
    f = open('C:/Users/india/OneDrive/바탕 화면/code/파이썬/petfood_exe/사료데이터.csv','r',encoding='utf-8-sig')
    rdr = csv.reader(f)

    feed_arr = []

    n=0
    for line in rdr :
        if n == 0 or n ==1 : 
            n+=1
            continue

        x=0
        for l in line :
            if x in {3,15} :
                x+=1
            else :
                line[x] = line[x].replace(" ","") #사료이름, 기타 빼고 나머지 띄어쓰기 제거
                x+=1


        dics = {}

        #급여대상 pet (int)
        dics['pet']=division['pet'].index(line[0])

        #브랜드 brand (int)
        dics['brand']=division['brand'].index(line[1])

        #사료이름 name (string)
        dics['name']=line[3]

        #특정종대상 breed (int)
        dics['breed']=division['breed'].index(line[4])

        #단백질원 like (int set)
        likely = line[5].split(',')
        temp = set()
        for l in likely :
            l = l.replace(" ","")
            temp.add(division['like'].index(l))
        dics['like']=temp

        #주원료 alle (int set)
        alle = line[6].split(',')
        temp = set()
        for al in alle :
            al = al.replace(" ","")
            i = division['alle'].index(al) if al in division['alle'] else None
            if (i != None) :
                temp.add(i)
        dics['alle']=temp

    
        #Kcal/100g kcal (float)
        dics['kcal']=float(line[7])

        #동물크기 size (int)
        dics['size']=division['size'].index(line[8])

        #사료종목 type (int)
        dics['type']=division['type'].index(line[9])

        #제조국 cont (int)
        dics['cont']=division['cont'].index(line[10])

        #급여연령 age_low, age_high (int, int)
        age=line[11].split('~')
        dics['age_low'] = int(age[0])
        if age[1] == 'max' : 
            age[1]=10000
        dics['age_high'] = int(age[1])

        #급여시기 when (int set)
        when = line[12].split(',')
        temp = set()
        for w in when :
            w = w.replace(" ","")
            i = division['when'].index(w) if w in division['when'] else None
            if (i != None) :
                temp.add(i)
        dics['when']=temp

        #유기농여부 org (bool)
        if line[13] == 'N' :
            dics['org']=False
        else : dics['org']=True

       #키블크기(mm) kib_size (int)
        dics['kib_size'] = int(line[14])

        #기타 etc (str)
        dics['etc']=line[15]

        #성분비율 nutr (float arr)

        temp = []
        for data in line[16:24] :
            if data == 'X' : data = -1
            temp.append(float(data))
    
        feed_arr.append(dics)

    f.close()
    
    return feed_arr