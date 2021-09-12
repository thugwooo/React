


def filter_pet(filter_data, key):
    filtered_general = []
    filtered_natural = []
    filtered_prescription = []
    filtered_nutrients = []
    
    for data in filter_data:
        if data["pet"] == key:
            if data["food_type"] == "일반식":
                filtered_general.append(data)
            elif data["food_type"] == "자연식":
                filtered_natural.append(data)
            elif data["food_type"] == "처방식":
                filtered_prescription.append(data)
            elif data["food_type"] == "영양제":
                filtered_nutrients.append(data)
    
    return filtered_general, filtered_natural, filtered_prescription, filtered_nutrients


def filter_age(filter_data, key):
    filtered_data = []
    
    for data in filter_data:
        if data["age"][0] <= key <= data["age"][1]:
            filtered_data.append(data)
    
    return filtered_data


def filter_flavor(filter_data, key):
    filtered_data = []
    
    for data in filter_data:
        cnt = 0
        for flavor_data in data["flavor"]:
            if flavor_data in key:
                cnt+=1
        if cnt>0 or key[0] == [""]:
            data["cnt"] = cnt
            filtered_data.append(data)
    return filtered_data


def filter_breed(filter_data, key):
    filtered_data = []
    for data in filter_data:
        if data["breed"] == key or data["breed"] == "전체":
            filtered_data.append(data)
    return filtered_data

def filter_health(filter_data, input_data):
    # 단백질, 지방, 칼슘, 인, 칼슘/인 비율, 식이섬유
    health_factor = [
        [[22, 32], [10,25], [0.7, 1.7], [0.6, 1.3], [1,1.8], [0,100]],
        [[20, 32], [8, 14], [0.7, 1.4], [0.6, 1.1], [1,1.5], [0,100]],
        [[15, 30], [5,100], [0.5, 0.8], [0.4, 0.6], [0,100], [0,5]],
        [[15, 23], [7, 15], [0.5, 1.0], [0.25, 0.75], [0,100], [2,100]],
        [[22, 32], [10,25], [0.7, 1.5], [0.6,1.3], [1,1.5], [0,5]],
        [[25, 35], [18,100], [0.75, 1.7], [0.6, 1.3], [1,1.5], [0,5]]
    ]
    filtered_data = []
    factor = health_factor[input_data["health_factor"]]
    for data in filter_data:
        if factor[0][0] <= data["nutr"][1] <= factor[0][1]: 
            if factor[1][0] <= data["nutr"][2] <= factor[1][1]:
                if factor[2][0] <= data["nutr"][5] <= factor[2][1]:
                    if factor[3][0] <= data["nutr"][6] <= factor[3][1]:
                        if factor[4][0] <= data["nutr"][5] / data["nutr"][5] <= factor[4][1]:
                            if factor[5][0] <= data["nutr"][4] <= factor[5][1]:
                                filtered_data.append(data)
    return filtered_data
                            
def filter_alg(filter_data, key):
    filtered_data = []
    for data in filter_data:
        flag = True
        for alg_data in data["alg"]:
            if alg_data in key:
                flag = False
                break
        if flag == True:
            filtered_data.append(data)
    
    return filtered_data

def filter_when(filter_data, key):
    filtered_data = []
    for data in filter_data:
        flag = False
        for when_data in key:
            if when_data in data["when"]:
                flag=True
        if flag or key == [""]:
            filtered_data.append(data)
    return filtered_data