import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from constants.index import list_questions
from components import tab_sections

def question_one(df):
   st.header(list_questions[0])
   st.write("The bar chart below shows the number of houses for rent in each district of Ho Chi Minh City.")
   st.bar_chart(df['district'].value_counts())
   st.markdown('---')
   
   st.subheader("The bar chart below shows the number of houses for rent in each district of Ho Chi Minh City in year that have most number house rent in each district.")
   df['published'] = pd.to_datetime(df['published'], format='%Y-%m-%d')
   top1_year = df['published'].dt.year.value_counts().index[0]

   fig, ax = plt.subplots()
   ax.bar(df['district'].value_counts().index, df['district'].value_counts().values, label='All year')
   ax.bar(df[df['published'].dt.year == top1_year]['district'].value_counts().index, df[df['published'].dt.year == top1_year]['district'].value_counts().values, label='2022')
   ax.set_xlabel('District')
   ax.set_ylabel('Number of houses')
   ax.set_title('Number of houses for rent in each district of Ho Chi Minh City in year that have most number house rent in each district')
   ax.set_xticks(df['district'].value_counts().index)
   ax.set_xticklabels(df['district'].value_counts().index, rotation=90)
   ax.legend()
   st.pyplot(fig)
   st.markdown('---')

   st.markdown('##### &#9889; <font color="yellow"><b>Comment</b></font>', unsafe_allow_html=True)
   st.markdown('> - We can see in 2022 have number of rooms published most but in the downtown districts tended to decrease significantly, while in the districts adjacent to the city center, the listings were higher, showing us that the demand for housing in the city near the center is higher than the demand for housing in the city center. ')
   st.markdown('> - In 2022 district `Quận Gò Vấp` and `Quận Tân Phú` and `Quận Bình Tân` and `Quận 7` have high rate rate compared to all previous listing time and the remaining districts show no sign of increasing over the previous years (Because the house prices here are quite high and the demand for accommodation is not much or in the districts too far from the city with poor facilities, ... )')
   st.markdown('---')
   
   import seaborn as sns
   st.subheader("The boxplot below shows the price of houses for rent in the top 3 districts with the highest number of houses for rent and the top 3 districts with the lowest number of houses for rent.")
   _top_3_district_highest = df['district'].value_counts().head(3).index
   _top_3_district_lowest = df['district'].value_counts().tail(3).index
   fig, ax = plt.subplots()
   sns.boxplot(x='district', y='price', data=df[df['district'].isin([*_top_3_district_highest, *_top_3_district_lowest])], order=[*_top_3_district_highest, *_top_3_district_lowest], showfliers=False, ax=ax)
   ax.set_title('Price of houses for rent in the top 3 districts with the highest number of houses for rent and the top 3 districts with the lowest number of houses for rent')
   ax.set_xlabel('District')
   ax.set_ylabel('Price')
   ax.set_xticklabels([*_top_3_district_highest, *_top_3_district_lowest], rotation=90)
   st.pyplot(fig)
   st.markdown('---')
   
   st.subheader("The boxplot below shows the acreage of houses for rent in the top 3 districts with the highest number of houses for rent and the top 3 districts with the lowest number of houses for rent.")
   fig, ax = plt.subplots()
   sns.boxplot(x='district', y='acreage', data=df[df['district'].isin([*_top_3_district_highest, *_top_3_district_lowest])], order=[*_top_3_district_highest, *_top_3_district_lowest], showfliers=False)
   ax.set_title('Acreage of houses for rent in the top 3 districts with the highest number of houses for rent and the top 3 districts with the lowest number of houses for rent')
   ax.set_xlabel('District')
   ax.set_ylabel('Acreage')
   ax.set_xticklabels([*_top_3_district_highest, *_top_3_district_lowest], rotation=90)
   st.pyplot(fig)
   st.markdown('---')
   
   tab_sections.make_tab_sections(0)
   
def question_two(df):
   st.subheader(list_questions[1])
   
   df['month'] = pd.DatetimeIndex(df['published']).month
   df['year'] = pd.DatetimeIndex(df['published']).year
   
   df['month_year'] = pd.to_datetime(df[['year', 'month']].assign(DAY=1))
   df['month_year'] = pd.to_datetime(df['month_year']).dt.strftime('%Y-%m')

   # group by month and count number of houses
   df['month_year'].groupby(df['month']).count()

   # calculate number of houses in month for each year
   month_each_year = df['month_year'].groupby([df['month'], df['year']]).count()
   month_each_year.head(12)   
   
   sum_each_month = month_each_year.groupby(month_each_year.index.get_level_values(0)).sum().reindex(range(1,13)).reindex(range(1,13), fill_value=0)
   # create a dataframe with month and sum_each_month column
   sum_each_month_df = pd.DataFrame({'month': sum_each_month.index, 'sum_each_month': sum_each_month.values})
   sum_each_month_df['average'] = sum_each_month_df['sum_each_month'] / (df['year'].unique().size)
   st.write("Dataframe with month, total number of houses and average number of houses.")
   st.dataframe(sum_each_month_df) 
   
   st.write("The bar chart below shows the Average number of houses rented in each month.")
   
   fig, ax = plt.subplots()
   ax.bar(sum_each_month.index , sum_each_month_df['average'].values, label='All year')
   ax.set_xlabel('Month')
   ax.set_ylabel('Average')
   ax.set_title('Average number of houses rented in each month')
   ax.legend()
   st.pyplot(fig)
   st.markdown('---')
   
   tab_sections.make_tab_sections(1)
   
def question_three():
   st.subheader(list_questions[2])

def question_four():
   st.subheader(list_questions[3])
   
def question_five():
   st.subheader(list_questions[4])