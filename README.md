## Swiggy_Restaurants_Data_Dashboard

#Overview

This project is a Streamlit-based interactive dashboard designed for analyzing restaurant data. The dashboard allows users to upload a dataset, apply filters, and explore various insights through dynamically updated visualizations. The app is particularly useful for exploring metrics such as restaurant prices, ratings, delivery times, and their relationships across different cities and food types.

#Features

1. Upload Dataset
a) Users can upload a CSV file containing restaurant data. The app processes the uploaded file and displays the first few rows for an initial overview.
b) Expected Columns in the dataset:
c) City: Name of the city where the restaurant is located.
d) Price: Price of the restaurant's offerings.
e) Avg ratings: Average customer ratings.
f) Food Type: Type of cuisine served by the restaurant.
g) Delivery Time: Average delivery time in minutes.

2. Sidebar Filters
a) City Filter: Select a specific city to analyze restaurants in that location.
b) Price Range Filter: Filter restaurants based on their price range.
c) Rating Range Filter: Filter restaurants based on average ratings.
d) These filters dynamically affect all visualizations, allowing for focused analysis.

#3. Visualizations

A. Grouped Analysis: Average Price and Ratings by City
a) Calculates the average price and ratings for restaurants in each city.
b) Displays a grouped bar chart comparing these metrics for filtered data.

B. Price and Ratings Box Plot by Rating Categories
a) Categorizes ratings into three groups:
b) Below 3
c) 3 - 4
d) Above 4
e) Displays a box plot comparing price distributions across these categories.

C. Rating Distribution Histogram
a) Shows the distribution of average ratings across restaurants.
b) A histogram is used to visualize the frequency of ratings for filtered data.

D. Average Price by Food Type
a) Calculates the average price for each food type.
b) Displays a bar chart of average prices for different cuisines, with the ability to dynamically filter based on city and other criteria.

E. Delivery Time Outliers
a) Identifies potential outliers in delivery times using a box plot.
b) This can highlight restaurants with unusually long or short delivery times.

#4. Dynamic Filtering
a) All visualizations are dynamically linked to the sidebar filters. For example:
b) Selecting a city automatically updates all charts and tables to show data specific to that city.
c) Changing the price or rating range instantly refreshes the visualizations.

#How to Use
1. Prerequisites
Ensure you have the following installed:
a) Python 3.7 or higher
b) Required Python libraries:
c) streamlit
d) pandas
e) matplotlib
f) seaborn
g) numpy
h) Command to install these libraries : pip install streamlit pandas matplotlib seaborn numpy

#2. Running the App
a) Save the project code into a Python file, e.g., restaurant_dashboard.py.
b) Open your terminal or command prompt and navigate to the directory where the file is saved.
c) Command to run the python file streamlit run restaurant_dashboard.py
d) he app will open automatically in your default web browser. If not, copy the URL shown in the terminal and paste it into your browser (e.g., http://localhost:8501).

#3. Uploading a Dataset
a) Prepare a CSV file with the required columns (City, Price, Avg ratings, Food Type, Delivery Time).
b) Use the "Upload your CSV file" option to load the dataset into the app.

#4. Using Filters
Use the sidebar to select:
a) City: Focus on restaurants from a specific city.
b) Price Range: Adjust the price range for analysis.
c) Rating Range: Adjust the rating range for analysis.

#5. Exploring Visualizations
a) Analyze restaurant data dynamically through charts and insights:
b) Grouped metrics for average price and ratings by city.
c) Distribution of restaurant prices across different rating categories.
d) Histogram showing the frequency of average ratings.
e) Average price comparison for different cuisines.
f) Outlier analysis for delivery times.

#Future Enhancements
Add support for additional filters like Food Type or Delivery Time.
Enable download of filtered data and visualizations.
Integrate with a database for real-time data updates

#Contributing
Feel free to contribute by raising issues or submitting pull requests to enhance this project. Let's make data analysis even more insightful and interactive!

#THANK YOU !
