import streamlit as st
from helpers.sidebar import display_welcome

st.title("🔡 AI POC")
st.subheader("🚀 Introducing AI Concepts: Your Intelligent Business Assistant 🚀")

display_welcome()

st.write("""
AI Concepts is your all-in-one solution for streamlining everyday business tasks. This revolutionary proof of concept empowers you to:

- Draft professional emails in seconds
- Summarize lengthy documents effortlessly
- Quickly access key information

Leveraging advanced natural language processing, AI Concepts understands your unique needs and delivers tailored results. Say goodbye to juggling multiple apps and spending hours on routine tasks. With AI Concepts as your professional sidekick, you'll:

- Boost productivity
- Reduce stress
- Stay ahead in today's fast-paced business world

Experience the future of work efficiency. Let AI Concepts handle the details while you focus on what truly matters.
""")
