import streamlit as st
import llmhelper as llm
import webhelper as wh
import filehelper as fh
from dotenv import load_dotenv

load_dotenv()

def main():
    st.title("📋 Text Assistant")
    st.write("Upload a PDF file, enter a URL, or paste text to get a summary.")

    file_text = ""

    uploaded_file = st.file_uploader("Upload a PDF file to summarize", type="pdf")
    if uploaded_file:
        file_text = fh.read_pdf(uploaded_file)

    url = st.text_input("Enter the URL of the webpage:")
    if url:
        try:
            file_text = wh.read_web(url)
        except Exception as e:
            st.error(f"Error reading URL: {str(e)}")

    text_to_summarize = st.text_area("Text Content to Summarize", file_text, height=200)

    if st.button("Summarize", type="primary"):
        if not text_to_summarize:
            st.warning("Please provide some text to summarize.")
            return

        system_prompt = "You are a helpful AI assistant. Summarize the given information concisely, ensuring that key facts and information are included."
        user_prompt = f"Summarize the following information: {text_to_summarize}. List important facts and key points in bullet points, with a brief summary at the end."

        with st.spinner("Generating summary..."):
            result = llm.call_llm_completion(system_prompt, user_prompt)
        
        st.success("Summary generated successfully.")
        st.markdown(result)

if __name__ == "__main__":
    main()
