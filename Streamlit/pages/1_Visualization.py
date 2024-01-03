import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset (gunakan dataset income prediction Anda)
df = pd.read_csv('dataset/data_cleaned.csv')

# Sidebar untuk pemilihan visualisasi
selected_visualization = st.sidebar.selectbox(
    'Pilih Visualisasi',
    ('Histogram', 'Pie Chart')
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
