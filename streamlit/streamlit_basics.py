import pandas as pd 
import numpy as np
import streamlit as st
import time

st.title('This is a title')
# st.header('this is a header')
# st.subheader('this is a sub-header')

# st.write('hello this is st.write. here you can type normal text.')

# st.markdown('''
#             ## this is a markdown text with 2 hashes.
#             - first bullet point
#             - 2nd bullet point.
#             ''')

# st.code('''
#         lambda x:x**2
#         ''')

# st.latex('''
#          x^2+y^2+5=0
#          ''')

st.metric('Revenue','3L','10%')
# st.json({'name':'abc','age':23,'gender':'M'})

## Display Media - images, video
# st.image('chrome.png')
# st.video('video name.extn')

## Creating Layouts - sidebad; Columns

# st.sidebar.title('Sidebar title')

# clolumns -  give num of columns for a row as a placeholder

# col1, col2=st.columns(2)
# with col1:
#     st.image('sam.jpg')
# with col2:
#     st.metric('Profit','10L','20%')
# with col2:
#     st.image('chrome.png')
    
## ****** Showing status - Error msg; Progress Bar. ********

# st.success('Ban gi Baat')
# st.error('error aa gya re baba!')
# st.info('this is info msg')
# st.warning('this is warning msg..')

# progress bar
# bar=st.progress(0)
# for i in range(1,101):
#     time.sleep(0.01)
#     bar.progress(i)


## Displaying a input dataframe
# df=pd.read_csv('startup_funding.csv')
# st.dataframe(df)

## taking user input - text/number/date
# name=st.text_input('enter your name')
# age=st.number_input('enter your age')
# date=st.date_input('enter a date')




# name=st.text_input('enter your name')
# password=st.text_input('enter your password')
# gender= st.selectbox('select Gender',['M','F','Other'])
# btn=st.button('Login')

# if btn:
#     if name=='abc' and password=='1234':
#         st.success('Login successful')
#         st.write(gender)
#         # st.balloons()
#     else:
#         st.error('Incorrect name/Password')

# ## Dropdown(st.selectbox & st.multibox is used )
# gender1= st.selectbox('select Gender1',['M','F','Other'])
# st.write(gender)

file=st.file_uploader('upload a csv file')

if file is not None:
    df1=pd.read_csv(file)
    st.dataframe(df1)


## AxiosError: Request failed with status code 403 -- how to resolve
# 1st Way
    # from CLI run streamlit app with the below command
    # streamlit run app_name.py --server.enableXsrfProtection=false --server.enableCORS=false
# 2nd Way
    # from streamlit import config as _config
    # from streamlit.web.bootstrap import run
    # _config.set_option("server.headless", True)
    # run("your_app.py", args=[], flag_options={"server.enableXsrfProtection": False, "server.enableCORS": False}, is_hello=False)
