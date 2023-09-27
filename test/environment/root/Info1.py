import streamlit as st
import time
import numpy as np
# from streamlit_modal import Modal
# from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Info 1")

st.markdown("# 안녕하세요:) 프로어스입니다!")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")

st.sidebar.header("☝️ STEP 1️") 
st.sidebar.header("🤞 STEP 2") 
st.sidebar.header("!! STEP 3") 

name = st.text_input("이름을 입력해주세요")
age = st.slider('나이를 알려주세요',0,50,25,1)

gender = ['여자', '남자']
gender_choice = st.selectbox("Gender", gender)
if gender == gender[0]:
    print(0)
else:
    print(1)
    
height = st.text_input("키가 궁금해요")
weight = st.number_input("몸무게는요")


# st.button("Re-run")
    
# pages = get_pages("want.py")
    
# con = st.container()
    