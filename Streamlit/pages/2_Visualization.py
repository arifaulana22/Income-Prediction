import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Load data from data_cleaned.csv
df = pd.read_csv('dataset/data_cleaned.csv')


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






# Load dataset (gunakan dataset income prediction Anda)
df = pd.read_csv('dataset/data_cleaned.csv')

# Sidebar untuk pemilihan visualisasi
selected_visualization = st.sidebar.selectbox(
    'Pilih Visualisasi',
    ('Histogram', 'Pie Chart', 'KDE Plot')
)

# Fungsi caching untuk menghindari pembacaan berulang dataset
@st.cache_data
def load_data():
    return df

# Visualisasi pertama: Histogram
if selected_visualization == 'Histogram':
    st.title('Histogram Age')
    
    data = load_data()
    
    fig = px.histogram(data, x='age', nbins=20, title='Histogram Age')
    st.plotly_chart(fig)

# Visualisasi kedua: Pie Chart
elif selected_visualization == 'Pie Chart':
    st.title('Pie Chart Distribusi Kelas Income')
    
    data = load_data()
    
    income_counts = data['income'].value_counts()
    labels = income_counts.index
    values = income_counts.values
    
    fig = px.pie(data, names='income', title='Distribusi Kelas Income')
    st.plotly_chart(fig)

# Visualisasi ketiga: KDE Plot
elif selected_visualization == 'KDE Plot':
    st.title('KDE Plot of Age')
    
    data = load_data()
    
    # Create a KDE plot using seaborn
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data['age'], shade=True)
    plt.title('KDE Plot of Age')
    plt.xlabel('Age')
    plt.ylabel('Density')
    st.pyplot(plt)



