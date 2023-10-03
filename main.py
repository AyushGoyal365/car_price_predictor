import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
import streamlit as st

# Load the preprocessed car data
car = pd.read_csv("C:\\Users\\goyal\\Desktop\\project python\\car_prize_preduction\\cleaned_car.csv")

# Model building
ohe = OneHotEncoder()

# Exclude 'Price' and 'Unnamed: 0' columns
x = car.drop(columns=['Price', 'Unnamed: 0'])
y = car['Price']
ohe.fit(x[['name', 'company', 'fuel_type']])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

column_trans = make_column_transformer(
    (OneHotEncoder(categories=ohe.categories_), ['name', 'company', 'fuel_type']),
    remainder='passthrough'
)

lr = LinearRegression()

pipe = make_pipeline(column_trans, lr)

pipe.fit(x_train, y_train)

st.title("Car Price Predictor")
def filter_models_by_company(selected_company):
    filtered_models = car[car['company'] == selected_company]['name'].unique()
    return filtered_models
selected_company = st.selectbox("Select the Company", car['company'].unique())

# Get the filtered models based on the selected company
filtered_models = filter_models_by_company(selected_company)

# Create a selectbox for model selection with the filtered models
selected_model = st.selectbox("Select the Model", filtered_models)
year_option = st.selectbox('Select year of purchase', car['year'].unique())
fule_option = st.selectbox('Select the Fule Type',car['fuel_type'].unique())

kilometers = st.text_input('Enter the Number of Kilometers that the Car has Traveled')

if st.button('Predict'):
    
# Create a DataFrame for prediction with the same columns as x_test
    input_data = pd.DataFrame(data=[[0, selected_model , selected_company, year_option, kilometers, fule_option]],
                         columns=['Unnamed: 0', 'name', 'company', 'year', 'kms_driven', 'fuel_type'])

# Drop the 'Unnamed: 0' column
    input_data = input_data.drop(columns='Unnamed: 0')

# Make predictions
    y_pred = pipe.predict(input_data)
    st.write("predicted price is Rs.",y_pred)

