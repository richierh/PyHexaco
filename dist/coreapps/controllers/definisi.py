from coreapps.models.query import query_referensi_dimensi


def rerata2(jenis_kelamin,Nilai_Dimensi):
    
    ambil_data = query_referensi_dimensi()
#     print (ambil_data)
    
#     list_dimensi = []
    
#     for k,v in Nilai_Dimensi.items():
#         list_dimensi.append([k,v])
    
#     print (list_dimensi)
    
    hasil_data = []
    if jenis_kelamin=="Laki - Laki":
        
        for k,v in Nilai_Dimensi.items():
#             print (k)
            for data in ambil_data:
                if k == data[1]:
#                     print (data[1])
                    if v > data[2]:
#                         print (data[4])
#                         print (data[6])
                        nilai = "Tinggi"
                        hasil_data.append([data[1],data[4],data[6],nilai])
                    
                    else :
                        nilai = "Rendah"
                        hasil_data.append([data[1],data[5],data[7],nilai])
    elif jenis_kelamin=="Perempuan":
        for k,v in Nilai_Dimensi.items():
#             print (k)
            for data in ambil_data:
                if k == data[1]:
#                     print (data[1])
                    if v > data[3]:
#                         print (data[4])
#                         print (data[6])
                        nilai = "Tinggi"
                        hasil_data.append([data[1],data[4],data[6],nilai])
                    
                    else :
                        nilai = "Rendah"
                        hasil_data.append([data[1],data[5],data[7],nilai])





#     print (hasil_data)    
    return hasil_data


            
if __name__=="__main__":
        import sys
        import pathlib
        print (sys.path.append(str(pathlib.Path.cwd()/"coreapps/models")))
        from query import query_referensi_dimensi

#     jenis_kelamin = "Laki - Laki"
        Nilai_Dimensi = {'Sincerity': 4.0, 'Fairness': 2.0, 'Greed Avoidance': 2.5, 'Modesty': 3.5, 'Fearfullness': 4.67, 'Anxiety': 3.0, 'Dependence': 2.0, 'Sentimentality': 2.0, 'Social Self Esteem': 3.33, 'Social Boldness': 4.0, 'Sociability': 2.0, 'Liveliness': 1.0, 'Forgiveness': 3.0, 'Gentleness': 3.67, 'Flexibility': 2.33, 'Patience': 2.5, 'Organization': 1.5, 'Diligence': 1.0, 'Perfectionism': 2.67, 'Prudence': 4.67, 'Aesthetic Appreciation': 3.5, 'Inquisitiveness': 3.0, 'Creativity': 3.0, 'Unconventionality': 1.67, 'Interstitial': 0.0}
        Nilai_Dimensi2 = {'Honesty & Humility': 3.0, 'Emotionality': 2.9175, 'Extraversion': 2.5825, 'Agreeableness': 2.875, 'Conscientiousness': 2.46, 'Openness to Experience': 2.7925, 'Interstitial': 0.0}
        for key,value in Nilai_Dimensi2.items():
                Nilai_Dimensi[key]=value
        
        #     print (rerata("Laki - Laki", Nilai_Dimensi) )
        #     hasils = rerata("Laki - Laki", Nilai_Dimensi)
        #     
        #     for k,v in hasils.items():
        #         print (k,v)
        #     
        # print (Sincerity["Laki - Laki"]["Nilai Median"])
        # print (Sincerity["Nilai Tinggi"])
        #     print (Sincerity["Laki - Laki"][1]["Nilai Tinggi"])


        rerata2("Perempuan",Nilai_Dimensi)


# 
# 
# def rerata(Jenis_kelamin,Nilai_Dimensi):
#     jenis_kelamin = Jenis_kelamin
#     Sincerity = {"Laki - Laki":[{"Nilai Median":3.17},
#                     {"Nilai Tinggi" :"Kecenderungan untuk tulus dalam hubungan interpersonal.  Orang dengan skor tinggi tidak mau memanipulasi orang lain."},
#                     {"Nilai Rendah" :"Kecenderungan untuk tulus dalam hubungan interpersonal. Orang dengan skor rendah akan menyanjung orang lain atau pura-pura menyukai mereka demi mendapatkan bantuan."},
#                     {"Prilaku Tinggi":"-Tulus dalam bekerja\n-Enggan mencurangi orang lain demi kepentiangan pribadi\n-Kooperatif"},
#                     {"Prilaku Rendah":"-Bekerja dengan baik apabila ada imbalan\n-Akan melakukan apa saja untuk mencapai apa yang diharapkan\n-sulit diajak bekerjasama"}],
#                  "Perempuan":[{"Nilai Median":3.31},
#                     {"Nilai Tinggi" :"Kecenderungan untuk tulus dalam hubungan interpersonal.  Orang dengan skor tinggi tidak mau memanipulasi orang lain."},
#                     {"Nilai Rendah" :"Kecenderungan untuk tulus dalam hubungan interpersonal. Orang dengan skor rendah akan menyanjung orang lain atau pura-pura menyukai mereka demi mendapatkan bantuan."},
#                     {"Prilaku Tinggi":"-Tulus dalam bekerja\n-Enggan mencurangi orang lain demi kepentiangan pribadi\n-Kooperatif"},
#                     {"Prilaku Rendah":"-Bekerja dengan baik apabila ada imbalan\n-Akan melakukan apa saja untuk mencapai apa yang diharapkan\n-sulit diajak bekerjasama"}]
#                  }
#     
#     Fairness = {"Laki - Laki":[{"Nilai Median":3.33},
#                     {"Nilai Tinggi" :"Kecenderungan untuk menghindari penipuan dan korupsi.  Orang dengan skor tinggi tidak mau mengambil keuntungan dari orang lain atau masyarakat luas."},
#                     {"Nilai Rendah" :"Kecenderungan untuk menghindari penipuan dan korupsi. Orang dengan skor rendah mau mendapatkan sesuatu dengan curang atau mencuri."},
#                     {"Prilaku Tinggi":""},
#                     {"Prilaku Rendah":""}],
#                  "Perempuan":[{"Nilai Median":3.73},
#                     {"Nilai Tinggi" :""},
#                     {"Nilai Rendah" :""},
#                     {"Prilaku Tinggi":""},
#                     {"Prilaku Rendah":""}]}
#                 
#     Greed_Avoidance = {"Laki - Laki":[{"Nilai Median":2.88},
#                     {"Nilai Tinggi" :""},
#                     {"Nilai Rendah" :""},
#                     {"Prilaku Tinggi":""},
#                     {"Prilaku Rendah":""}],
#                  "Perempuan":[{"Nilai Median":3.11},
#                     {"Nilai Tinggi" :""},
#                     {"Nilai Rendah" :""},
#                     {"Prilaku Tinggi":""},
#                     {"Prilaku Rendah":""}]}
#     
#     Modesty = {"Laki - Laki":[{"Nilai Median":3.22},
#                     {"Nilai Tinggi" :""},
#                     {"Nilai Rendah" :""},
#                     {"Prilaku Tinggi":""},
#                     {"Prilaku Rendah":""}],
#                  "Perempuan":[{"Nilai Median":3.63},
#                     {"Nilai Tinggi" :""},
#                     {"Nilai Rendah" :""},
#                     {"Prilaku Tinggi":""},
#                     {"Prilaku Rendah":""}]}
#     
#     Honesty_Humility = {"Laki - Laki":[{"Nilai Median":3.15},
#                             {"Nilai Tinggi" :""},
#                             {"Nilai Rendah" :""},
#                             {"Prilaku Tinggi":""},
#                             {"Prilaku Rendah":""}],
#                          "Perempuan":[{"Nilai Median":3.45},
#                             {"Nilai Tinggi" :""},
#                             {"Nilai Rendah" :""},
#                             {"Prilaku Tinggi":""},
#                             {"Prilaku Rendah":""}]}
#     
#     Fearfullness = {"Laki - Laki":[{"Nilai Median":2.52},
#                         {"Nilai Tinggi" :""},
#                         {"Nilai Rendah" :""},
#                         {"Prilaku Tinggi":""},
#                         {"Prilaku Rendah":""}],
#                      "Perempuan":[{"Nilai Median":3.12},
#                         {"Nilai Tinggi" :""},
#                         {"Nilai Rendah" :""},
#                         {"Prilaku Tinggi":""},
#                         {"Prilaku Rendah":""}]}
#     
#     Anxiety = {"Laki - Laki":[{"Nilai Median":3.32},
#                     {"Nilai Tinggi" :""},
#                     {"Nilai Rendah" :""},
#                     {"Prilaku Tinggi":""},
#                     {"Prilaku Rendah":""}],
#                  "Perempuan":[{"Nilai Median":3.76},
#                     {"Nilai Tinggi" :""},
#                     {"Nilai Rendah" :""},
#                     {"Prilaku Tinggi":""},
#                     {"Prilaku Rendah":""}]}
#     
#     Dependence = {"Laki - Laki":[{"Nilai Median":2.61},
#                     {"Nilai Tinggi" :""},
#                     {"Nilai Rendah" :""},
#                     {"Prilaku Tinggi":""},
#                     {"Prilaku Rendah":""}],
#                  "Perempuan":[{"Nilai Median":3.08},
#                     {"Nilai Tinggi" :""},
#                     {"Nilai Rendah" :""},
#                     {"Prilaku Tinggi":""},
#                     {"Prilaku Rendah":""}]}
#     
#     Sentimentality = {"Laki - Laki":[{"Nilai Median":2.99},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.58},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Emotionality = {"Laki - Laki":[{"Nilai Median":2.86},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.38},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Social_self_esteem = {"Laki - Laki":[{"Nilai Median":3.61},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.51},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Social_boldness = {"Laki - Laki":[{"Nilai Median":3.10},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":2.99},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Sociability = {"Laki - Laki":[{"Nilai Median":2.97},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.07},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Liveliness = {"Laki - Laki":[{"Nilai Median":3.24},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.28},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Extraversion = {"Laki - Laki":[{"Nilai Median":3.23},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.21},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
# 
#     Forgiveness = {"Laki - Laki":[{"Nilai Median":2.41},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":2.42},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Gentleness = {"Laki - Laki":[{"Nilai Median":2.92},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":2.99},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
# 
#     Flexibility = {"Laki - Laki":[{"Nilai Median":2.68},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":2.75},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
# 
#     Patience = {"Laki - Laki":[{"Nilai Median":3.1},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":2.97},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Agreeableness = {"Laki - Laki":[{"Nilai Median":2.78},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":2.78},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     
#     
#     Organization = {"Laki - Laki":[{"Nilai Median":3.27},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.45},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Diligence = {"Laki - Laki":[{"Nilai Median":3.77},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.81},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Perfectionism = {"Laki - Laki":[{"Nilai Median":3.51},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.59},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     prudence = {"Laki - Laki":[{"Nilai Median":3.44},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.36},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Conscientiouseness = {"Laki - Laki":[{"Nilai Median":3.49},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.55},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Aesthectc_Appreciation = {"Laki - Laki":[{"Nilai Median":3.41},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.64},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Inquitiveness = {"Laki - Laki":[{"Nilai Median":4.04},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.64},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Creativity = {"Laki - Laki":[{"Nilai Median":3.72},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.72},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Unconventionality = {"Laki - Laki":[{"Nilai Median":3.76},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.61},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Openess_to_experience = {"Laki - Laki":[{"Nilai Median":3.73},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.65},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
#     Interstitial = {"Laki - Laki":[{"Nilai Median":3.56},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}],
#          "Perempuan":[{"Nilai Median":3.97},
#             {"Nilai Tinggi" :""},
#             {"Nilai Rendah" :""},
#             {"Prilaku Tinggi":""},
#             {"Prilaku Rendah":""}]}
#     
# #     print (type(Nilai_Dimensi["Sincerity"]))
# #     print (Sincerity["Laki - Laki"][0]["Nilai Median"])
# #     print (Nilai_Dimensi["Sincerity"])
# #     print (type(Sincerity["Laki - Laki"][0]["Nilai Median"]))
# 
#          
#     data = {}
#     if jenis_kelamin == "Laki - Laki":
#         if Nilai_Dimensi["Sincerity"] > Sincerity["Laki - Laki"][0]["Nilai Median"]:
#             data["Sincerity"] = Sincerity["Laki - Laki"][1]
#         else :
#             data["Sincerity"] = Sincerity["Laki - Laki"][2]
# 
#         if Nilai_Dimensi["Fairness"] > Fairness["Laki - Laki"][0]["Nilai Median"]:
#             data["Fairness"] = Fairness["Laki - Laki"][1]
#         else :
#             data["Fairness"] = Fairness["Laki - Laki"][2]
# 
#         if Nilai_Dimensi["Greed Avoidance"] > Greed_Avoidance["Laki - Laki"][0]["Nilai Median"]:
#             data["Greed Avoidance"] = Greed_Avoidance["Laki - Laki"][1]
#         else :
#             data["Greed Avoidance"] = Greed_Avoidance["Laki - Laki"][2]
#      
#         if Nilai_Dimensi["Modesty"] > Modesty["Laki - Laki"][0]["Nilai Median"]:
#             data["Modesty"] = Modesty["Laki - Laki"][1]
#         else :
#             data["Modesty"] = Modesty["Laki - Laki"][2]
# 
# #         if Nilai_Dimensi["Honesty & Humility"] > Honesty_Humility["Laki - Laki"][0]["Nilai Median"]:
# #             data["Honesty & Humility"] = Honesty_Humility["Laki - Laki"][1]
# #         else :
# #             data["Honesty & Humility"] = Honesty_Humility["Laki - Laki"][2]
# #             
#             
#         if Nilai_Dimensi["Fearfullness"] > Fearfullness["Laki - Laki"][0]["Nilai Median"]:
#             data["Fearfullness"] = Fearfullness["Laki - Laki"][1]
#         else :
#             data["Fearfullness"] = Fearfullness["Laki - Laki"][2]
#             
#             
#         if Nilai_Dimensi["Anxiety"] > Anxiety["Laki - Laki"][0]["Nilai Median"]:
#             data["Anxiety"] = Anxiety["Laki - Laki"][1]
#         else :
#             data["Anxiety"] = Anxiety["Laki - Laki"][2]
#         
#         
#         if Nilai_Dimensi["Dependence"] > Dependence["Laki - Laki"][0]["Nilai Median"]:
#             data["Dependence"] = Dependence["Laki - Laki"][1]
#         else :
#             data["Dependence"] = Dependence["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Sentimentality"] > Sentimentality["Laki - Laki"][0]["Nilai Median"]:
#             data["Sentimentality"] = Sentimentality["Laki - Laki"][1]
#         else :
#             data["Sentimentality"] = Sentimentality["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Emotionality"] > Emotionality["Laki - Laki"][0]["Nilai Median"]:
#             data["Emotionality"] = Emotionality["Laki - Laki"][1]
#         else :
#             data["Emotionality"] = Emotionality["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Social Self Esteem"] > Social_self_esteem["Laki - Laki"][0]["Nilai Median"]:
#             data["Social Self Esteem"] = Social_self_esteem["Laki - Laki"][1]
#         else :
#             data["Social Self Esteem"] = Social_self_esteem["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Social Boldness"] > Social_boldness["Laki - Laki"][0]["Nilai Median"]:
#             data["Social Boldness"] = Social_boldness["Laki - Laki"][1]
#         else :
#             data["Social Boldness"] = Social_boldness["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Sociability"] > Sociability["Laki - Laki"][0]["Nilai Median"]:
#             data["Sociability"] = Sociability["Laki - Laki"][1]
#         else :
#             data["Sociability"] = Sociability["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Liveliness"] > Liveliness["Laki - Laki"][0]["Nilai Median"]:
#             data["Liveliness"] = Liveliness["Laki - Laki"][1]
#         else :
#             data["Liveliness"] = Liveliness["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Extraversion"] > Extraversion["Laki - Laki"][0]["Nilai Median"]:
#             data["Extraversion"] = Extraversion["Laki - Laki"][1]
#         else :
#             data["Extraversion"] = Extraversion["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Forgiveness"] > Forgiveness["Laki - Laki"][0]["Nilai Median"]:
#             data["Forgiveness"] = Forgiveness["Laki - Laki"][1]
#         else :
#             data["Forgiveness"] = Forgiveness["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Gentleness"] > Gentleness["Laki - Laki"][0]["Nilai Median"]:
#             data["Gentleness"] = Gentleness["Laki - Laki"][1]
#         else :
#             data["Gentleness"] = Gentleness["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Flexibility"] > Flexibility["Laki - Laki"][0]["Nilai Median"]:
#             data["Flexibility"] = Flexibility["Laki - Laki"][1]
#         else :
#             data["Flexibility"] = Flexibility["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Patience"] > Patience["Laki - Laki"][0]["Nilai Median"]:
#             data["Patience"] = Patience["Laki - Laki"][1]
#         else :
#             data["Patience"] = Patience["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Agreeableness"] > Agreeableness["Laki - Laki"][0]["Nilai Median"]:
#             data["Agreeableness"] = Agreeableness["Laki - Laki"][1]
#         else :
#             data["Agreeableness"] = Agreeableness["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Organization"] > Organization["Laki - Laki"][0]["Nilai Median"]:
#             data["Organization"] = Organization["Laki - Laki"][1]
#         else :
#             data["Organization"] = Organization["Laki - Laki"][2]
# 
#         if Nilai_Dimensi["Diligence"] > Diligence["Laki - Laki"][0]["Nilai Median"]:
#             data["Diligence"] = Diligence["Laki - Laki"][1]
#         else :
#             data["Diligence"] = Diligence["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Perfectionism"] > Perfectionism["Laki - Laki"][0]["Nilai Median"]:
#             data["Perfectionism"] = Perfectionism["Laki - Laki"][1]
#         else :
#             data["Perfectionism"] = Perfectionism["Laki - Laki"][2]
#     
#         if Nilai_Dimensi["Prudence"] > prudence["Laki - Laki"][0]["Nilai Median"]:
#             data["Forgiveness"] = prudence["Laki - Laki"][1]
#         else :
#             data["Forgiveness"] = prudence["Laki - Laki"][2]
# 
# 
#         if Nilai_Dimensi["Conscientiousness"] > Conscientiouseness["Laki - Laki"][0]["Nilai Median"]:
#             data["Conscientiousness"] = Conscientiouseness["Laki - Laki"][1]
#         else :
#             data["Conscientiousness"] = Conscientiouseness["Laki - Laki"][2]
#  
#         if Nilai_Dimensi["Aesthetic Appreciation"] > Aesthectc_Appreciation["Laki - Laki"][0]["Nilai Median"]:
#             data["Aesthetic Appreciation"] = Aesthectc_Appreciation["Laki - Laki"][1]
#         else :
#             data["Aesthetic Appreciation"] = Aesthectc_Appreciation["Laki - Laki"][2]
# 
#         if Nilai_Dimensi["Inquisitiveness"] > Inquitiveness["Laki - Laki"][0]["Nilai Median"]:
#             data["Inquisitiveness"] = Inquitiveness["Laki - Laki"][1]
#         else :
#             data["Inquisitiveness"] = Inquitiveness["Laki - Laki"][2]
# 
#         if Nilai_Dimensi["Creativity"] > Creativity["Laki - Laki"][0]["Nilai Median"]:
#             data["Creativity"] = Creativity["Laki - Laki"][1]
#         else :
#             data["Creativity"] = Creativity["Laki - Laki"][2]
# 
#         if Nilai_Dimensi["Unconventionality"] > Unconventionality["Laki - Laki"][0]["Nilai Median"]:
#             data["Unconventionality"] = Unconventionality["Laki - Laki"][1]
#         else :
#             data["Unconventionality"] = Unconventionality["Laki - Laki"][2]
#  
#         if Nilai_Dimensi["Openness to Experience"] > Openess_to_experience["Laki - Laki"][0]["Nilai Median"]:
#             data["Openness to Experience"] = Openess_to_experience["Laki - Laki"][1]
#         else :
#             data["Openness to Experience"] = Openess_to_experience["Laki - Laki"][2]
#    
#         if Nilai_Dimensi["Interstitial"] > Interstitial["Laki - Laki"][0]["Nilai Median"]:
#             data["Interstitial"] = Interstitial["Laki - Laki"][1]
#         else :
#             data["Interstitial"] = Interstitial["Laki - Laki"][2]
# 
#     elif jenis_kelamin == "Perempuan":
#         if Nilai_Dimensi["Sincerity"] > Sincerity["Perempuan"][0]["Nilai Median"]:
#             data["Sincerity"] = Sincerity["Perempuan"][1]
#         else :
#             data["Sincerity"] = Sincerity["Perempuan"][2]
# 
#         if Nilai_Dimensi["Fairness"] > Fairness["Perempuan"][0]["Nilai Median"]:
#             data["Fairness"] = Fairness["Perempuan"][1]
#         else :
#             data["Fairness"] = Fairness["Perempuan"][2]
# 
#         if Nilai_Dimensi["Greed Avoidance"] > Greed_Avoidance["Perempuan"][0]["Nilai Median"]:
#             data["Greed Avoidance"] = Greed_Avoidance["Perempuan"][1]
#         else :
#             data["Greed Avoidance"] = Greed_Avoidance["Perempuan"][2]
#      
#         if Nilai_Dimensi["Modesty"] > Modesty["Perempuan"][0]["Nilai Median"]:
#             data["Modesty"] = Modesty["Perempuan"][1]
#         else :
#             data["Modesty"] = Modesty["Perempuan"][2]
# 
# #         if Nilai_Dimensi["Honesty & Humility"] > Honesty_Humility["Perempuan"][0]["Nilai Median"]:
# #             data["Honesty & Humility"] = Honesty_Humility["Perempuan"][1]
# #         else :
# #             data["Honesty & Humility"] = Honesty_Humility["Perempuan"][2]
# #             
#             
#         if Nilai_Dimensi["Fearfullness"] > Fearfullness["Perempuan"][0]["Nilai Median"]:
#             data["Fearfullness"] = Fearfullness["Perempuan"][1]
#         else :
#             data["Fearfullness"] = Fearfullness["Perempuan"][2]
#             
#             
#         if Nilai_Dimensi["Anxiety"] > Anxiety["Perempuan"][0]["Nilai Median"]:
#             data["Anxiety"] = Anxiety["Perempuan"][1]
#         else :
#             data["Anxiety"] = Anxiety["Perempuan"][2]
#         
#         
#         if Nilai_Dimensi["Dependence"] > Dependence["Perempuan"][0]["Nilai Median"]:
#             data["Dependence"] = Dependence["Perempuan"][1]
#         else :
#             data["Dependence"] = Dependence["Perempuan"][2]
#     
#         if Nilai_Dimensi["Sentimentality"] > Sentimentality["Perempuan"][0]["Nilai Median"]:
#             data["Sentimentality"] = Sentimentality["Perempuan"][1]
#         else :
#             data["Sentimentality"] = Sentimentality["Perempuan"][2]
#     
#         if Nilai_Dimensi["Emotionality"] > Emotionality["Perempuan"][0]["Nilai Median"]:
#             data["Emotionality"] = Emotionality["Perempuan"][1]
#         else :
#             data["Emotionality"] = Emotionality["Perempuan"][2]
#     
#         if Nilai_Dimensi["Social Self Esteem"] > Social_self_esteem["Perempuan"][0]["Nilai Median"]:
#             data["Social Self Esteem"] = Social_self_esteem["Perempuan"][1]
#         else :
#             data["Social Self Esteem"] = Social_self_esteem["Perempuan"][2]
#     
#         if Nilai_Dimensi["Social Boldness"] > Social_boldness["Perempuan"][0]["Nilai Median"]:
#             data["Social Boldness"] = Social_boldness["Perempuan"][1]
#         else :
#             data["Social Boldness"] = Social_boldness["Perempuan"][2]
#     
#         if Nilai_Dimensi["Sociability"] > Sociability["Perempuan"][0]["Nilai Median"]:
#             data["Sociability"] = Sociability["Perempuan"][1]
#         else :
#             data["Sociability"] = Sociability["Perempuan"][2]
#     
#         if Nilai_Dimensi["Liveliness"] > Liveliness["Perempuan"][0]["Nilai Median"]:
#             data["Liveliness"] = Liveliness["Perempuan"][1]
#         else :
#             data["Liveliness"] = Liveliness["Perempuan"][2]
#     
#         if Nilai_Dimensi["Extraversion"] > Extraversion["Perempuan"][0]["Nilai Median"]:
#             data["Extraversion"] = Extraversion["Perempuan"][1]
#         else :
#             data["Extraversion"] = Extraversion["Perempuan"][2]
#     
#         if Nilai_Dimensi["Forgiveness"] > Forgiveness["Perempuan"][0]["Nilai Median"]:
#             data["Forgiveness"] = Forgiveness["Perempuan"][1]
#         else :
#             data["Forgiveness"] = Forgiveness["Perempuan"][2]
#     
#         if Nilai_Dimensi["Gentleness"] > Gentleness["Perempuan"][0]["Nilai Median"]:
#             data["Gentleness"] = Gentleness["Perempuan"][1]
#         else :
#             data["Gentleness"] = Gentleness["Perempuan"][2]
#     
#         if Nilai_Dimensi["Flexibility"] > Flexibility["Perempuan"][0]["Nilai Median"]:
#             data["Flexibility"] = Flexibility["Perempuan"][1]
#         else :
#             data["Flexibility"] = Flexibility["Perempuan"][2]
#     
#         if Nilai_Dimensi["Patience"] > Patience["Perempuan"][0]["Nilai Median"]:
#             data["Patience"] = Patience["Perempuan"][1]
#         else :
#             data["Patience"] = Patience["Perempuan"][2]
#     
#         if Nilai_Dimensi["Agreeableness"] > Agreeableness["Perempuan"][0]["Nilai Median"]:
#             data["Agreeableness"] = Agreeableness["Perempuan"][1]
#         else :
#             data["Agreeableness"] = Agreeableness["Perempuan"][2]
#     
#         if Nilai_Dimensi["Organization"] > Organization["Perempuan"][0]["Nilai Median"]:
#             data["Organization"] = Organization["Perempuan"][1]
#         else :
#             data["Organization"] = Organization["Perempuan"][2]
# 
#         if Nilai_Dimensi["Diligence"] > Diligence["Perempuan"][0]["Nilai Median"]:
#             data["Diligence"] = Diligence["Perempuan"][1]
#         else :
#             data["Diligence"] = Diligence["Perempuan"][2]
#     
#         if Nilai_Dimensi["Perfectionism"] > Perfectionism["Perempuan"][0]["Nilai Median"]:
#             data["Perfectionism"] = Perfectionism["Perempuan"][1]
#         else :
#             data["Perfectionism"] = Perfectionism["Perempuan"][2]
#     
#         if Nilai_Dimensi["Prudence"] > prudence["Perempuan"][0]["Nilai Median"]:
#             data["Forgiveness"] = prudence["Perempuan"][1]
#         else :
#             data["Forgiveness"] = prudence["Perempuan"][2]
# 
# 
#         if Nilai_Dimensi["Conscientiousness"] > Conscientiouseness["Perempuan"][0]["Nilai Median"]:
#             data["Conscientiousness"] = Conscientiouseness["Perempuan"][1]
#         else :
#             data["Conscientiousness"] = Conscientiouseness["Perempuan"][2]
#  
#         if Nilai_Dimensi["Aesthetic Appreciation"] > Aesthectc_Appreciation["Perempuan"][0]["Nilai Median"]:
#             data["Aesthetic Appreciation"] = Aesthectc_Appreciation["Perempuan"][1]
#         else :
#             data["Aesthetic Appreciation"] = Aesthectc_Appreciation["Perempuan"][2]
# 
#         if Nilai_Dimensi["Inquisitiveness"] > Inquitiveness["Perempuan"][0]["Nilai Median"]:
#             data["Inquisitiveness"] = Inquitiveness["Perempuan"][1]
#         else :
#             data["Inquisitiveness"] = Inquitiveness["Perempuan"][2]
# 
#         if Nilai_Dimensi["Creativity"] > Creativity["Perempuan"][0]["Nilai Median"]:
#             data["Creativity"] = Creativity["Perempuan"][1]
#         else :
#             data["Creativity"] = Creativity["Perempuan"][2]
# 
#         if Nilai_Dimensi["Unconventionality"] > Unconventionality["Perempuan"][0]["Nilai Median"]:
#             data["Unconventionality"] = Unconventionality["Perempuan"][1]
#         else :
#             data["Unconventionality"] = Unconventionality["Perempuan"][2]
#  
#         if Nilai_Dimensi["Openness to Experience"] > Openess_to_experience["Perempuan"][0]["Nilai Median"]:
#             data["Openness to Experience"] = Openess_to_experience["Perempuan"][1]
#         else :
#             data["Openness to Experience"] = Openess_to_experience["Perempuan"][2]
#    
#         if Nilai_Dimensi["Interstitial"] > Interstitial["Perempuan"][0]["Nilai Median"]:
#             data["Interstitial"] = Interstitial["Perempuan"][1]
#         else :
#             data["Interstitial"] = Interstitial["Perempuan"][2]    
#     
#     return data
#  