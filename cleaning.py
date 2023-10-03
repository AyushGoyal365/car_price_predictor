
import pandas as pd
import numpy as np

car= pd.read_csv("C:\\Users\\goyal\\Desktop\\project python\\car_prize_preduction\\quikr_car.csv")

# issues in data 
#  year has many non_year values
#year object to int
#price has ask for price
#price object to int
# kms_driven has kms with integers
#kms_driven has nan values
#kms_drivenn object to int 
# fuel_type nan values
# keep first 3 woeds of name 

## Cleaning Data 

car=car[car['year'].str.isnumeric()]

car['year']=car['year'].astype(int)

car=car[car['Price']!='Ask For Price']
car['Price']=car['Price'].str.replace(',','').astype(int) # type: ignore
#car['price'] = car['price'].astype(int)
#print(car['Price']) 

car['kms_driven']=car['kms_driven'].str.split().str.get(0).str.replace(',','')
#car['kms_driven']= car['kms_driven'].str.replace(',','')
car=car[car['kms_driven'].str.isnumeric()]
car['kms_driven']=car['kms_driven'].astype(int)
#print(car['kms_driven'])

car=car[~car['fuel_type'].isna()]

car['name']=car['name'].str.split().str.slice(start=0,stop=3).str.join(' ')

car=car.reset_index(drop=True)


car= car[car['Price']<6e6].reset_index(drop=True)


car.to_csv('cleaned_car.csv')