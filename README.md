# Multi-Language Invoice Extractor - Streamlit App

## Overview
This Streamlit-based web application allows users to upload invoice images and ask questions about them. The app utilizes Google's Gemini AI to analyze and extract information from invoices.

![WhatsApp Image 2025-02-10 at 06 50 37](https://github.com/user-attachments/assets/8b800fd4-d59b-4f44-a43f-f9a982ebf242)


## Features
- Upload invoice images (JPG, JPEG, PNG)
- Extract relevant information using AI
- Ask questions about the invoice content
- Display extracted results interactively

## Requirements
Ensure you have the following installed:

- Python 3.8+
- Streamlit
- google-generativeai
- Pillow
- dotenv

## Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <project-folder>
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Upload an invoice image through the UI.
3. Enter your query related to the invoice.
4. Click "Tell Me About this Invoice" to get AI-generated insights.

## Troubleshooting
- Ensure the `.env` file is properly configured.
- Verify that required dependencies are installed.
- Run `print(os.getenv("GOOGLE_API_KEY"))` to confirm the API key is loading.
- Check that the uploaded file is in a supported format (JPG, JPEG, PNG).


