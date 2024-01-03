import streamlit as st
import pandas as pd
# from joblib import load
import pickle

st.title('Income Prediction ML App')



#model_load = load('xgboostbaru1.pkl')
# @st.cache_data

# model_load = pickle.load(open('./model/xgboostbaru1.pkl', 'rb'))
# @st.cache_data
# def model_load():
#        loaded_object = pickle .load(open('./model/xgboostbaru1.pkl', 'rb'))
#        st.write(f"Loaded Object Type: {type(loaded_object)}")
#        return loaded_object
model_load = pickle.load(open('model/xgboostbaru1.pkl', 'rb'))
# # Load model
# with open('./model/xgboostbaru1.pkl', 'rb') as file:
#      model_load = pickle.load(file)

if model_load:
    st.subheader("Fill in the information below to predict income category!")

    age = st.slider('Age', 17, 90, 25)
    workclass = st.selectbox('Workclass', ['State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov',
       'Local-gov', 'Self-emp-inc', 'Without-pay'])
    education = st.selectbox('Education', ['Bachelors', 'HS-grad', '11th', 'Masters', '9th',
       'Some-college', 'Assoc-acdm', '7th-8th', 'Doctorate',
       'Assoc-voc', 'Prof-school', '5th-6th', '10th', 'Preschool',
       '12th', '1st-4th'])
    marital_status = st.selectbox('Marital Status', ['Never-married', 'Married-civ-spouse', 'Divorced',
       'Married-spouse-absent', 'Separated', 'Married-AF-spouse',
       'Widowed'])
    occupation = st.selectbox('Occupation', ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners',
       'Prof-specialty', 'Other-service', 'Sales', 'Transport-moving',
       'Farming-fishing', 'Machine-op-inspct', 'Tech-support',
       'Craft-repair', 'Protective-serv', 'Armed-Forces',
       'Priv-house-serv'])
    relationship = st.selectbox('Relationship', ['Not-in-family', 'Husband', 'Wife', 'Own-child', 'Unmarried',
       'Other-relative'])
    race = st.selectbox('Race', ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo',
       'Other'])
    sex = st.selectbox('Sex', ['Male', 'Female'])
    capital_gain = st.slider('Capital Gain', 0, 99999, 0)
    capital_loss = st.slider('Capital Loss', 0, 4356, 0)
    hours_per_week = st.slider('Hours per Week', 1, 99, 40)
    native_country = st.selectbox('Native Country',['United-States', 'Cuba', 'Jamaica', 'India', 'Mexico',
       'Puerto-Rico', 'Honduras', 'England', 'Canada', 'Germany',
       'Iran', 'Philippines', 'Poland', 'Columbia', 'Cambodia',
       'Thailand', 'Ecuador', 'Laos', 'Taiwan', 'Haiti', 'Portugal',
       'Dominican-Republic', 'El-Salvador', 'France', 'Guatemala',
       'Italy', 'China', 'South', 'Japan', 'Yugoslavia', 'Peru',
       'Outlying-US(Guam-USVI-etc)', 'Scotland', 'Trinadad&Tobago',
       'Greece', 'Nicaragua', 'Vietnam', 'Hong', 'Ireland',
       'Hungary', 'Holand-Netherlands'])


    
    data = {
        
            'workclass':  [workclass],
            'education': [education],
            'marital.status' : [marital_status],
            'occupation': [occupation],
            'relationship': [relationship],
            'race': [race],
            'sex' : [sex],
            'native.country': [native_country],
            'age': [age],
            'capital.gain': [capital_gain],
            'capital.loss': [capital_loss],
            'hours.per.week': [hours_per_week]
    }

    input_df = pd.DataFrame(data)     #, index=[0]
    workclass_mapping = {'State-gov': 1, 'Self-emp-not-inc': 2, 'Private': 3, 'Federal-gov': 4,
       'Local-gov': 5, 'Self-emp-inc':6, 'Without-pay':7}
    education_mapping = {'Bachelors':1, 'HS-grad': 2, '11th': 3, 'Masters':4, '9th':5,
       'Some-college':6, 'Assoc-acdm':7, '7th-8th':8, 'Doctorate':9,
       'Assoc-voc':10, 'Prof-school':11, '5th-6th':12, '10th':13, 'Preschool':14,
       '12th':15, '1st-4th':16}
    marital_mapping = {'Never-married': 1, 'Married-civ-spouse':2, 'Divorced':3,
       'Married-spouse-absent':4, 'Separated':5, 'Married-AF-spouse':6,
       'Widowed':7}
    occupation_mapping = {'Adm-clerical': 1, 'Exec-managerial':2, 'Handlers-cleaners':3,
       'Prof-specialty': 4, 'Other-service': 5, 'Sales': 6, 'Transport-moving':7 ,
       'Farming-fishing': 8, 'Machine-op-inspct': 9, 'Tech-support': 10,
       'Craft-repair': 11, 'Protective-serv': 12, 'Armed-Forces': 13,
       'Priv-house-serv': 14}
    relationship_mapping = {'Not-in-family': 1, 'Husband': 2, 'Wife':3, 'Own-child': 4, 'Unmarried': 5, 'Other-relative': 6  }
    race_mapping = {'White':1, 'Black':2, 'Asian-Pac-Islander': 3, 'Amer-Indian-Eskimo':4, 'Other':5 }
    sex_mapping = {'Male': 1, 'Female': 2}

    native_mapping = {'United-States':1,'Cuba':2, 'Jamaica':3, 'India':4, 'Mexico':5, 'Puerto-Rico':6, 'Honduras':7, 'England':8, 'Canada':9, 'Germany':10,
                      'Iran':11, 'Philippines':12, 'Poland':13, 'Columbia':14, 'Cambodia':15, 'Thailand':16, 'Ecuador':17, 'Laos': 18, 'Taiwan':17, 'Haiti':18, 'Portugal':19, 'Dominican-Republic':20,
                      'El-Salvador':21, 'France':22, 'Guatemala':23, 'Italy': 24, 'China':25, 'South': 26, 'Japan':27, 'Yugoslavia':28, 'Peru':29, 'Outlying-US(Guam-USVI-etc)':30,
                      'Scotland': 31, 'Trinadad&Tobago': 32, 'Greece': 33, 'Nicaragua':34, 'Vietnam': 35, 'Hong': 36, 'Ireland': 37, 'Hungary':38, 'Holand-Netherlands': 39}
  


    input_df['sex'] = input_df['sex'].replace(sex_mapping)
    input_df['workclass'] = input_df['workclass'].replace(workclass_mapping)
    input_df['education'] = input_df['education'].replace(education_mapping)
    input_df['marital.status'] = input_df['marital.status'].replace(marital_mapping)
    input_df['occupation'] = input_df['occupation'].replace(occupation_mapping)
    input_df['relationship'] = input_df['relationship'].replace(relationship_mapping)
    input_df['race'] = input_df['race'].replace(race_mapping)
    input_df['native.country'] = input_df['native.country'].replace(native_mapping)

    


    if st.button('Predict'):
        st.write(input_df)
        result = model_load.predict(input_df)
        if result[0] == 0:
            st.write('<= 50K')
        else:
            st.write('> 50K')
