import csv
import filtering
def csv_to_dict():
    data = []
    with open('King File.csv', encoding='utf-8-sig') as csvfile:
        rdr = csv.DictReader(csvfile)
        for line in rdr:
            dic_data = {
                "pet": "",
                "brand" : "",
                "name" : "",
                "food_type" : "",
                "size" : "",
                "age" : "",
                "flavor" : [],
                "alg" : [],
                "health" : [],
                "main_eff" : "",
            }

            dic_data["pet"] = line["급여대상"]
            dic_data["brand"] = line["브랜드"]
            dic_data["name"] = line["이름"]
            dic_data["food_type"] = line["사료 형태"]
            dic_data["size"] = line["동물크기"]
            dic_data["age"] = line["급여연령"]
            dic_data["flavor"] = [flavor_data.strip() for flavor_data in line["Mainflavor"].split(",")]
            dic_data["alg"] = [alg_data.strip() for alg_data in line["알레르기"].split(",")]
            dic_data["health"] = [dis_data.strip() for dis_data in line["건강 개선"].split(",")]
            dic_data["main_eff"] = line["사료 해석"]
            data.append(dic_data)
    
    return data
petData = {'flavor':['닭'], 'alg':['소','양'], 'health':['눈물']}

petfood = csv_to_dict()
petfood = filtering.filter_flavor(petfood, petData['flavor'])
print(len(petfood))
petfood = filtering.filter_alg(petfood, petData['alg'])
print(len(petfood))

petfood = filtering.filter_health(petfood, petData['health'])
print(len(petfood))