# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yBdDfhM-oU3CHf4lnyRkRNuHsVzGzwt3
"""

import pandas as pd
baza={
    "FISH":["Tursunov Muhammadqodir","Otabekova Jamila","Muhammadaliyev Abdullo","Yoldoshev Husniddin","Tohirova Sarvinoz","Tursunova Robiya",'Dadahonov Dilshodbek',"Burhonova Soliha","Aliyev Vali","Turg'unov Abdulvosit"],
    "Yoshi":["20","15","21","19","24","16","23","20","19","19"],
    "Maktabi":["24 - maktab","1 - maktab","55-maktab","33-maktab","2-maktab","1-maktab","62-maktab","3-maktab","72-maktab","7-maktab"],
    "Jinsi":["erkak","ayol","erkak","erkak","ayol","ayol","erkak","ayol","erkak","erkak"],
   "Manzili":["Shahrixon tumani","Marsdan","Namangan","Besh ariq","Farg'ona shahri","chinobot", "Shahrixon","Fargona shahri","Shahrixon tumani","Shahrixon tumani"],



}
db=pd.DataFrame(baza)
print(db)

filtr=db[db['Jinsi']=="ayol"]
print(filtr)

filtr=db[(db['Jinsi']=="erkak") & (db['Yoshi']=="19")]
print(filtr)