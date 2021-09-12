def filter_pet(filter_data, key):
    filtered_data = filter_data
    filtered_data = filter(lambda elem:elem["pet"]==key,filtered_data)
    return filtered_data



def filter_breed(filter_data, key):
    filtered_data = []
    for data in filter_data:
        if key == 0:
            filtered_data.append(data)
        elif data["breed"] == key or data["breed"] == 0:
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


def when_filter(filter_data, key):
    if filter_data["when"] in key:
        return True
    else:
        return False
def filter_when(filter_data, key):   # 나중에
    filtered_data = filter_data
    if key:    
        filtered_data = filter(lambda elem: True if elem["when"] in key else False, filtered_data)
    return filtered_data



def filter_size(filter_data, key):
    filtered_data = []
    for data in filter_data:
        if data["size"] == 0 or data["size"] == key:
            filtered_data.append(data)
    return filtered_data



def filter_age(filter_data, key):
    filtered_data = []

    for data in filter_data:

        if key >= data["age"][0] and key <= data["age"][1]:
            
            filtered_data.append(data)
    return filtered_data



def filter_like(filter_data, key):
    filtered_data = []
    for data in filter_data:
        for like_data in data["like"]:
            if like_data in key:
                data["cnt"]+=1   
        if data["cnt"]>0:
            filtered_data.append(data)
    filtered_data.sort(key=lambda x:-x["cnt"])
    return filtered_data



# 여기부턴 처방식 사료

def filter_not_when(filter_data, key):
    filtered_data = filter_data
    for not_when in key:
        filtered_data = filter(lambda elem:elem["not_when"] !=not_when, filtered_data)


def filter_disease(filter_data, key):
    filtered_data = [] 
    for data in filter_data:

        if data["disease"] == key:
            filtered_data.append(data)
    return filtered_data
