# Healthcare KPI Performance Dashboard

**Type:** Portfolio Case Study (BI/Analytics)  
**Stack:** Power BI · SQL · DAX · Data Modeling · (Optional) Python  
**Domain:** Healthcare operations & quality

## Problem
Clinical and operations leaders relied on 20+ spreadsheets and static reports. KPIs were inconsistent across departments, delaying decisions on patient throughput, wait times, readmissions, and staffing.

## Solution (What I built)
- Star-schema model with Facts: `Admissions`, `Encounters`, `Readmissions`, `WaitTimes`; Dimensions: `Date`, `Facility`, `Department`, `Provider`, `Payer`.
- Power BI dashboard with drilldowns: System ➜ Facility ➜ Department ➜ Provider.
- Standardized KPI definitions with DAX measures and a “KPI Dictionary.”
- Scheduled refresh + row-level security (RLS) for role-based access.

## Business Value (Portfolio framing)
Designed to:
- Centralize metrics → enable **faster decisions** by reducing metric hunting and reconciliation.
- Improve trust in numbers via consistent definitions.
- Reduce ad-hoc report requests by enabling **self-serve** exploration.

## Example KPIs
- LOS, Bed Occupancy %, On-time Discharges %, Readmission Rate, Avg Wait Time, Case Mix Index.

## Data
- Synthetic sample generated for demonstration. No PHI/PII.  
- `/data/` folder includes CSVs + schema dictionary.

## Repo Structure

