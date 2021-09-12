"""
csv_to_dic_general_petfood()	//일반 사료 csv를 dictionary 형태로 return
csv_to_dic_division_general_petfood()	// 일반 사료 분류 csv 를 dictionary 형태로 return
csv_to_dic_prescription_petfood()	//처방식 사료 csv를 dictionary 형태로 return
csv_to_dic_division_prescription_petfood()	//처방식 사료 분류 csv를 dictionary로 return
"""

import csv

def csv_to_dic_division_general_petfood() :
    division = {}
    f = open('division_general_petfood.csv','r',encoding='utf-8-sig')
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

def csv_to_dic_general_petfood(division) :
    f = open('general_petfood.csv','r',encoding='utf-8-sig')
    rdr = csv.reader(f)
    general_petfood = []

    n=0
    for line in rdr :
        if n == 0 : 
            n+=1
            continue
        food_dic = {
            'pet' : 0,
            'brand' : 0,
            'name' : "no name",
            'breed' : 0,
            'price' : 1000000.0,
            'like' : [],
            'alg' : [],
            'kcal' : 0.0,
            'size' : 0,
            'type' : 0,
            'cont' : 0,
            'age' : [0,10000],
            'org' : bool,
            'kib_size' : 1000,
            'when' : [0],
            'nutr' : [],
            'cnt' : 0
        }
        
        #급여대상 pet (int)
        food_dic['pet']=division['pet'].index(line[0])

        #브랜드 brand (int)
        if line[1] in division['brand'] :
            food_dic['brand']=division['brand'].index(line[1])

        #사료이름 name (string)
        food_dic['name']=line[2]

        #특정종대상 breed (int)
        if line[3] in division['breed'] :
            food_dic['breed']=division['breed'].index(line[3])

        #가격/kg    price (float)
#        food_dic['price']=division['price'].index(line[6])

        #단백질원 like (int list)
        likely = line[7].split(',')
        for l in likely :
            l = l.replace(" ","")
            if l in division['like'] :
                food_dic['like'].append(division['like'].index(l))

        #주원료 alg (int list)
        alg = line[8].split(',')
        for al in alg :
            al = al.replace(" ","")
            if al in division['alg'] and al not in food_dic['alg'] :
                food_dic['alg'].append(division['alg'].index(al))

        """
        #Kcal/100g kcal (float)
        food_dic['kcal']=float(line[9])
        """
        #동물크기 size (int)
        if line[9] in division['size'] :
            food_dic['size']=division['size'].index(line[10])

        #사료종목 type (int)
        food_dic['type']=division['type'].index(line[11])

        #제조국 cont (int)
        if line[12] in division['cont'] :
            food_dic['cont']=division['cont'].index(line[12])

        #급여연령 age (int list)
        if line[13] != '' :
            age=line[13].split('~')
            food_dic['age'].append(int(age[0]))
            if age[1] == 'max' : 
                age[1]=10000
            food_dic['age'].append(int(age[1]))

        #유기농여부 org (bool)
        if line[14] == 'O' :
            food_dic['org']=True
        else : food_dic['org']=False
        """
        #키블크기(mm) kib_size (int)
        food_dic['kib_size'] = int(line[15])
        """
        #급여시기 when (int list)
        when = line[16].split(',')
        for w in when :
            w = w.replace(" ","")
            if w in division['when'] :
                food_dic['when'].append(division['when'].index(w))

        #성분비율 nutr (float list)
        for data in line[18:26] :
            if data == "" : data = -1
            food_dic['nutr'].append(float(data))
        
        general_petfood.append(food_dic)

    f.close()
    return general_petfood


def csv_to_dic_division_prescription_petfood() :
    division = {}
    f = open('division_prescription_petfood.csv','r',encoding='utf-8-sig')
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

def csv_to_dic_prescription_petfood(division) :
    f = open('prescription_petfood.csv','r',encoding='utf-8-sig')
    rdr = csv.reader(f)
    prescription_petfood = []

    n=0
    for line in rdr :
        if n == 0 : 
            n+=1
            continue

        food_dic = {
            'pet' : 0,
            'brand' : 0,
            'name' : "no name",
            'price' : 1000000.0,
            'disease' : [],
            'type' : 0,
            'size' : 0,
            'age' : [0,10000],
            'kib_size' : 1000,
            'like' : [],
            'alg' : [],
            'not_when' : str,
            'kcal' : 0.0
        }

        #급여대상 pet (int)
        food_dic['pet']=division['pet'].index(line[0])

        """
        #브랜드 brand (int)
        food_dic['brand']=division['brand'].index(line[1])
        """

        #사료이름 name (string)
        food_dic['name']=line[2]

        """
        #가격/kg price (float)
        food_dic['price']=division['price'].index(line[5])
        """

        #질환 disease (int list)
        disease = line[6].split(',')
        food_dic['disease'] = []
        for d in disease :
            d = d.replace(" ","")
            if d in division['disease'] :
                food_dic['disease'].append(division['disease'].index(d))

        """
        #사료종목 type (int)
        food_dic['type']=division['type'].index(line[8])
        """

        #동물크기 size (int)
        if line[9] in division['size'] :
            food_dic['size']=division['size'].index(line[9])

        #급여연령 age (int list)
        if line[10] != '' :
            age=line[10].split('~')
            food_dic['age'] = []
            food_dic['age'].append(int(age[0]))
            if age[1] == 'max' : 
                age[1]=10000
            food_dic['age'].append(int(age[1]))
        """
        #키블크기(mm) kib_size (int)
        food_dic['kib_size'] = int(line[11])
        """

        #단백질원 like (int list)
        likely = line[12].split(',')
        food_dic['like'] = []
        for l in likely :
            l = l.replace(" ","")
            if l in division['like'] :
                food_dic['like'].append(division['like'].index(l))

        #원료 alg (int like)
        alg = line[13].split(',')
        food_dic['alg'] = []
        for al in alg :
            al = al.replace(" ","")
            if al in division['alg'] and al not in food_dic['alg'] :
                food_dic['alg'].append(division['alg'].index(al))

        #급여시기 not_when (int list)
        food_dic['not_when'] = line[14]

        """
        when = line[14].split(',')
        food_dic['not_when'] = []
        for nw in when :
            nw = nw.replace(" ","")
            if nw in division['not_when'] :
                food_dic['not_when'].append(division['not_when'].index(nw))
        """        
    
        """
        #Kcal/100g kcal (float)
        food_dic['kcal']=float(line[16])
        """
        prescription_petfood.append(food_dic)

    f.close()
    return prescription_petfood