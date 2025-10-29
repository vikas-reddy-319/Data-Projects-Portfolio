# Claims Data Quality Automation

**Type:** Portfolio Case Study (Data Quality · ETL · Analytics)  
**Stack:** Python · SQL · (ADF/Glue/dbt optional) · Power BI alerts  
**Domain:** Insurance / Healthcare claims

## Problem
Claims pipelines suffered from invalid codes, missing fields, and schema drift → rework, rejected filings, and reporting delays.

## Solution (What I built)
- Rule-based validation framework:
  - **Field checks**: nulls, ranges, date logic (service ≤ submission)
  - **Code checks**: ICD/CPT/NPI pattern validation
  - **Referential checks**: provider/payer cross-refs
  - **Anomaly checks**: sudden volume spikes vs baseline
- Auto-generated **Data Quality Report** + push to BI for monitoring.
- Optional Slack/Email alerts for severe rule failures.

## Business Value (Portfolio framing)
Designed to:
- Reduce manual QA effort by automating repeatable checks.
- Improve analytics reliability and SLA adherence.
- Detect issues earlier (pre-aggregation) to prevent downstream rework.

## Folder Structure

