import streamlit as st

def insight_question_1():
   st.markdown('&#9889; <font color="yellow"><b>What are benefits of finding the answer? </b></font>', unsafe_allow_html=True)
   st.markdown('>- Then after we can choose district to live in HCMC')
   st.markdown('>- We can know the number of rooms in each district and the proportion of rooms in each district, from which we can see which district has the most rooms, and why it has so many rooms (school, industrial area)')
   st.markdown('>- We can see "Quận Bình Thạnh" is most popular district in HCMC, and "Quận 1" is the least popular district in HCMC (because of the high price of rooms in "Quận 1"). And because `Quận Bình Thạnh` is near university school and price of rooms is not high and food is cheap, so it is the most popular district in HCMC.')
   st.markdown('>- And the district `Huyện Nhà Bè`, `Huyện Hóc Môn`, `Huyện Củ Chi`, `Huyện Bình Chánh` is the least popular district in HCMC (because of the far from center of HCMC and price of rooms is not high and food is not cheap but job opportunities, the workers are not many and security is not good,... so it is the least popular district in HCMC).')
      
def provide_question_1():
   st.markdown('&#9889; <font color="yellow"><b>Does it need to have preprocessing step, and if yes, how does your group preprocess? </b></font>', unsafe_allow_html=True)
   st.markdown('&#9889; <font color="yellow"><b>How does your group analyze data to answer the question? </b></font>', unsafe_allow_html=True)

def make_tab_sections(index):
   st.title(':blue[Conclusions]')
   insight, provide = st.tabs(["Insight", "Provide"])

   with insight:
      if index == 0:
         insight_question_1()
      elif index == 1:
         st.write(' ')
      if st.button('👍🏻'):
         st.success('Thank you for your feedback!')
      else:
         st.write(' ')

   with provide:
      if index == 0:
         provide_question_1()
      elif index == 1:
         st.write(' ')