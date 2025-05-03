# Personal Finance Dashboard

A Streamlit-based application for analyzing and categorizing personal banking transactions, with support for Dutch bank statements.

## Overview

This application helps users track and analyze their personal finances by:
- Importing bank statements in CSV format
- Automatically categorizing transactions
- Providing visual expense analysis
- Managing custom categories and rules

## Features

- 📊 Transaction categorization
- 📈 Visual expense analysis
- 🔍 Custom category management
- 💶 Support for Dutch bank statements
- 💾 Persistent category rules

## Project Documentation

Comprehensive project documentation is maintained in the `memory-bank` directory:

- [Project Brief](memory-bank/projectbrief.md) - Core requirements and goals
- [Product Context](memory-bank/productContext.md) - Product vision and user experience
- [System Patterns](memory-bank/systemPatterns.md) - Architecture and design patterns
- [Technical Context](memory-bank/techContext.md) - Technical setup and dependencies
- [Active Context](memory-bank/activeContext.md) - Current work and decisions
- [Progress](memory-bank/progress.md) - Project status and roadmap

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate
# Unix
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run main.py
```

## Bank Statement Format

The application expects CSV files with the following headers:
```
"Date";"Name / Description";"Account";"Counterparty";"Code";"Debit/credit";
"Amount (EUR)";"Transaction type";"Notifications";"Resulting balance";"Tag"
```

## Project Status

Currently in initial setup phase. See [Progress](memory-bank/progress.md) for detailed status.
