## Swiggy_Restaurants_Data_Dashboard

# Swiggy Restaurant Analysis Dashboard

This repository contains the source code for the **Swiggy Restaurant Analysis Dashboard**. The dashboard provides insights into various restaurant data including ratings, price distribution, food type popularity, and more. It was built using **Streamlit**, **Pandas**, **Seaborn**, and **Matplotlib** to present interactive visualizations in a user-friendly format.

You can access the live dashboard [here](https://swiggyresturantdata-dashboard-l6udsz4am2z52jsybmcaju.streamlit.app/).

## Tools and Libraries Used

1. **Streamlit**: 
   - Streamlit is a powerful Python library that allows the creation of interactive web applications with ease. It's the core library used to create the dashboard.
   - It allows us to display data frames, create visualizations, and build interactive elements such as filters, sliders, and charts in a few lines of code.

2. **Pandas**: 
   - Pandas is a Python library used for data manipulation and analysis. It was used to load, clean, and process the dataset.

3. **Matplotlib** and **Seaborn**:
   - Matplotlib is a plotting library, and Seaborn is built on top of it. Both were used to create various plots, such as histograms, bar charts, and pie charts, to visualize the restaurant data in a meaningful way.
   - Visualizations include **Price Distribution**, **Average Ratings by Area**, **Top 10 Restaurants by Ratings**, and more.

4. **Pillow**: 
   - Pillow is a Python Imaging Library used to process and display images. It was used to display the Swiggy logo on the dashboard.

5. **Base64**: 
   - Base64 encoding was used to embed the Swiggy logo directly into the dashboard as a base64 string, ensuring it can be viewed without needing an external image file.

6. **NumPy**:
   - NumPy was used for numerical operations such as generating the price ranges for filtering data.

## Key Insights from the Dashboard

### 1. **Cities and Restaurants Distribution**:
- The dataset contains information on restaurants spread across different cities. The **City** column was used to analyze the distribution of restaurants in each city.
- A bar chart was generated to display the number of restaurants in each city.

### 2. **Average Rating Trends**:
- The **Avg ratings** column provides the average ratings for each restaurant. This data was categorized into four segments: Poor, Average, Good, and Excellent.
- A pie chart was used to visualize the distribution of ratings among the restaurants.

### 3. **Price Analysis**:
- The **Price** column provides the price range of food at restaurants. A histogram was created to display the distribution of restaurant prices, helping identify common price ranges.
  
### 4. **Delivery Time Insights**:
- The **Delivery time** column was analyzed to reveal trends in delivery times across different restaurants.
- A boxplot was used to show the distribution of delivery times, helping identify potential bottlenecks in delivery.

### 5. **Food Types Popularity**:
- The **Food type** column was used to analyze the most popular food types across restaurants.
- A bar chart displayed the top 10 most common food types.

### 6. **Top 10 Restaurants by Ratings**:
- The **Avg ratings** column was used to find the top 10 restaurants based on customer ratings.
- A pie chart was created to show the ratings of these top 10 restaurants.

## How the Dashboard Was Built

The dashboard was developed using the following steps:

1. **Data Collection**:
   - The restaurant data was collected into a CSV file (`swiggy.csv`) containing columns such as Restaurant name, City, Area, Price, Avg ratings, Delivery time, and Food type.

2. **Data Cleaning**:
   - Using **Pandas**, the dataset was cleaned by handling missing values, filtering data based on user inputs, and aggregating values (e.g., calculating average ratings per area).

3. **Visualization**:
   - Various visualizations were created using **Seaborn** and **Matplotlib** to provide clear insights into the dataset. This included histograms, bar charts, pie charts, and box plots.

4. **Interactivity**:
   - Streamlit's interactive widgets (e.g., `selectbox`, `slider`) were used to filter data based on user inputs like city, price range, and rating range.

5. **Deployment**:
   - Once the application was developed locally, it was deployed on **Streamlit Cloud** to make it accessible online. You can access the live version of the dashboard [here](https://swiggyresturantdata-dashboard-l6udsz4am2z52jsybmcaju.streamlit.app/).

## How to Run the Dashboard Locally

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/swiggy-restaurant-analysis.git

