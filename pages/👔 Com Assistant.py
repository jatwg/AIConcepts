import streamlit as st
from helpers import llmhelper as llm
from helpers import emailhelper as eh
from dotenv import load_dotenv

load_dotenv()

def main():
    st.title("👔 Communication Assistant")
    st.write("This AI helps you draft various documents based on the option you pick below.")

    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input("Client Name:", "Smith, Inc.")
    with col2:
        client_contact_name = st.text_input("Client Contact Name:", "John Smith")

    choice = st.selectbox("Document to help draft:", ("Tax Memo", "Engagement Letter", "Email Draft"))

    if choice in ["Tax Memo", "Engagement Letter"]:
        prompt = st.text_input(label="Topic and Purpose of this document.")
        if choice == "Tax Memo":
            system_prompt = """
            You are a senior tax expert tasked with drafting a comprehensive and professional tax memo. Follow these guidelines:

            1. Structure:
               - Heading: Include "Tax Memo", date, client name, and subject
               - Executive Summary: Brief overview of the issue and conclusion
               - Facts: Relevant background information and assumptions
               - Issue(s): Clearly state the tax question(s) to be addressed
               - Analysis: Detailed examination of applicable tax laws and regulations
               - Conclusion: Concise summary of findings and recommendations
               - Additional Considerations: Any caveats or alternative viewpoints

            2. Content:
               - Be thorough and precise in your analysis
               - Cite relevant Internal Revenue Code sections, Treasury Regulations, and case law
               - Explain complex tax concepts in clear, understandable language
               - Address potential counterarguments or alternative interpretations
               - Provide practical recommendations based on the analysis

            3. Tone and Style:
               - Maintain a formal, professional tone throughout
               - Use clear, concise language to explain complex tax issues
               - Avoid jargon unless necessary, and explain technical terms when used
               - Use active voice and present tense for clarity

            4. Formatting:
               - Use headings and subheadings for easy navigation
               - Include page numbers and section references
               - Use bullet points or numbered lists for key points or steps
               - Consider including a table of contents for longer memos

            5. Quality Assurance:
               - Ensure all facts and legal references are accurate and up-to-date
               - Double-check calculations and numerical examples
               - Proofread for grammar, spelling, and punctuation errors

            Remember: The goal is to provide a clear, well-reasoned analysis of the tax issue(s) that will guide the client's decision-making process.

            Based on the following details, draft a professional tax memo:
            Client Name: {client_name}
            Contact Name: {client_contact_name}
            Topic: {prompt}

            Create a detailed and well-structured tax memo that addresses the specified topic and provides valuable insights and recommendations.
            """
            user_prompt = f"Create a tax memo for contact name: {client_contact_name} for company: {client_name} regarding this topic: {prompt}"
        else:
            user_prompt = f"Create a {'tax memo' if choice == 'Tax Memo' else 'tax engagement letter'} for contact name: {client_contact_name} for company: {client_name} regarding this topic: {prompt}"
    elif choice == "Email Draft":
        example = st.selectbox("Sample topics:", ("Happy Anniversary", "Asking for more information", "Welcome new client"))
        description = st.text_area("Enter the description of the email you want to write:", value=example)
        tone = st.selectbox("Select the tone of the email:", ("Professional", "Conversational", "Friendly"))

    if st.button("Generate", type="primary"):
        with st.spinner("Generating document..."):
            if choice == "Email Draft":
                result = eh.generate_email(description, tone)
            else:
                result = llm.call_llm_completion(user_prompt, system_prompt if choice == "Tax Memo" else None)
        
        st.success("Document generated successfully.")
        st.markdown(result)

if __name__ == "__main__":
    main()
