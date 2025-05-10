
### First you streamlit run streamlit_deployment.py
## python -m streamlit run streamlit_deployment.py


import streamlit as st
import time
from PIL import Image


st.title("Machine Learning Model Deployment...")


## Header 
st.header("Introduction: This is subheader")



st.text("This is text Mac...")

input_text = st.text("Type something Jackass..", "Type here....")
st.text(input_text)


input_text = st.text_area("Enter here", "this is large text area")

st.markdown("RThis text is  really important")
st.markdown("### This is a heading")
st.markdown(""" 1. firdt item
            2. second item""")

button = st.button("Click me")
st.text("Button is clicked...")
if button:
    st.text("I am clicked...")
    st.info("I am clicked. Snap me fast....")
    st.toast("I am dissapeared")
    st.warning("This warning...")
    st.error("this is an error")

## Image....

st.image("C:\Users\chris' pc\aws_sentiment_program\steamlit_production\aic-home.jpg", width= 100)

img = Image.open("C:\Users\chris' pc\aws_sentiment_program\water-5393919_1280.jpg")
st.image(img, width=100)

## Check bot widget....

flag = st.checkbox("Select me")
st.write(flag)

if flag:
    img = Image.open("C:\Users\chris' pc\aws_sentiment_program\water-5393919_1280.jpg")
    st.image(img,width=100)

## radio button....

selection = st.radio("CHoose your model you want to use...." ['NLP', 'Image', 'Audio'])
st.write(selection)

## SSelect box options.....

selection = st.selectbox("Choose your model you want to use Mac....",['NLP', 'Image', 'Audio'])
st.write(selection)

### Multi select option thing....

selection = st.multiselect("Choose your model 'Jack'...", ['NLP', 'Image', 'Audio'])
st.write(selection)




with st.spinnner("Its downloading 'Mac'. Hold on...."):
    st.write("Download model here...")
    time.sleep(10)

## Select numerical value from the give list.....
## TH = 0.5, large -> high precision, small TH -> high recall. I am providing this measument to the user to select the TH value for the model to use....
st.slider("Set the Threshold", 0, 100, step=10)







