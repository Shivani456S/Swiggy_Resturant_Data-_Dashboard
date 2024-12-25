import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
import base64

# Load the dataset
df = pd.read_csv("swiggy (1).csv")

# Header Section with Swiggy Logo
logo_path = "Image.jpeg"  # Replace with the correct path to your uploaded logo file
logo = Image.open(logo_path)

# Convert the logo to a base64 string
def get_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

logo_base64 = get_base64(logo_path)

st.markdown(
    f"""
    <div style='display: flex; align-items: center; margin-bottom: 80px;'>
        <img src='data:image/jpeg;base64,{logo_base64}' alt='Swiggy Logo' style='height: 120px; margin-right: 20px;'>
        <div>
            <h3 style='color: #1E90FF; font-size: 42px; font-weight: bold; font-family: Arial, sans-serif; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);'>
                <em>Swiggy Restaurant Dashboard</em>
            </h3>
            <p style='color: #555; font-size: 18px; font-style: italic; font-family: "Georgia", serif;'>
                Dive into restaurant trends, ratings, delivery times, and cuisine popularity. Make data-driven decisions with this comprehensive dashboard.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar Filters
st.sidebar.header('🔍 Filter Options')

# City Filter
cities = df['City'].unique()
selected_city = st.sidebar.selectbox('🌆 Select a City:', cities)

# Price Range Filter
price_min, price_max = float(df['Price'].min()), float(df['Price'].max())
selected_price_range = st.sidebar.slider('💸 Select Price Range:', price_min, price_max, (price_min, price_max))

# Rating Filter
rating_min, rating_max = float(df['Avg ratings'].min()), float(df['Avg ratings'].max())
selected_rating_range = st.sidebar.slider('⭐ Select Rating Range:', rating_min, rating_max, (rating_min, rating_max))

# Filter the data
filtered_data = df[(df['City'] == selected_city) & 
                   (df['Price'] >= selected_price_range[0]) & (df['Price'] <= selected_price_range[1]) &
                   (df['Avg ratings'] >= selected_rating_range[0]) & (df['Avg ratings'] <= selected_rating_range[1])]

# Display filtered data
st.subheader(f"Filtered Data for {selected_city}")
st.write(filtered_data)

# 1. Price Distribution and Average Ratings by Area
st.markdown("<h2 style='color: #FF6347;'>📊 Price Distribution and Average Ratings by Area</h2>", unsafe_allow_html=True)
st.markdown("Price Distribution shows the spread of prices for restaurants in the selected city, helping identify affordability trends.")
st.markdown("Average Ratings by Area highlights the top-rated areas based on customer reviews.")
col1, col2 = st.columns(2)

if not filtered_data.empty:
    with col1:
        st.markdown("### Price Distribution")
        fig1 = plt.figure(figsize=(8, 5))
        sns.histplot(filtered_data['Price'], bins=20, kde=True, color='blue')
        plt.title('Price Distribution', fontsize=16)
        plt.xlabel('Price', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        st.pyplot(fig1)

    with col2:
        st.markdown("### Average Ratings by Area")
        avg_ratings_area = filtered_data.groupby('Area')['Avg ratings'].mean().reset_index()
        fig2 = plt.figure(figsize=(10, 6))
        sns.barplot(x='Avg ratings', y='Area', data=avg_ratings_area, palette='viridis')
        plt.title('Average Ratings by Area', fontsize=16)
        plt.xlabel('Average Ratings', fontsize=12)
        plt.ylabel('Area', fontsize=12)
        st.pyplot(fig2)
else:
    st.write("No data available for the selected filters.")

# 2. Delivery Time Distribution and Popular Food Types
st.markdown("<h2 style='color: #FFD700;'>⏱️ Delivery Time Distribution and Popular Food Types</h2>", unsafe_allow_html=True)
st.markdown("Delivery Time Distribution gives insights into the time taken for food deliveries, aiding in understanding customer expectations.")
st.markdown("Popular Food Types identifies the most sought-after cuisines or dishes in the selected city.")
col3, col4 = st.columns(2)

if not filtered_data.empty:
    with col3:
        st.markdown("### Delivery Time Distribution")
        fig3 = plt.figure(figsize=(8, 5))
        sns.boxplot(x=filtered_data['Delivery time'], color='orange')
        plt.title('Delivery Time Distribution', fontsize=16)
        plt.xlabel('Delivery Time (minutes)', fontsize=12)
        st.pyplot(fig3)

    with col4:
        st.markdown("### Popular Food Types")
        food_counts = filtered_data['Food type'].value_counts().head(10)
        fig4 = plt.figure(figsize=(10, 6))
        food_counts.plot(kind='bar', color='green')
        plt.title('Top 10 Popular Food Types', fontsize=16)
        plt.xlabel('Food Type', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        st.pyplot(fig4)
else:
    st.write("No data available for the selected filters.")

# 3. Restaurant Ratings
st.markdown("<h2 style='color: #32CD32;'>🏅 Top 10 Restaurants by Ratings</h2>", unsafe_allow_html=True)
st.markdown("This section highlights the top 10 restaurants in the selected city based on customer ratings.")
if not filtered_data.empty:
    top_rated = filtered_data[['Restaurant', 'Avg ratings']].sort_values(by='Avg ratings', ascending=False).head(10)
    
    # Pie chart for top 10 restaurants by ratings
    st.markdown("### 🍰 Top 10 Restaurants by Ratings (Pie Chart)")
    fig5 = plt.figure(figsize=(8, 8))
    plt.pie(top_rated['Avg ratings'], labels=top_rated['Restaurant'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3', len(top_rated)))
    plt.title('Top 10 Restaurants by Ratings', fontsize=16)
    st.pyplot(fig5)
else:
    st.write("No data available for the selected filters.")


    

    
