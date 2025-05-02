import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set style
sns.set_style("whitegrid")

# Title
st.title("Diwali Sales EDA Dashboard")

# Load Data
df = pd.read_csv("Diwali Sales Data.csv", encoding='unicode_escape')
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
df.dropna(inplace=True)
df['Amount'] = df['Amount'].astype('int')

# Sidebar Filters
st.sidebar.header("Filter Options")

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)

age_filter = st.sidebar.multiselect(
    "Select Age Group",
    options=df['Age Group'].unique(),
    default=df['Age Group'].unique()
)

marital_filter = st.sidebar.multiselect(
    "Select Marital Status",
    options=df['Marital_Status'].unique(),
    default=df['Marital_Status'].unique()
)

occupation_filter = st.sidebar.multiselect(
    "Select Occupation",
    options=df['Occupation'].unique(),
    default=df['Occupation'].unique()
)

product_filter = st.sidebar.multiselect(
    "Select Product Category",
    options=df['Product_Category'].unique(),
    default=df['Product_Category'].unique()
)

state_filter = st.sidebar.multiselect(
    "Select State",
    options=df['State'].unique(),
    default=df['State'].unique()
)

# Filtered Data
filtered_df = df[(df['Gender'].isin(gender_filter)) & (df['Age Group'].isin(age_filter))]

# Gender Plot
st.subheader("Total Sales by Gender")
gender_sales = filtered_df.groupby('Gender')['Amount'].sum().reset_index()
fig1 = sns.barplot(x='Gender', y='Amount', data=gender_sales)
st.pyplot(fig1.figure)

# Age Group Plot
st.subheader("Sales by Age Group")
age_sales = filtered_df.groupby('Age Group')['Amount'].sum().reset_index()
fig2 = sns.barplot(x='Age Group', y='Amount', data=age_sales)
st.pyplot(fig2.figure)

# Marital Status Plot
st.subheader("Sales by Marital Status")
marital_sales = filtered_df.groupby('Marital_Status')['Amount'].sum().reset_index()
fig3 = sns.barplot(x='Marital_Status', y='Amount', data=marital_sales)
st.pyplot(fig3.figure)

# Occupation Plot
st.subheader("Sales by Occupation")
occupation_sales = filtered_df.groupby('Occupation')['Amount'].sum().reset_index().sort_values(by='Amount', ascending=False)
fig4 = sns.barplot(x='Amount', y='Occupation', data=occupation_sales)
st.pyplot(fig4.figure)

# Product Category Plot
st.subheader("Sales by Product Category")
product_sales = filtered_df.groupby('Product_Category')['Amount'].sum().reset_index().sort_values(by='Amount', ascending=False)
fig5 = sns.barplot(x='Amount', y='Product_Category', data=product_sales)
st.pyplot(fig5.figure)

# State-wise Sales
st.subheader("Top States by Sales")
state_sales = filtered_df.groupby('State')['Amount'].sum().sort_values(ascending=False).head(10)
st.bar_chart(state_sales)
