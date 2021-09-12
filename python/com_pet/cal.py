from datetime import date, datetime, timedelta

def cal_kcal(general_pet_food_dict, natural_pet_food_dict, input_data):
    plan_percent = [1, 0.75, 0.5, 0.25, 0]
    petfood = [[0,0,0],[0,0,0]] #100g당 칼로리, 사료 총량(g), 사료 가격 // 일반식, 자연식

    petfood[0][0] = general_pet_food_dict['kcal']
    petfood[0][1] = general_pet_food_dict['amount']
    petfood[0][2] = general_pet_food_dict['price']

    petfood[1][0] = natural_pet_food_dict['kcal']
    petfood[1][1] = natural_pet_food_dict['amount']
    petfood[1][2] = natural_pet_food_dict['price']
    
    weight = input_data['weight']
    day_kcal = 70 * (weight ** 0.75) * input_data["factor"]
    month_kcal = int(day_kcal * 30)
    dry_buy = round(month_kcal/(petfood[0][0]/100*petfood[0][1]),2)
    fresh_buy = round(month_kcal/(petfood[1][0]/100*petfood[1][1]),2)
    plan = [0,0,0,0,0]

    plan[0] = int(dry_buy*plan_percent[0]*petfood[0][2] +fresh_buy*plan_percent[4]*petfood[1][2])
    plan[1] = int(dry_buy*plan_percent[1]*petfood[0][2] +fresh_buy*plan_percent[3]*petfood[1][2])
    plan[2] = int(dry_buy*plan_percent[2]*petfood[0][2] +fresh_buy*plan_percent[2]*petfood[1][2])
    plan[3] = int(dry_buy*plan_percent[3]*petfood[0][2] +fresh_buy*plan_percent[1]*petfood[1][2])
    plan[4] = int(dry_buy*plan_percent[4]*petfood[0][2] +fresh_buy*plan_percent[0]*petfood[1][2])

    return plan, month_kcal, day_kcal

def cal_factor(input_data):
    factor = [[2.5, 1.8, 1.6, 1.4, 1.2, 0.9, 2, 1.4],[3.5, 1.4, 1.2, 1.1, 1, 0.8, 1.8, 1.1]]  # 강아지 / 고양이
    # 4 비만의 징후 / 5 심각한 비만
    if input_data["pet"] == "강아지":
        pet = 1
    elif input_data["pet"] == "고양이": 
        pet = 2

    if input_data["when"] == "수유기":      input_data["factor"] = factor[pet][7]
    elif "임신기" in input_data["when"] :    input_data["factor"] = factor[pet][6]
    elif 96 <= input_data["age"] :          input_data["factor"] = factor[pet][3]
    elif input_data["age"] < 12:            input_data["factor"] = factor[pet][0]
    elif input_data["neutering"] == 1 :     input_data["factor"] = factor[pet][2]
    else:                                   input_data["factor"] == factor[pet][1]

    return input_data

def cal_age(input_data):

    input_data["age"] = (datetime.now() - datetime.strptime(input_data["date"],'%Y-%m-%d') ).days // 30
    return input_data

def cal_health_factor(input_data):
    # 1번 추가하기
    if input_data["pet"] == "강아지":
        if "임신기" in input_data["when"]:
            input_data["health_factor"] = 4
        elif "수유기" in input_data["when"]:
            input_data["health_factor"] = 5
        elif 85 < input_data["age"]:
            input_data["health_factor"] = 3
        elif input_data["age"] <12:
            input_data["health_factor"] = 0
        else :
            input_data["health_factor"] = 2
    return input_data
