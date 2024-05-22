import pandas as pd 
import numpy as np
import streamlit as st
# import time

st.set_page_config(layout='wide', page_title='Startup Analysis')

## Pre-processing to be done on dataset.
    # drop remarks column.
    #set the sr. no. column as index.
    # rename the cols
    # convert amt to CR rupees
    # date col- convert it to datetime format.
    # drop na
## Data preprocessing starts-
    # drop remarks column.

df=pd.read_csv('startup_cleaned.csv')
# st.dataframe(df.head())
def load_investor_details(investor):
    st.title(f'{investor} Analysis')
    # load the recent 5 investments of the investor.
    last_5_df=df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city','round', 'amount']]
    st.subheader('last 5 investments')
    st.dataframe(last_5_df)
    
    # top 5 investments
    top_5_series=df[df['investors'].str.contains(' IDG Ventures')].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
    
    st.subheader('Top 5 investments')
    st.dataframe(top_5_series)

    
startup_list=sorted(df['startup'].unique().tolist())
# df['investors']=df['investors'].fillna('Undisclosed') not required after we got the cleaned data
# st.dataframe(df['investors'].head())
investor_list=sorted(set(df['investors'].str.split(',').sum()))


st.sidebar.title('Startup funding Analysis')
option=st.sidebar.selectbox('Select one',['Overall Analysis','Startup','Invester'])

if option=='Overall Analysis':
    st.title('Overall Analysis')
elif option=='Startup':
    st.sidebar.selectbox('select startup',startup_list)
    btn1=st.sidebar.button('Find startup details')
    st.title('Startup Analysis')

else:
    selected_investor= st.sidebar.selectbox('select investor', investor_list)
    btn2=st.sidebar.button('Find investor details')
    if btn2:
        load_investor_details(selected_investor)
   
    

