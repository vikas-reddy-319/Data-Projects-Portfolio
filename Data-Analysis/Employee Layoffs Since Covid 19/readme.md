# Employee Layoffs Since COVID-19: Industry Impact and Interest Rate Analysis

## Problem Statement:
The purpose of this project is to analyze the impact of employee layoffs globally since the onset of COVID-19. The project aims to identify which industries experienced the highest number of layoffs, which countries were most affected, and to explore whether there is a correlation between U.S. federal interest rates and layoffs in companies. We have two datasets:
1. Global employee layoffs across different industries and companies.
2. U.S. federal interest rates over the same time period.

The analysis will focus first on identifying trends in layoffs by industry and company, and then move to investigate potential relationships between federal interest rates and layoffs.

## Objective:
- To identify the industries and companies most affected by employee layoffs globally since COVID-19.
- To determine which countries experienced the most significant layoffs.
- To explore the potential relationship between U.S. federal interest rates and the layoffs in companies over time.

## Approach:
1. **Data Collection**: Gather data from two datasets:
   - One covering global layoffs in different industries and companies.
   - Another covering U.S. federal interest rates.
2. **Industry and Country Analysis**: 
   - Analyze the data to determine which industries and companies saw the most layoffs and which countries were most impacted.
3. **Interest Rate Analysis**:
   - Examine the trends in U.S. federal interest rates during the same period.
   - Investigate potential correlations between the rise/fall of interest rates and employee layoffs in various industries.
4. **Correlation Study**: Use statistical techniques to determine if there is a significant relationship between U.S. interest rate fluctuations and the layoffs observed in specific industries.

## Struggles Faced:
1. **Data Availability and Quality**: Ensuring that the datasets used for layoffs and interest rates are accurate, complete, and cover the entire period of analysis.
2. **Mismatch in Data Granularity**: The datasets for layoffs and interest rates differ in terms of time granularity, making it difficult to directly compare the two over certain periods.
3. **Global vs. National Analysis**: The challenge of comparing global layoffs with U.S.-specific interest rate data, requiring adjustments to ensure the analysis captures meaningful insights.
4. **Economic Complexity**: Multiple factors beyond interest rates (like inflation, market demand, etc.) contribute to layoffs, complicating the analysis.

## Solutions to Challenges:
1. **Data Cleaning and Transformation**: We ensured both datasets were cleaned, standardized, and aligned to enable better comparison. Missing data was handled using imputation techniques.
2. **Data Aggregation and Resampling**: Interest rate data was resampled to match the frequency of layoffs data for a more accurate analysis.
3. **Multivariate Analysis**: We considered additional economic indicators to mitigate the complexity and potential confounding factors affecting layoffs.
4. **Visualization**: Used visual techniques to show trends in layoffs and interest rates, allowing stakeholders to grasp the relationship more intuitively.

## Results and Final Deliverables:
- **Industry and Company Impact Report**: A detailed report identifying the industries and companies most affected by layoffs globally since COVID-19.
- **Country Analysis Report**: A breakdown of countries most impacted by employee layoffs, helping identify geographic trends.
- **Correlation Analysis**: Statistical findings showing whether there is a significant relationship between U.S. federal interest rates and layoffs in companies across different industries.
- **Visualization Dashboard**: An interactive dashboard showing trends in layoffs by industry, company, country, and overlaid with interest rate trends to visualize potential relationships.

## Tools and Technologies Used:

1. **Data Collection and Cleaning**:
   - **Pandas**: Used for loading, cleaning, and transforming the datasets for layoffs and interest rates.
   - **NumPy**: Employed for numerical operations, especially in handling large-scale data calculations.

2. **Data Analysis**:
   - **Matplotlib and Seaborn**: Used to visualize trends in employee layoffs across industries and countries.
   - **Plotly**: Interactive visualizations to explore relationships between layoffs and interest rates in a dynamic way.
   - **Scikit-learn**: Applied for statistical analysis and correlation modeling between interest rates and layoffs data.

3. **Statistical Modeling**:
   - **Statsmodels**: Used to perform regression analysis to explore potential relationships between interest rates and layoffs.
   - **Time Series Analysis**: Applied to identify trends and patterns over time in both layoffs and interest rates.

4. **Reporting and Visualization**:
   - **Tableau/Power BI**: Interactive dashboards for visualizing key trends and insights in layoffs and interest rates.
   - **Jupyter Notebooks**: Documented analysis steps, data exploration, and correlation findings in an easy-to-follow format.

## Conclusion:
This project provides a comprehensive analysis of employee layoffs since COVID-19 across different industries and countries, while exploring the relationship between U.S. federal interest rates and layoffs. The findings offer key insights into which industries were most affected, and how economic factors like interest rates may play a role in company decisions regarding layoffs. The visualizations and reports provide actionable information for stakeholders seeking to understand the broader economic impacts of the pandemic on employment.

