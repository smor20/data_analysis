import pandas as pd 
import numpy as np
import streamlit as st
import time

# -----------------------------------------------------------------------------------
# text utility=> title, header, subheader, write, markdown, code, latex
# display elements=> dataframe, metric(card), json
# display media=> image, video
# creating layout=> sidebar, columns.
# showing status=> progress bra, error message(success)
# taking user input=> text input, number input, date input
# buttons, baloons, dropdown, fileuploader.
# -----------------------------------------------------------------------------------

# text utility=> title, header, subheader, write, markdown, code, latex ---------------

# st.title('Startup Dashboard')
# st.header('this is a header displayed using st.header().')
# st.subheader('this is a sub-header displayed using st.subheader().')

# st.write('this is a normal text displayed using st.write().')

# st.markdown('''
#             list of fav movies--
#             - movie a
#             - movie b
#             - movie c
#             ''')

# st.code('''
#         def add_nums(a,b):
#             return (a+b)
#         ''')

# st.latex('x^2+y^2+1=0')

# display elements=> dataframe, metric(card), json ---------------
df_dict={'Name':['a','b','c'],
                  'age':[6,7,8],
                  'class':['1st','2nd','3rd']
                  }
df= pd.DataFrame(df_dict)

st.dataframe(df)

st.metric('Revenue','3L','3%')

# st.json(df_dict)

# display media=> image, video -------------

# st.image('sample_img.jpg')
# st.video()
# st.audio()

# creating layouts=> sidebar columns -----------------
st.sidebar.title('Page Sidebar')

# col1, col2= st.columns(2)

# with col1:
#     st.image('sample_img.jpg')

# with col2:
#     st.image('sample_img.jpg')
    
# showing status=> messages, progress bar -----------------

st.success('login successful')
st.error('login failed')
st.info('this is info')
st.warning('this is warning')

# bar=st.progress(0)
# for i in range(1,101):
#     time.sleep(0.1)
#     bar.progress(i)


# taking user input=> text input, number input, date input -----------------

email=st.text_input('enter email: ')
user_age=st.number_input('enter age: ')
user_dob=st.date_input('enter dob: ')


user_email=st.text_input('enter your email: ')
user_password=st.text_input('enter password: ')
gender=st.selectbox('Select Gender', ['Male','Female','Others'])

btn=st.button('login karo')

if btn:
    if user_email=='abc@gmail.com' and user_password=='1234':
        st.success('login successful')
        # st.balloons()
        st.write(gender)
    else:
        st.error('login failed')
        
file=st.file_uploader('Please upload CSV file:')

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())

