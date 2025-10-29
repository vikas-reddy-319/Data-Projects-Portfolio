---

# 4) `time-series-demand-forecasting`

# Time-Series Demand Forecasting

**Type:** Portfolio Case Study (Forecasting · BI)  
**Stack:** Python (Prophet/ARIMA) · Pandas · Power BI  
**Domain:** Inventory / Supply Chain

## Problem
Inventory planning was reactive, leading to:
- Stockouts for high-velocity items  
- Excess carrying costs for slow-moving SKUs  

## Solution (What I built)
- Developed Prophet/ARIMA models per SKU/region with weekly seasonality
- Added external regressors: holidays, promotions, and price shifts
- Implemented MAPE/RMSE monitoring for model selection (champion vs. challenger)
- Automated weekly forecast publishing to Power BI for planners

## Business Value (Portfolio Framing)
Designed to:
- Improve forecast accuracy for **proactive planning**
- Reduce stockouts and over-inventory
- Optimize supply chain decisions with data-driven insights

## Repo Structure
