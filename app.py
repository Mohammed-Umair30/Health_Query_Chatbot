import streamlit as st
from chatbot import ask_healthbot

st.set_page_config(page_title="Pro Health Assistant", page_icon="🩺", layout="centered")

st.title("🩺 Professional Health Assistant")
st.markdown("Ask me general health-related questions. I’ll try to help as much as I can, but always consult a real doctor. 😊")

with st.expander("💡 Example questions"):
    st.markdown("""
    - What causes a sore throat?
    - Is paracetamol safe for children?
    - How can I manage stress naturally?
    - What are the symptoms of dehydration?
    """)

user_query = st.text_input("Your Question:", placeholder="e.g., What are the symptoms of vitamin D deficiency?")

if user_query:
    with st.spinner("Thinking..."):
        reply = ask_healthbot(user_query)
        st.markdown("**🧠 Assistant says:**")
        st.success(reply)
