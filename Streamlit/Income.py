import streamlit as st

st.set_page_config(
    page_title="Income Prediction",
)

st.markdown("# Welcome to My Streamlit!! 👋")

st.markdown(
    """
    Welcome Everyone!
    
This dataset is about data income in US per year.

Target is <=50K per year or >50K per year


"""
)

# Penjelasan awal Hello
st.markdown("""🌐 Source Data (https://code.datasciencedojo.com/datasciencedojo/datasets/tree/master/Census%20Income) """)


st.markdown("""### Full Presentation [Portfolio](https://bit.ly/49bgnAZ) """)

st.markdown(
    """
    Thank you for checking out my portfolio! Before exploring this Streamlit app, feel free to take a look at my other projects. 🚀📁
    - ⛔ **Machine Learning Model to Predict Hotel Booking Cancellation** [Don't Cancel!](https://bit.ly/3Su89hM)
    - 📦 **Here another portofolio and my finished project (https://bit.ly/3Sx1CBR)
"""
)

st.markdown(
    """
 # Model 🤖
# **- XGBoost **
"""
)

st.markdown(
    """
Using XGBoost, I trained the model to predict income people are <=50K or >50K $ per years.

These are the error metrics; it has good precision, Recall, and F1 score values. The model didn't experience overfitting or underfitting one factor can see from stable value in train and test.

""")

st.image('xgboost.png', caption='Model Performance', use_column_width=True)

st.markdown("## Evaluation Metriks")


# Display the DataFrame with specified precision
st.image('result.png', caption='Model Performance', use_column_width=True)

st.markdown(
    """
    **👈 Select any pages from the sidebar** to see some demonstration!

    Enjoy! Critiques and suggestions are welcome, you can contact me at:
    - 📨 arifmaulana22597@gmail.com
    - 👷 Let's get connected on [LinkedIn](https://www.linkedin.com/in/arif-maulana22/)
    - 💻 https://github.com/arifaulana22
"""
)



