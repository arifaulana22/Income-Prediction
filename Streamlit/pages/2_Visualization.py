import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from data_cleaned.csv
df = pd.read_csv('Streamlit/dataset/data_cleaned.csv')


st.title('Income Prediction Boxplot Visualization')

# Sidebar dengan tab dan select box
tab_selector = st.sidebar.radio("Select Visualization", ["Boxplot", "Other Visualization"])
selected_feature = st.sidebar.selectbox("Select Feature", df.columns)

# Boxplot

if tab_selector == "Boxplot":
    st.subheader(f'Boxplot of {selected_feature} by Income Category')

    # Create a boxplot using seaborn
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='income', y=selected_feature, data=df)
    plt.title(f'Boxplot of {selected_feature} by Income Category')
    plt.xlabel('Income Category')
    plt.ylabel(selected_feature)
    st.pyplot(plt)

