# IPL Player Retention Performance Analysis

## Objective:
The objective of this project is to conduct an in-depth performance analysis of IPL players over the past three seasons to support team management in making informed decisions regarding player retention. The analysis will help teams maximize their budgets by identifying five key players, based on batting and bowling performance, who should be retained. The evaluation will focus on metrics such as average, strike rate, wickets, bowling average, and economy rate.

## Approach:
1. **Data Collection**: Gather historical performance data of IPL players for the past three seasons, including batting and bowling statistics.
2. **Player Categorization**: Separate players into two categories—batters and bowlers—to evaluate performance based on different metrics.
   - **For batters**: Focus on batting average and strike rate.
   - **For bowlers**: Focus on total wickets, bowling average (runs per wicket), and economy rate.
3. **Budget Allocation**: Simulate each team's budget constraints and compare the performance of key players to assess their cost-effectiveness.
4. **Retention Criteria**: Develop a scoring system based on performance metrics to rank players and identify the top five to retain.
5. **Team-specific Analysis**: Provide tailored recommendations to each team, ensuring they retain the most valuable players within their budget limits.

## Struggles Faced:
1. **Data Availability**: One of the initial challenges was finding consistent, accurate, and comprehensive performance data for all players across the past three seasons.
2. **Data Normalization**: IPL seasons are often disrupted by various factors such as injury and international commitments. Some players played fewer matches, making comparisons difficult.
3. **Metric Trade-offs**: While batters may excel in average, their strike rate might be low, and for bowlers, balancing wickets with economy rate often posed a dilemma.
4. **Budget Constraints**: Limited budget for retention made it challenging to retain all high-performing players, forcing tough decisions.

## Solutions to Challenges:
1. **Data Aggregation**: We compiled data from multiple sources and cross-verified player performance across different seasons to ensure accuracy and consistency.
2. **Weighted Scoring System**: We developed a weighted scoring model that balanced different metrics (average, strike rate, wickets, etc.) so that players could be fairly evaluated, regardless of the number of matches played.
3. **Normalization Techniques**: We used normalization techniques to adjust for variations in the number of games played to ensure that players who performed well despite playing fewer matches were given due consideration.
4. **Simulation for Budget Optimization**: Using a simulation approach, we optimized player retention within the given budget, taking into account the player’s market value and performance.

## Results and Final Deliverables:
- **Performance Dashboard**: A comprehensive dashboard was created, displaying player performance metrics over the past three years for each team.
- **Retention Recommendations**: Tailored reports for each IPL team, identifying the top five players based on their batting and bowling performance and alignment with budget constraints.
- **Cost-Benefit Analysis**: Detailed analysis showing how retaining the recommended players fits within the team’s budget while providing optimal value for the upcoming auction.
- **Visualization**: Graphical representations of performance trends, helping teams understand the progression of each player and supporting retention decisions.

## Tools and Technologies Used:

1. **Data Collection and Cleaning**:
   - **Pandas**: Used for data manipulation and cleaning, ensuring that the performance data across different seasons was consistent and in the correct format.
   - **NumPy**: Employed for handling large numerical datasets, especially when performing calculations related to averages, strike rates, and economy rates.

2. **Data Analysis**:
   - **Matplotlib and Seaborn**: Utilized for visualizing trends in player performance across different seasons, making it easier to compare players based on key metrics such as batting average, strike rate, and bowling economy.
   - **Plotly**: Implemented to create interactive visualizations, allowing stakeholders to explore various player performance scenarios interactively.
   - **Scikit-learn**: Used for normalization and feature scaling of performance data to ensure fair comparisons between players with varying numbers of matches.

3. **Budget Simulation and Optimization**:
   - **Excel/Google Sheets**: Used to simulate budget constraints and retention options, providing an easy way for non-technical stakeholders to interact with retention scenarios.
   - **Python**: Automated budget optimization using Python scripts to simulate different player retention combinations based on budget and performance constraints.
   
4. **Reporting and Dashboarding**:
   - **Tableau/Power BI**: Developed interactive dashboards for team managers and analysts to visualize key player metrics and retention recommendations.
   - **Jupyter Notebooks**: Documented the analysis process and allowed for step-by-step insights into the methodology and results.

## Conclusion:
This analysis provides IPL teams with valuable insights into player performance, enabling them to make informed decisions about player retention ahead of the auction. By evaluating key performance indicators such as batting average, strike rate, bowling average, and economy rate, and balancing these with budget constraints, teams are better positioned to retain their most impactful players while maintaining financial flexibility. The project delivers actionable data and recommendations that help teams stay competitive in the upcoming season.

