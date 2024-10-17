import streamlit as st
from dotenv import load_dotenv
from helpers import llmhelper as llm
import base64
from helpers.sidebar import display_welcome

load_dotenv()

st.title("👓 Vision Assistant")
st.write("this AI help you perform task on an image")   
display_welcome()
file = st.file_uploader("Upload a file", type=["png", "jpg", "jpeg"])
user_prompt = st.text_area("Enter the task for the image","Describe this image in detail")
if st.button('Submit',type="primary"):
    file_content = file.read()
    base64_encoded_data = base64.b64encode(file_content).decode('utf-8')
    image_text = llm.call_llm_vision(base64_encoded_data,file.type,user_prompt)
    st.write(image_text)



