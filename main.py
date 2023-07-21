import streamlit as st
import pandas as pd
import openai_helper


col1, col2 = st.columns([3,2])

financial_dataframe = pd.DataFrame({"Measure":['Company Name','Stock Symbol','Revenue','Net Income','EPS'],
        "Value":["","","","",""]})

with col1:
    st.title("Financial Data Extraction Tool")
    news_article = st.text_area("Paste your financial news article here",height=300)
    if st.button("Extract"):
        financial_dataframe = openai_helper.exract_financial_data(news_article)

with col2:
    st.markdown("<br/>"*7,unsafe_allow_html=True) #Creates 5 lines of vertical space
    st.dataframe(financial_dataframe, 
                 column_config={
                     "Measure": st.column_config.Column(width=150),
                     "Value": st.column_config.Column(width=150)
                 },
                 hide_index=True
    )