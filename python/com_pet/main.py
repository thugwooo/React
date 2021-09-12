from csv_to_dict import csv_to_dict
import filtering as ft
import cal
test = {
    "pet" : "강아지",
    "name" : "두부",
    "age" : 23,
    "breed" : "전체",
    "sex" : "남",
    "neutral" : "X",
    "weight": 2.8,
    "alg" : [""],
    "flavor" : [""],
    "when" : [""] # 얘 필터링
}

def filter_petfood(input_data):
    input_data = cal.cal_health_factor(input_data)
    filter_data = csv_to_dict()
    
    #강아지 or 고양이 일반식, 자연식, 처방식, 영양제
    filtered_general,filtered_natural, filtered_prescription, filtered_nutrients = ft.filter_pet(filter_data, input_data["pet"])
    
    # 일반식
    # 추가 필터링 when, size
    # 견종별 영양소
    
    filtered_general = ft.filter_age(filtered_general, input_data["age"])
    print("age", len(filtered_general))
    filtered_general = ft.filter_flavor(filtered_general, input_data["flavor"])
    print("flavor", len(filtered_general))
    #filtered_general = ft.filter_breed(filtered_general, input_data["breed"])
    #print("breed", len(filtered_general))
    filtered_general = ft.filter_alg(filtered_general, input_data["alg"])
    print("alg", len(filtered_general))
    
    filtered_general = ft.filter_when(filtered_general, input_data["when"])
    print("when", len(filtered_general))
    #for data in filtered_general:
    #    print(data["alg"])
    #filtered_general =  ft.filter_health(filtered_general, input_data)
    #print("health", len(filtered_general))
    
    # 자연식
    print("natural", len(filtered_natural))
    filtered_natural = ft.filter_age(filtered_natural, input_data["age"])
    print("age", len(filtered_natural))
    filtered_natural = ft.filter_flavor(filtered_natural, input_data["flavor"])
    print("flavor", len(filtered_natural))
    filtered_natural = ft.filter_alg(filtered_natural, input_data["alg"])
    print("alg", len(filtered_natural))
    
    #filtered_natural =  ft.filter_health(filtered_natural, input_data)
    #print("health", len(filtered_general))
    return filtered_general, filtered_natural
filter_petfood(test)
