import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
st.title('Restaurant Data Analysis Dashboard')

# Upload file option
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(r"C:\Users\chaud\OneDrive\Desktop\swiggydatatvisualization\swiggy (1).csv")

    # Display the dataset
    st.subheader("Dataset Overview")
    st.write(df.head())

    # Sidebar Filters
    st.sidebar.header('Filters')
    
    # City Filter
    cities = df['City'].unique()
    selected_city = st.sidebar.selectbox('Select a City:', cities)
    
    # Price Range Filter
    price_min, price_max = float(df['Price'].min()), float(df['Price'].max())
    selected_price_range = st.sidebar.slider('Select Price Range:', price_min, price_max, (price_min, price_max))
    
    # Rating Range Filter
    rating_min, rating_max = float(df['Avg ratings'].min()), float(df['Avg ratings'].max())
    selected_rating_range = st.sidebar.slider('Select Rating Range:', rating_min, rating_max, (rating_min, rating_max))
    
    # Filter the data
    filtered_data = df[(df['City'] == selected_city) & 
                       (df['Price'] >= selected_price_range[0]) & (df['Price'] <= selected_price_range[1]) &
                       (df['Avg ratings'] >= selected_rating_range[0]) & (df['Avg ratings'] <= selected_rating_range[1])]

    # Display filtered data
    st.subheader(f"Filtered Data for {selected_city}")
    st.write(filtered_data)

    # 1. Grouped Analysis: Average Price and Rating by City
    st.subheader("Average Price and Rating by City")
    grouped_data = filtered_data.groupby('City')[['Price', 'Avg ratings']].mean().reset_index()

    # Plot grouped data
    if not grouped_data.empty:
        fig, ax = plt.subplots(figsize=(12, 6))
        bar_width = 0.35
        index = np.arange(len(grouped_data))

        ax.bar(index, grouped_data['Price'], bar_width, label='Average Price', color='yellow')
        ax.bar(index + bar_width, grouped_data['Avg ratings'], bar_width, label='Average Rating', color='green')

        ax.set_xlabel('City')
        ax.set_ylabel('Value')
        ax.set_title('Average Price and Rating for Each City (Filtered)')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(grouped_data['City'], rotation=45, ha='right')
        ax.legend()

        st.pyplot(fig)
    else:
        st.write("No data available for the selected filters.")

    # 2. Price and Ratings Box Plot
    st.subheader("Price and Ratings Box Plot by Rating Categories")

    # Categorize ratings
    def rating_category(avg_rating):
        if avg_rating < 3:
            return 'Below 3'
        elif 3 <= avg_rating <= 4:
            return '3 - 4'
        else:
            return 'Above 4'

    filtered_data['Rating Category'] = filtered_data['Avg ratings'].apply(rating_category)

    # Box plot
    if not filtered_data.empty:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Rating Category', y='Price', data=filtered_data, palette='Set2')
        plt.title('Price Distribution by Rating Categories (Filtered)', fontsize=14)
        plt.xlabel('Rating Category', fontsize=12)
        plt.ylabel('Price', fontsize=12)
        st.pyplot(plt)
    else:
        st.write("No data available for the selected filters.")

    # 3. Rating Distribution Histogram
    st.subheader("Rating Distribution Histogram")

    if not filtered_data.empty:
        plt.figure(figsize=(10, 6))
        plt.hist(filtered_data['Avg ratings'], bins=10, color='yellow', edgecolor='green')
        plt.title('Rating Distribution (Filtered)', fontsize=14)
        plt.xlabel('Ratings', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        st.pyplot(plt)
    else:
        st.write("No data available for the selected filters.")

    # 4. Average Price by Food Type
    st.subheader("Average Price by Food Type")

    if not filtered_data.empty:
        food_price = filtered_data.groupby('Food type')['Price'].mean().reset_index()

        plt.figure(figsize=(18, 11))
        sns.barplot(x='Food type', y='Price', data=food_price, palette='viridis')
        plt.title('Average Price for Each Food Type (Filtered)', fontsize=14)
        plt.xlabel('Food Type', fontsize=12)
        plt.ylabel('Average Price', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        st.pyplot(plt)
    else:
        st.write("No data available for the selected filters.")

    # 5. Delivery Time Outliers
    st.subheader("Delivery Time Outliers")

    if not filtered_data.empty:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=filtered_data['Delivery time'], color='lightcoral', fliersize=7, linewidth=1.5)
        plt.title('Delivery Time Distribution with Outliers (Filtered)', fontsize=14)
        plt.xlabel('Delivery Time (minutes)', fontsize=12)
        st.pyplot(plt)
    else:
        st.write("No data available for the selected filters.")

else:
    st.write("Please upload a dataset to proceed.")
