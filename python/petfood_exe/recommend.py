def recommend_feed(input_data, division, feed_arr) :
    recommend_feed=[]

    #전체 & 해당 종 추천
    def breed_check(feed_dic, input_breed) :
        if feed_dic['breed'] == 0 or feed_dic['breed'] == input_breed : 
            return True
        else : return False

    #하나라도 선호품 있으면 추천
    def likely_check(feed_dic, input_like) :
        for l in input_like :
            if l == -1 : return True
            if l in feed_dic['like'] : return True
        return False

    #하나라도 비선호 있으면 스킵
    def non_likely_check(feed_dic, input_non_like) :
        for no in input_non_like :
            if no == -1 : return True
            if no in feed_dic['like'] : return False
        return True

    #하나라도 알러지가 있으면 스킵
    def allergy_check(feed_dic, input_alle) :
        for al in input_alle :
            if al == -1 : return True
            if al in feed_dic['alle'] : return False
        return True

    def size_check(feed_dic, input_size) :
        if feed_dic['size'] == 0 or feed_dic['size'] == input_size : return True
        else : return False

    def age_check(feed_dic, input_age) :
        if feed_dic['age_low'] <= input_age and input_age <= feed_dic['age_high'] :
            return True
        else : return False


    #특별한 급여시기가 해당되는 경우 그 사료도 추천 가능
    def when_check(feed_dic, input_when) :
        if feed_dic['when'] == 0 : return True

        for w in input_when :
            if w in feed_dic['when'] : return True
            else : continue
        return False

    #걸러서 추천 목록에 추가
    for feed_dic in feed_arr :
        if breed_check(feed_dic, input_data[0]) == False : continue
        if likely_check(feed_dic, input_data[1]) == False : continue
        if non_likely_check(feed_dic, input_data[2]) == False : continue
        if allergy_check(feed_dic, input_data[3]) == False : continue
        if size_check(feed_dic, input_data[4]) == False : continue
        if age_check(feed_dic, input_data[5]) == False : continue
        if when_check(feed_dic, input_data[6]) == False : continue
        else : recommend_feed.append(feed_dic)

    return recommend_feed