#! usr/bin/env python
'''
Created on May 9, 2019

@author: cireng
'''
# 
data_versi = {'1': '4', '2': '2', '3': '5', '4': '3', '5': '5',
                '6': '4', '7': '1', '8': '1', '9': '1', '10': '1',
                '11': '4', '12': '2', '13': '2', '14': '1',
                '15': '5', '16': '1', '17': '2', '18': '1',
                '19': '5', '20': '1', '21': '4', '22': '1',
                '23': '1', '24': '4', '25': '5', '26': '5',
                '27': '1', '28': '2', '29': '4', '30': '1',
                '31': '1', '32': '5', '33': '2', '34': '2',
                '35': '4', '36': '1', '37': '4', '38': '1',
                '39': '3', '40': '3', '41': '4', '42': '2',
                '43': '3', '44': '2', '45': '3', '46': '5',
                '47': '1', '48': '1', '49': '3', '50': '2',
                '51': '4', '52': '3', '53': '1', '54': '3',
                '55': '5', '56': '1', '57': '3', '58': '5',
                '59': '2', '60': '5'}

# data_versi = {'1': '4', '2': '2', '3': '5', '4': '3', '5': '5',
#                 '6': '4', '7': '1', '8': '1', '9': '1', '10': '1',
#                 '11': '4', '12': '2', '13': '2', '14': '1',
#                 '15': '5', '16': '1', '17': '2', '18': '1',
#                 '19': '5', '20': '1', '21': '4', '22': '1',
#                 '23': '1', '24': '4'}



def hitung_data_mentah(data, data_input):
    human_dict = {}

    for k, v in data_input.items():
        for i in data:

            if i[-1:] == "R":
#                 print(i)
                a = i.replace("R", "")
                nilai_v = {"0":"0","1":"5","2":"4","3":"3","4":"2","5":"1"}
                val = nilai_v.get(v)
#                 print (val)
                
                if k == a:
                    human_dict[str(k)] = int(val)
                
                else:
                    pass
                    
            else :
                pass
              
            if k == i:
#                 print (v)
                human_dict[str(k)] = int(v)
#             print(i)
            else:
                pass
    return sum(human_dict.values()),sum(human_dict.values())/len(data)

def hitung_versi_24(data_versi):
    Sincerity = ["6", "30R", "54"]
    Fairness = ["12R", "36", "60R"]
    Greed_Avoidance = ["18", "42R"]
    Modesty = ["24R", "48R"]

    Fearfullness = ["5", "29", "53R"]
    Anxiety = ["11", "35R"]
    Dependence = ["17", "41R"] 
    Sentimentality = ["23", "47", "59R"]
    
    Social_Self_Esteem = ['4', "28R", "52R"]
    Social_Boldness = ["10R", "34", "58"]
    Sociability = ["16", "40"]    
    Liveliness = ["22", "46R"]    
                
    Forgiveness = ["3", "27"]    
    Gentleness = ["9R", "33", "51"]
    Flexibility = ["15R", "39", "57R"]
    Patience = ["21R", "45"]    
                
    Organization = ["2", "26R"]    
    Diligence = ["8", "32R"]   
    Perfectionism = ["14R", "38", "50"]
    Prudence = ["20R", "44R", "56R"]
                
    Aesthetic_Appreciation = ["1R", "25"]    
    Inquitiveness = ["7", "31R"]    
    Creativity = ["13", "37", "49R"]
    Unconventionality = ["19R", "43", "55R"]
                
    Attristium = ["97", "98"]    
#         

#     
    list_sub_dimensi = [[Sincerity,Fairness,Greed_Avoidance,Modesty],
                        [Fearfullness,Anxiety,Dependence,Sentimentality],
                        [Social_Self_Esteem,Social_Boldness,Sociability,Liveliness],
                        [Forgiveness,Gentleness,Flexibility,Patience],
                        [Organization,Diligence,Perfectionism,Prudence],
                        [Aesthetic_Appreciation,Inquitiveness,Creativity,Unconventionality],
                        [Attristium]] 
       
    sub_dimensi = [["Sincerity", "Fairness", "Greed Avoidance", "Modesty"],
                   ["Fearfullness", "Anxiety", "Dependence","Sentimentality"],
                   ["Social Self Esteem","Social Boldness","Sociability","Liveliness"],
                   ["Forgiveness","Gentleness","Flexibility","Patience"],
                   ["Organization","Diligence","Perfectionism","Prudence"],
                   ["Aesthetic Appreciation","Inquisitiveness","Creativity","Unconventionality"],
                   ["Interstitial"]
                   ]
    
    data_hasil = {}
    data_hasil2= {}
    
#     list_dimensi = ["Honesty & Humility","B","C","D"]
#     Total_Dimensi = {}

#     total = 0
    i_list_sub_dimensi = 0

    for data_sub_dim in list_sub_dimensi:
        
        itter = 0
#         print (data_sub_dim)

        for data_per_sub_dim in list_sub_dimensi[i_list_sub_dimensi]:
#                 print(hitung_data_mentah(data_sub_dim, data_versi))
            data_hasil[sub_dimensi[i_list_sub_dimensi][itter]] = round(hitung_data_mentah(data_per_sub_dim,\
                                                                data_versi)[1],2)
            data_hasil2[sub_dimensi[i_list_sub_dimensi][itter]] = round(hitung_data_mentah(data_per_sub_dim,\
                                                                data_versi)[0],2)

#             print (data_hasil)
            itter += 1
#         print (data_hasil["Sincerity"])

        i_list_sub_dimensi +=1
    
    sum_honesty_humility =  (data_hasil["Sincerity"]+data_hasil["Fairness"]\
                            +data_hasil["Greed Avoidance"]+data_hasil["Modesty"])/4
    
    sum_emotionality = (data_hasil["Fearfullness"] + data_hasil["Anxiety"]\
                        +data_hasil["Dependence"] + data_hasil["Sentimentality"])/4
    
    sum_extraversion = (data_hasil["Social Self Esteem"] + data_hasil["Social Boldness"]\
                        +data_hasil["Sociability"] + data_hasil["Liveliness"])/4
                        
    sum_agreeableness = (data_hasil["Forgiveness"] + data_hasil["Gentleness"]\
                                +data_hasil["Flexibility"]+data_hasil["Patience"])/4
    
    sum_conscientiousness = (data_hasil["Organization"] + data_hasil["Diligence"]\
                            +data_hasil["Perfectionism"] + data_hasil["Prudence"])/4

    sum_openness_to_experience = (data_hasil["Aesthetic Appreciation"]+data_hasil["Inquisitiveness"]\
                                +data_hasil["Creativity"]+data_hasil["Unconventionality"])/4
                                
    sum_interstitial = data_hasil["Interstitial"]
    
    sum_6_dimensi_kepribadian = {
        "Honesty & Humility" : sum_honesty_humility,
        "Emotionality" : sum_emotionality,
        "Extraversion" : sum_extraversion,
        "Agreeableness" : sum_agreeableness,
        "Conscientiousness": sum_conscientiousness,
        "Openness to Experience" : sum_openness_to_experience,
        "Interstitial" : sum_interstitial}
    

#     print (sum_honesty_humility)
#     print (sum_emotionality)
#     print (sum_extraversion)
#     print (sum_agreeableness)
#     print (sum_conscientiousness)
#     print(sum_openness_to_experience)
#     print (sum_interstitial)
    
#     print (data_hasil)
#     print (sum_6_dimensi_kepribadian)
    
    return data_hasil,sum_6_dimensi_kepribadian


def hitung_versi_60(data_versi):
    Sincerity = ["6", "30R", "54"]
    Fairness = ["12R", "36", "60R"]
    Greed_Avoidance = ["18", "42R"]
    Modesty = ["24R", "48R"]

    Fearfullness = ["5", "29", "53R"]
    Anxiety = ["11", "35R"]
    Dependence = ["17", "41R"] 
    Sentimentality = ["23", "47", "59R"]
    
    Social_Self_Esteem = ['4', "28R", "52R"]
    Social_Boldness = ["10R", "34", "58"]
    Sociability = ["16", "40"]    
    Liveliness = ["22", "46R"]    
                
    Forgiveness = ["3", "27"]    
    Gentleness = ["9R", "33", "51"]
    Flexibility = ["15R", "39", "57R"]
    Patience = ["21R", "45"]    
                
    Organization = ["2", "26R"]    
    Diligence = ["8", "32R"]   
    Perfectionism = ["14R", "38", "50"]
    Prudence = ["20R", "44R", "56R"]
                
    Aesthetic_Appreciation = ["1R", "25"]    
    Inquitiveness = ["7", "31R"]    
    Creativity = ["13", "37", "49R"]
    Unconventionality = ["19R", "43", "55R"]
                
    Attristium = ["97", "98"]    
#         

    list_sub_dimensi = [[Sincerity,Fairness,Greed_Avoidance,Modesty],
                        [Fearfullness,Anxiety,Dependence,Sentimentality],
                        [Social_Self_Esteem,Social_Boldness,Sociability,Liveliness],
                        [Forgiveness,Gentleness,Flexibility,Patience],
                        [Organization,Diligence,Perfectionism,Prudence],
                        [Aesthetic_Appreciation,Inquitiveness,Creativity,Unconventionality],
                        [Attristium]] 
       
    sub_dimensi = [["Sincerity", "Fairness", "Greed Avoidance", "Modesty"],
                   ["Fearfullness", "Anxiety", "Dependence","Sentimentality"],
                   ["Social Self Esteem","Social Boldness","Sociability","Liveliness"],
                   ["Forgiveness","Gentleness","Flexibility","Patience"],
                   ["Organization","Diligence","Perfectionism","Prudence"],
                   ["Aesthetic Appreciation","Inquisitiveness","Creativity","Unconventionality"],
                   ["Interstitial"]
                   ]
    
    data_hasil = {}
    data_hasil2 = {}
    
    list_dimensi = ["Honesty & Humility","B","C","D"]
    Total_Dimensi = {}

    total = 0
    i_list_sub_dimensi = 0

    for data_sub_dim in list_sub_dimensi:
        itter = 0
#         print (data_sub_dim)

        for data_per_sub_dim in list_sub_dimensi[i_list_sub_dimensi]:
#                 print(hitung_data_mentah(data_sub_dim, data_versi))
            data_hasil[sub_dimensi[i_list_sub_dimensi][itter]] = round(hitung_data_mentah(data_per_sub_dim,\
                                                                data_versi)[1],2)
            data_hasil2[sub_dimensi[i_list_sub_dimensi][itter]] = round(hitung_data_mentah(data_per_sub_dim,\
                                                                data_versi)[0],2)
#             print (data_hasil)
            itter += 1
#         print (data_hasil["Sincerity"])

        i_list_sub_dimensi +=1
    
    sum_honesty_humility =  (data_hasil["Sincerity"]+data_hasil["Fairness"]\
                            +data_hasil["Greed Avoidance"]+data_hasil["Modesty"])/4
    
    sum_emotionality = (data_hasil["Fearfullness"] + data_hasil["Anxiety"]\
                        +data_hasil["Dependence"] + data_hasil["Sentimentality"])/4
    
    sum_extraversion = (data_hasil["Social Self Esteem"] + data_hasil["Social Boldness"]\
                        +data_hasil["Sociability"] + data_hasil["Liveliness"])/4
                        
    sum_agreeableness = (data_hasil["Forgiveness"] + data_hasil["Gentleness"]\
                                +data_hasil["Flexibility"]+data_hasil["Patience"])/4
    
    sum_conscientiousness = (data_hasil["Organization"] + data_hasil["Diligence"]\
                            +data_hasil["Perfectionism"] + data_hasil["Prudence"])/4

    sum_openness_to_experience = (data_hasil["Aesthetic Appreciation"]+data_hasil["Inquisitiveness"]\
                                +data_hasil["Creativity"]+data_hasil["Unconventionality"])/4
                                
    sum_interstitial = data_hasil["Interstitial"]
    sum_6_dimensi_kepribadian = {
        "Honesty & Humility" : sum_honesty_humility,
        "Emotionality" : sum_emotionality,
        "Extraversion" : sum_extraversion,
        "Agreeableness" : sum_agreeableness,
        "Conscientiousness": sum_conscientiousness,
        "Openness to Experience" : sum_openness_to_experience,
        "Interstitial" : sum_interstitial}
    
    
#     print (sum_honesty_humility)
#     print (sum_emotionality)
#     print (sum_extraversion)
#     print (sum_agreeableness)
#     print (sum_conscientiousness)
#     print(sum_openness_to_experience)
#     print (sum_interstitial)

    print (data_hasil)
    print (sum_6_dimensi_kepribadian)
     
    return data_hasil,sum_6_dimensi_kepribadian

def hitung_versi_100(data_versi):
    Sincerity = ["6", "30R", "54"]
    Fairness = ["12R", "36", "60R"]
    Greed_Avoidance = ["18", "42R"]
    Modesty = ["24R", "48R"]

    Fearfullness = ["5", "29", "53R"]
    Anxiety = ["11", "35R"]
    Dependence = ["17", "41R"] 
    Sentimentality = ["23", "47", "59R"]
    
    Social_Self_Esteem = ['4', "28R", "52R"]
    Social_Boldness = ["10R", "34", "58"]
    Sociability = ["16", "40"]    
    Liveliness = ["22", "46R"]    
                
    Forgiveness = ["3", "27"]    
    Gentleness = ["9R", "33", "51"]
    Flexibility = ["15R", "39", "57R"]
    Patience = ["21R", "45"]    
                
    Organization = ["2", "26R"]    
    Diligence = ["8", "32R"]   
    Perfectionism = ["14R", "38", "50"]
    Prudence = ["20R", "44R", "56R"]
                
    Aesthetic_Appreciation = ["1R", "25"]    
    Inquitiveness = ["7", "31R"]    
    Creativity = ["13", "37", "49R"]
    Unconventionality = ["19R", "43", "55R"]
                
    Attristium = ["97", "98"]    
#         

#     
    list_sub_dimensi = [[Sincerity,Fairness,Greed_Avoidance,Modesty],
                        [Fearfullness,Anxiety,Dependence,Sentimentality],
                        [Social_Self_Esteem,Social_Boldness,Sociability,Liveliness],
                        [Forgiveness,Gentleness,Flexibility,Patience],
                        [Organization,Diligence,Perfectionism,Prudence],
                        [Aesthetic_Appreciation,Inquitiveness,Creativity,Unconventionality],
                        [Attristium]] 
       
    sub_dimensi = [["Sincerity", "Fairness", "Greed Avoidance", "Modesty"],
                   ["Fearfullness", "Anxiety", "Dependence","Sentimentality"],
                   ["Social Self Esteem","Social Boldness","Sociability","Liveliness"],
                   ["Forgiveness","Gentleness","Flexibility","Patience"],
                   ["Organization","Diligence","Perfectionism","Prudence"],
                   ["Aesthetic Appreciation","Inquisitiveness","Creativity","Unconventionality"],
                   ["Interstitial"]
                   ]
    
    data_hasil = {}
    data_hasil2={}
    
#     list_dimensi = ["Honesty & Humility","B","C","D"]
#     Total_Dimensi = {}

#     total = 0
    i_list_sub_dimensi = 0

    for data_sub_dim in list_sub_dimensi:
        itter = 0
#         print (data_sub_dim)

        for data_per_sub_dim in list_sub_dimensi[i_list_sub_dimensi]:
#                 print(hitung_data_mentah(data_sub_dim, data_versi))
            data_hasil[sub_dimensi[i_list_sub_dimensi][itter]] = round(hitung_data_mentah(data_per_sub_dim,\
                                                                data_versi)[1],2)
            data_hasil2[sub_dimensi[i_list_sub_dimensi][itter]] = round(hitung_data_mentah(data_per_sub_dim,\
                                                                data_versi)[0],2)
#             print (data_hasil)
            itter += 1
#         print (data_hasil["Sincerity"])

        i_list_sub_dimensi +=1
    
    sum_honesty_humility =  (data_hasil["Sincerity"]+data_hasil["Fairness"]\
                            +data_hasil["Greed Avoidance"]+data_hasil["Modesty"])/4
    
    sum_emotionality = (data_hasil["Fearfullness"] + data_hasil["Anxiety"]\
                        +data_hasil["Dependence"] + data_hasil["Sentimentality"])/4
    
    sum_extraversion = (data_hasil["Social Self Esteem"] + data_hasil["Social Boldness"]\
                        +data_hasil["Sociability"] + data_hasil["Liveliness"])/4
                        
    sum_agreeableness = (data_hasil["Forgiveness"] + data_hasil["Gentleness"]\
                                +data_hasil["Flexibility"]+data_hasil["Patience"])/4
    
    sum_conscientiousness = (data_hasil["Organization"] + data_hasil["Diligence"]\
                            +data_hasil["Perfectionism"] + data_hasil["Prudence"])/4

    sum_openness_to_experience = (data_hasil["Aesthetic Appreciation"]+data_hasil["Inquisitiveness"]\
                                +data_hasil["Creativity"]+data_hasil["Unconventionality"])/4
                                
    sum_interstitial = data_hasil["Interstitial"]
    
    sum_6_dimensi_kepribadian = {
        "Honesty & Humility" : sum_honesty_humility,
        "Emotionality" : sum_emotionality,
        "Extraversion" : sum_extraversion,
        "Agreeableness" : sum_agreeableness,
        "Conscientiousness": sum_conscientiousness,
        "Openness to Experience" : sum_openness_to_experience,
        "Interstitial" : sum_interstitial}
    

#     print (sum_honesty_humility)
#     print (sum_emotionality)
#     print (sum_extraversion)
#     print (sum_agreeableness)
#     print (sum_conscientiousness)
#     print(sum_openness_to_experience)
#     print (sum_interstitial)
    print (data_hasil)
    print (sum_6_dimensi_kepribadian)  
    
    return data_hasil,sum_6_dimensi_kepribadian

class DimensiHexaco():
    
    def __init__(self, parent, parent2):
        self.parent = parent
        self.parent2 = parent2
        pass
    
    def hitung(self):
        if self.parent == 24 :
            hitungdimensi,hitungsubdimesi=hitung_versi_24(self.parent2)
            pass
        
        elif self.parent == 60 :
            hitungdimensi,hitungsubdimesi=hitung_versi_60(self.parent2)
            
        elif self.parent == 100 :
            hitungdimensi,hitungsubdimesi=hitung_versi_100(self.parent2)
            pass
        
        else :
            print ("ada yang kurang")
            pass
        
        return hitungdimensi,hitungsubdimesi



if __name__ == "__main__":
    
    run = DimensiHexaco(60, data_versi)
    x,y = run.hitung()  
    print ("batas")

    print (x)
    print (y)
# if __name__=="__main__":
#     run = HexacoDimensi(data_versi60)
#     print (run)

