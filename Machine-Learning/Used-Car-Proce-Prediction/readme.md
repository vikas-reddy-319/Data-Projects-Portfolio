# Used Car Price Prediction and Analysis

## Problem Statement
Used car prices can be challenging to navigate due to various contributing factors such as car condition, mileage, and age. This project aims to provide a model that predicts the price of used cars based on their specifications. By analyzing historical car listings data from Craigslist, we can gain insights into factors that influence pricing, helping potential buyers and sellers make more informed decisions.

## Objectives
1. **Trend Analysis**: Identify trends in car sales over the years.
2. **Correlation Analysis**: Investigate relationships between car price and specifications.
3. **Price Prediction Model**: Build a regression model to predict car prices based on selected features.

## Approach
1. **Data Collection**: Used data scraped from Craigslist, which included 426,880 entries covering a range of car features and pricing data from 1900-2022.
2. **Data Cleaning**: Addressed null values, duplicates, and removed unnecessary columns, reducing the dataset to 338,589 rows and 14 key columns.
3. **Feature Engineering**: Selected important features for prediction, including:
   - **Condition**
   - **Fuel type**
   - **Drive type**
   - **Car type**
   - **Manufacture year**
   - **Odometer reading**
4. **Exploratory Data Analysis (EDA)**: Conducted EDA to uncover patterns, using visualizations to explore car pricing trends, distribution by condition, and odometer impact.
5. **Model Training**: Implemented multiple regression models, including Linear Regression, Decision Tree, Random Forest, and XGBoost, to predict car prices.
6. **Application Deployment**: Built a Streamlit app that allows users to input car features and receive price predictions.

## Struggles Faced
1. **Data Quality**: Large portions of data had missing values, requiring extensive cleaning to ensure consistency and accuracy.
2. **Feature Selection**: Identifying which features most impacted car prices was challenging, as various factors contribute to pricing.
3. **Model Selection**: Testing different regression models required balancing interpretability, performance, and generalization capabilities.
4. **User Interface Development**: Developing an intuitive, user-friendly app on Streamlit for non-technical users required extra focus on user experience.

## Solutions to Challenges
1. **Data Imputation and Transformation**: Addressed missing values through imputation and removed duplicates to improve data quality.
2. **Correlation Analysis**: Conducted correlation analysis to identify the most influential features and focus on those in the model.
3. **Model Testing and Evaluation**: Used cross-validation and performance metrics like R-squared to identify Random Forest as the best model based on accuracy.
4. **User-Friendly App Design**: Designed a streamlined interface in Streamlit to make the model accessible to end-users, enabling intuitive data input and price prediction.

## Results and Final Deliverables
- **Data Insights**: Key findings from EDA included:
  - **Condition Impact**: Fair and good condition cars dominate the market, with condition significantly impacting price.
  - **Odometer vs. Price**: Higher odometer readings correlate with lower prices, while cars with lower readings tend to have higher values.
  - **Price Trends by Year**: Older used cars saw higher prices pre-2010, while more recent models showed a decline in average prices.
- **Model Performance**: The Random Forest model outperformed others, achieving the highest R² score for test data.
- **Streamlit Application**: A user-friendly app where users can input car specifications to get price predictions. This app is particularly valuable for buyers and sellers in the used car market, as it provides an easy way to understand expected pricing.

## Tools and Technologies Used

1. **Data Collection and Cleaning**:
   - **Pandas**: For data manipulation, cleaning, and preparation.
   - **NumPy**: For handling numerical data and calculations.

2. **Data Analysis**:
   - **Matplotlib and Seaborn**: Used to visualize trends in car sales, condition impact, and odometer-price relationships.
   - **Plotly**: For interactive visualizations to explore correlations in car attributes and prices.

3. **Model Training**:
   - **Scikit-learn**: Used for implementing Linear Regression, Decision Tree, and Random Forest.
   - **XGBoost**: For high-performance gradient boosting regression.
   - **Cross-validation techniques**: To ensure model robustness and generalizability.

4. **Application Development**:
   - **Streamlit**: Developed a user-friendly web application for end-users to interact with the model and predict car prices.

## Conclusion and Future Scope
This project successfully identified key factors that influence used car prices and built a model with strong predictive accuracy. The insights provided can help buyers make informed decisions, while sellers can price cars more competitively.

### Future Scope
1. **Expand Dataset**: Adding more recent listings to improve model accuracy.
2. **Enhance Model Complexity**: Explore advanced models like neural networks for higher accuracy.
3. **Broaden User Interface**: Improve the Streamlit app for a more comprehensive user experience, such as integrating real-time data for predictions.

## References

- **Videos**
  - [YouTube: Data Analysis of Used Car Dataset](https://www.youtube.com/watch?v=VqgUkExPvLY)
  - [DataThinkers YouTube Channel](https://www.youtube.com/@DataThinkers)
- **Articles**
  - [Data Analysis and Science of Craigslist Used Car Dataset](https://minaomobonike.medium.com/data-analysis-and-science-of-craigslist-used-car-dataset-cfe8b0147a51)
  - [Streamlit on PyPI](https://pypi.org/project/streamlit/)

