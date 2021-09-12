import filtering as ft
import read_csv



def main(test):

    if test["case"] == 1:
        division_general_petfood_dic = read_csv.csv_to_dic_division_general_petfood()
        general_petfood_list = read_csv.csv_to_dic_general_petfood(division_general_petfood_dic)

        
        filtered_data = general_petfood_list
        """
        for data in filtered_data:
            print(data)
        """
        filtered_data = ft.filter_pet(filtered_data, test["pet"])
        filtered_data = ft.filter_breed(filtered_data, test["breed"])
        #filtered_data = ft.filter_alg(filtered_data, test["alg"])
        #filtered_data = ft.filter_when(filtered_data, test["when"])
        #filtered_data = ft.filter_size(filtered_data, test["size"])
        #filtered_data = ft.filter_age(filtered_data, test["age"])
        filtered_data = ft.filter_like(filtered_data, test["like"])

        result = list(filtered_data)

        for data in result:
            print(data)
        print(len(result))


        

    elif test["case"] == 2:  #처방식

        division_prescription_petfood_dic = read_csv.csv_to_dic_division_prescription_petfood()
        prescription_petfood_list = read_csv.csv_to_dic_prescription_petfood(division_prescription_petfood_dic)

        filtered_data = prescription_petfood_list

        for data in filtered_data:
            print(data)

        #
        # print("first",len(list(filtered_data)))


        filtered_data = ft.filter_size(filtered_data, test["size"])
        print("size",len(list(filtered_data)))

        filtered_data = ft.filter_age(filtered_data, test["age"])
        print("age",len(list(filtered_data)))

        #filtered_data = ft.filter_not_when(filtered_data, test["when"])
        #print("not_when",len(list(filtered_data)))

        filtered_data = ft.filter_alg(filtered_data, test["alg"])
        #print("alg",len(list(filtered_data)))

        filtered_data = ft.filter_disease(filtered_data, test["disease"])



        result = list(filtered_data)
        print(len(result))
        for data in result:
            print(data["name"])
    return result