import streamlit as st

def app():
   st.title("Reflection for each member")
   with st.expander("If we had more time, we would have..."):
      st.write("- We would have more time to do more feature engineering and more data exploration")
      st.write("- We would have more time to do more data visualization")
      st.write("- We would have more time to do more model tuning")
      st.write("- We would have more time to do more model evaluation")
      
   with st.expander("What difficulties have you encountered?"):
      st.subheader("- 20127458 - Đặng Tiến Đạt")
      st.subheader("- 20127627 - Nguyễn Quốc Thắng")
      st.subheader("- 20127680 - Phạm Thị Ánh Phát")
      st.subheader("- 20127084 - Nguyễn Ngọc Bảo Trâm")
      
   with st.expander("What did you learn?"):
      st.subheader("- 20127458 - Đặng Tiến Đạt")
      st.subheader("- 20127627 - Nguyễn Quốc Thắng")
      st.subheader("- 20127680 - Phạm Thị Ánh Phát")
      st.subheader("- 20127084 - Nguyễn Ngọc Bảo Trâm")
      
   st.markdown(
    """
      <style>
      .streamlit-expanderHeader > div > p {
         font-size: x-large;
         font-weight: 700;
      }
      </style>
   """,
    unsafe_allow_html=True,
   )