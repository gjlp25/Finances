# Project Brief: Personal Finance Dashboard

## Overview
A Streamlit-based personal finance application that helps users analyze and categorize their banking transactions. The application provides an intuitive interface for transaction management, expense tracking, and financial visualization.

## Core Requirements
1. Transaction Processing
   - Import bank transactions from CSV files
   - Automatic categorization based on transaction details
   - Support for both debits (expenses) and credits (payments)

2. Transaction Management
   - View and edit transaction categories
   - Add new expense categories
   - Manual categorization capabilities

3. Financial Analysis
   - Expense summaries by category
   - Visual representations (pie charts)
   - Separate views for expenses and payments

4. Data Persistence
   - Save category configurations
   - Maintain categorization rules via keywords

5. Language
   - The app should be in Dutch

6. Bankstatements
   - The bankstatements that i get are semicolon separated csv files with the following headers:
     "Date";"Name / Description";"Account";"Counterparty";"Code";"Debit/credit";"Amount (EUR)";"Transaction type";"Notifications";"Resulting balance";"Tag"

## Technical Goals
- Maintain a simple, user-friendly interface
- Ensure efficient transaction processing
- Provide clear financial insights
- Enable flexible category management
- Support persistent configuration

## Success Criteria
- Successfully import and process bank statement CSV files
- Accurately categorize transactions
- Generate meaningful financial visualizations
- Save and load category configurations
- Provide intuitive category management
