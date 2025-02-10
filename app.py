from dotenv import load_dotenv
load_dotenv(verbose=True)

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load model
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_prompt, image_data, input):
    # Combine the prompt and user input
    prompt = f"{input_prompt}\n{input}"
    
    # Generate content with the correct format
    response = model.generate_content(
        contents=[
            prompt,  # Text part
            image_data[0]  # Image part
        ]
    )
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit UI
st.title("Multi-Language Invoice Extractor")
st.header("Made With Gemmini")
input = st.text_input("Ask Your Query  :", key="input")
uploaded_file = st.file_uploader("Upload an image of invoice", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice")

submit = st.button("Tell Me About this Invoice")

input_prompt = """You are an expert in understanding invoices. We will upload a image as invoice and you will have to answer any questions based on the uploaded invoice image."""

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader(response)