
##importing 

from dotenv import load_dotenv
load_dotenv()

from PIL import Image
import streamlit as st
import google.generativeai as genai
import os

##accessing the GOOGLE_API_KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#Creating the Image model GEMINI-PRO-VISION
image_model = genai.GenerativeModel("gemini-pro-vision")

#Creating the Text model GEMINI-PRO
text_model = genai.GenerativeModel("gemini-pro")


##page Title
st.set_page_config(page_title="Gemini LLM Application")





##functions for Gemini-pro-vision Images

def get_gemini_vision_response(input,image):
    if input!="":
        response=image_model.generate_content([input,image])
    else:
        response=image_model.generate_content(image)
    return response.text


def home_page():
    st.header("Gemini Pro Vision")     #adding heading
    image_text_input=st.text_input("Image Input Prompt: ",key ="input1",placeholder=("optional"))   #taking image text input (optional)
    uploaded_file = st.file_uploader("Choose an image....", type =["jpg","jpeg","png"])     #taking file as an input
    image=""

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image,caption="uploaded Image.",use_column_width =True)

    submit = st.button("Generate about image")


    if submit:
        response =get_gemini_vision_response(image_text_input,image)
        st.subheader("The Response is....")
        st.write(response)



##functions for Gemini-pro Text

def get_gemini_response(question):
    response=text_model.generate_content(question)
    return response.text

def Text_page():
    st.header("Gemini Pro")
    input = st.text_input("Input Prompt: ",key="input")    #text input
    submit = st.button("Generate")

    ## when submit is clicked
    if submit :
        response = get_gemini_response(input)
        st.subheader("The Response is")
        st.write(response)






#calling Text function
Text_page()

#calling Image function
home_page()


