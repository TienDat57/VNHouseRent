import streamlit as st

def make_tab_sections():
   st.title('Conclusions')
   insight, provide = st.tabs(["Insight", "Provide"])

   with insight:
      st.write('WOW!')
      st.image("https://i.gifer.com/DJR3.gif", width=400)

   with provide:
      st.write('Do you like ice cream? 🍨')
      agree = st.checkbox('Yes! I love it')
      disagree = st.checkbox("Nah! 😅")
      if agree:
         st.write('Even I love it 🤤')
      if disagree:
         st.write('You are boring 😒')