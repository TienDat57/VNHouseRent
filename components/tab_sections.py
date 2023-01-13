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

def insight_question_2():
   st.markdown( '&#9889; <font color="yellow"><b>What are benefits of finding the answer? </b></font>', unsafe_allow_html=True)
   st.markdown('>- Monthly statistics of the year help homeowners have plans to serve the times when the demand for rent is high in the city.')
   st.markdown('>- According to the chart, the number of rooms posted in the months of May, June, and July is quite high (average over 140 rooms). This is also easy to explain because it is the time when students enroll and need to find accommodation.')
   st.markdown('>- Therefore, the following months (August, September, and October) the number of rooms for rent is quite low, nearly halving compared to the previous months (about 35 to 70 rooms) because this is the time when students enter school. accommodation has been settled.')
   st.markdown('>- The remaining months average between 70 and 110 rooms per month.')
   st.markdown('> => Thus, from the above data, we can tell landlords when the demand for rental housing increases so that there are prepared mechanisms to respond.')  
   
def make_tab_sections(index):
   st.title(':blue[Conclusions]')
   insight, provide = st.tabs(["Insight", "Provide"])

   with insight:
      if index == 0:
         insight_question_1()
      elif index == 1:
         insight_question_2()
      if st.button('👍🏻'):
         st.success('Thank you for your feedback!')
      else:
         st.write(' ')
         

   with provide:
      if index == 0:
         provide_question_1()
      elif index == 1:
         st.write(' ')