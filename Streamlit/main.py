import streamlit as st
import pandas as pd
import time as ts
import time 
from datetime import time
import matplotlib.pyplot as plt
import numpy as np


#-----------------ELEMENTS---------------------
#for writing title
st.title("Hi! I m streamlit web app")  

#for sub-headings
st.subheader("This is sub-heading")

#headers
st.header("i m headers")

#for text (similar to <p> tag in html)
st.text("This is text,This is text,This is text,This is text")

#to bold the text **text** to be bolded
st.markdown("**Hello** world")
st.markdown("Hello **world**")

#to make italic *text* to be italic
st.markdown("*Hello* world")
st.markdown("Hello *world*")

#for using h1 tag we use # before text from h1-h6
st.markdown("# Hello world")  #h1
st.markdown("## Hello world")  #h2

#for block-code we use '>' before text
st.markdown("> Hello world")
st.markdown(">> Hello world")

#for horizontal line we use --- 
st.markdown("---")

#to add links
st.markdown("[Goggle](https://www.google.com)")

#for captions
st.caption("This is caption")

#to have mathematical equations
st.latex("e=mc^2")

#for json format
json={'name':'John', 'age':30, 'city':'New York'}
st.json(json)

#for codes
code = """
print("hellow world")
def fun():
    return 0;"""
st.code(code)

code = """
print("hellow world")
def fun():
    return 0;"""
st.code(code , language='python')

#using write function we can have everything for markdown , code or json and many more
st.write("## Hello world")

#metric fun
st.metric(label="Temperature", value="70 °F" , delta="1.2 °F")
st.metric(label="Temperature", value="70 °F" , delta="-1.2 °F")

#for dataframes making tables 
table = pd.DataFrame({
    'name':['John', 'Anna', 'Peter', 'Linda'],
    'age':[24, 13, 53, 33]
})
st.table(table) 
st.dataframe(table)



#------------------WIDGETS---------------------
#for image
st.image("image.jpeg")
st.image("image.jpeg", caption="This is my bird image" , width=300)

#for audio
st.audio("audio.mp3")

#for vedio
st.video("vedio.mp4")

#for checkbox
# st.checkbox("chechbox")
# st.checkbox("chechbox" , value=True)

state=st.checkbox("i m checkbox")
if state:
    st.write("checked")
else:
    pass

#on_chnge property
def change():
    print("changed")
st.checkbox("chechbox" , value=True , on_change=change)


#radio buttons
st.radio("in which country do you live?", ('India', 'USA', 'UK', 'Other'))

#buttons
def btn_click():
    print("button clicked")
st.button("Click me",on_click=btn_click)

#select boxes
st.selectbox("Select your age", [10,20,30,40,50])
st.multiselect("choose you fav food", ["dosa","samosa","black-cuurent","sandwich"])

#uploading files 
#st.file_uploader("please upload a file" , type=["pdf","png","jpg","jpeg","mp4","mp3","docx"])
image = st.file_uploader("please upload a file" , type=["pdf","png","jpg","jpeg","mp4","mp3","docx"] , accept_multiple_files=True)
if image is not None:
    st.image(image)
    
    
#slider for defining min amd max value 
st.slider("choose the appropriate ph" , min_value=0 , max_value=14 , value=7)

#area - for paras , eassy , descriptive answer
st.text_area("Enter your address")

#for single line
st.text_input("Enter your name" , max_chars=10)

#for dates
st.date_input("Enter your dob")

#for times
val = st.time_input("Enter time" , value=time(0,0,0))

#progress bar
st.progress(20)

if str(val) == "00:00:00":
    st.write("please sset timer")
else:
    bar=st.progress(0)
    for i in range(10):
       bar.progress((i+1)*10)
       ts.sleep(1)
    
#--------------FORMS-------------
st.markdown("## USER-REGISTRATION FORM")
# form=st.form("form1")
# form.text_input("Enter your name")
# form.form_submit_button("Submit")

with st.form("form2"):
    col1,col2=st.columns(2)
    col1.text_input("first name")
    col2.text_input("last name")
    st.text_input("enter you email")
    col3,col4=st.columns(2)
    col3.text_input("create password")
    col4.text_input("re-type your password")
    day,month,year=st.columns(3)
    day.text_input("day")
    month.text_input("month")
    year.text_input("year")
    st.form_submit_button("Submit")
    
#------sidebar-----
st.sidebar.write("hello, this is my sidebar")


#---------------matplotlib charts--------
opt=st.sidebar.radio("select any graph:" , ("bar","line","pie"))
if opt=="line":
    fig=plt.figure()
    plt.style.use('ggplot')
    x=np.linspace(0,10,100)
    plt.plot(x,np.sin(x))
    st.write(fig)
    
elif opt=="bar":
    fig=plt.figure()
    x=np.linspace(1,6)
    plt.style.use('ggplot')
    plt.plot(x,x*10)
    
