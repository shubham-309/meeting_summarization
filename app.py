from utils import *
import streamlit as st

st.set_page_config(page_title="Meeting Summariser and Task Assiging APP")
st.title(" Summarising your meeting and assigning you Task 🤖 📑")
st.subheader("Helping you with your meetings 📝")

input_audio = st.text_input("Enter your audio URL.")
submit = st.button("Load")
if submit and input_audio:
    with st.spinner("Summarising your meeting audio and getting you your results..."):
        res = loadaudio(input_audio)
        st.write(res[0].page_content)
        response = res[0].page_content
        chunk_data = split_text_into_sentences(response)
        st.write(chunk_data)
        for chunks in chunk_data:
            response += generate(chunks)
        
        summary = summarize(response)
        
        st.write(response)
        st.expander(summary)





