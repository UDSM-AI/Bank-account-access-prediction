import streamlit as st

# Title
st.title('Financial Inclusion in Africa')

# Header
st.text('Forecasting Weather a person in likely to have a bank account or not')

# divider line
st.write('---')

# subheader
st.subheader('Overview of the challenge')

# text

# Background and Objective
st.write("""
#### Background:
A prominent financial institution operating in East Africa is committed to fostering financial inclusion and reaching underserved populations. To achieve this, the institution is leveraging predictive modeling to identify potential clients who are likely to benefit from their banking services.

#### Objective:
The primary goal is to use machine learning models to predict which individuals are most likely to have a bank account. By doing so, the financial institution aims to streamline its outreach efforts, tailor services, and extend banking access to those who may not have traditionally engaged with formal financial services.
""")

# Solution Overview
st.write("""
#### Solution Overview:
The financial institution draws insights from demographic information and financial services usage data collected from a diverse pool of approximately 33,600 individuals across the East African countries of Kenya, Rwanda, Tanzania, and Uganda. Using a sophisticated binary classification model, we predict the likelihood of an individual having a bank account.
""")