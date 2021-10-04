
import streamlit as st
import base64
import pandas as pd
import pickle
import plotly.express as px
import datetime
from statsmodels.tsa.arima_model import ARIMA
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import timedelta
import time
import datetime
from datetime import datetime, date, time

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

st.title('''Forecasting of Daily Gold Price''')


#st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>Forcasting of daily Gold Price</h1>", unsafe_allow_html=True)


pickle_in = open('arima_model.pkl', 'rb')
forecast = pickle.load(pickle_in)


rad = st.sidebar.radio("Select", ["Home", "Application Description"])
if rad == "Home":
    activities=['Forcasting','Visualisation']
    option=st.sidebar.selectbox('Selection option:',activities)

    if (option=='Visualisation'):
        st.subheader("Input Data and its Distribution")
        data = pd.read_csv("C:/Users/JAYA/OneDrive/gold/venv/new_dataset.csv", header=0, parse_dates=True)
        data_1 = pd.read_csv("C:/Users/JAYA/OneDrive/gold/venv/data1.csv", header=0, parse_dates=True)
        st.dataframe(data)

        if st.checkbox('Display Lineplot'):
            st.line_chart(data['gold'])
        if st.checkbox('Histogram'):
            fig1 = plt.figure(figsize=(25, 20))
            sns.histplot(data['gold'])
            st.pyplot(fig1)
        if st.checkbox('Heatmap'):
            fig2 = plt.figure(figsize=(25, 20))
            heatmap_y_month = pd.pivot_table(data=data_1, values="gold", index="year", columns="month", aggfunc="mean",
                                             fill_value=0)
            sns.heatmap(heatmap_y_month, annot=True, fmt="g")
            st.pyplot(fig2)
        if  st.checkbox('Boxplot'):
            st.subheader("Month wise Distribution of Gold price")
            fig3 = plt.figure(figsize=(25, 15))

            sns.boxplot(x="month", y="gold", data=data_1)
            st.pyplot(fig3)


    elif (option=='Forcasting'):
        data = pd.read_csv("C:/Users/JAYA/OneDrive/gold/venv/new_dataset.csv", header=0, parse_dates=True)
        v = st.number_input('Enter number of days to forcast Gold Prices', value=10)
        start_date = datetime(2021, 7, 21)
        max_days = v
        end_date = (start_date + timedelta(days=max_days)).date()
        index_future_dates = pd.date_range(start=start_date, end=end_date, freq='D')
        Gold = forecast.predict(start=len(data), end=len(data) + max_days, exog=None, typ='levels', dynamic=False)
        df = pd.DataFrame({'Date': index_future_dates, 'gold': Gold})

        if st.button("Predict"):
            current_future_df = pd.concat([data, df])
            df
        if st.checkbox('forecast plot'):
            current_future_df = pd.concat([data, df])
            st.line_chart(current_future_df['gold'])

        if st.checkbox("Future Forecast plot for Selected days Only"):

            fig1 = px.line(df,y=df['gold'],x=df['Date'])

            st.plotly_chart(fig1)

if rad == "Application Description":
    st.header("Purpose")
    st.markdown(
        "** forecasting model which can effectively forecast gold prices for next coming days according to user input.**")
    st.header("Data Description")
    st.markdown(
                " We have data from 4/1/1968 to 7/21/202. ")
    st.header("Adavantages")
    st.markdown(
        """> * Quick Gold Price Forecasting App.""", True)
    st.markdown("""> * Easy to use.""", True)
    st.markdown("""> * User friendly with simple interface.""", True)
    st.markdown("""> * Time saving.""", True)

    st.header("How to Use")
    st.markdown("""**This section describes API user interface.**""", True)
    st.markdown("""> 1. Go to Home.""", True)
    st.markdown(""" Select Foecast option from side menu option for gold price prediction""", True)
    st.markdown("""Enter number of days to forcast Gold Prices""")
    st.markdown("Click on Predict Button")
    st.markdown("""> it will show gold price for future days""", True)
    st.markdown("""> 2. Click on the Forcast plot it will show line plot from 1964 to future date""", True)
    st.markdown("""> 3. Click on Future Forecast plot for Selected days Only.""",True)
    st.markdown("It will show price distribution for only future predicated days")

    st.subheader("Visualization")
    st.markdown(""" select Visualization option from side menu to see the input data distribution""", True)





footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Devloped by Jaya Gupta <a style='display: block; text-align: center;' href="https://github.com/jaya3126" target="_blank">Jaya Gupta</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

