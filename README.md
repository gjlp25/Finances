# Personal Finance Dashboard

Een Streamlit-gebaseerde applicatie voor persoonlijke financiën die gebruikers helpt bij het analyseren en categoriseren van banktransacties. De applicatie biedt een intuïtieve interface voor transactiebeheer, uitgaventracking en financiële visualisatie.

## Features

- CSV bankafschriften import met ondersteuning voor:
  - Semicolon-gescheiden bestanden
  - YYYYMMDD datumformaat
  - Europees nummerformaat (komma als decimaal)
- Automatische transactie categorisatie
- Dynamisch categoriebeheer
- Uitgaven visualisatie met cirkeldiagrammen
- Aparte weergaven voor uitgaven en inkomsten
- Real-time categorie updates
- Nederlandse interface

## Project Structure

```
/
├── main.py              # Application entry point with UI and logic
├── categories.json      # Category configuration with keywords
├── requirements.txt     # Project dependencies
├── bank_statements/     # Bank statement files
└── memory-bank/        # Project documentation
```

## Setup

1. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Unix
# or
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run main.py
```

The application will be available at http://localhost:8501

## Documentation

All project documentation is maintained in the memory-bank directory:

- [Project Brief](memory-bank/projectbrief.md) - Core requirements and goals
- [Product Context](memory-bank/productContext.md) - Why this project exists
- [System Patterns](memory-bank/systemPatterns.md) - Technical architecture
- [Technical Context](memory-bank/techContext.md) - Development setup and details
- [Active Context](memory-bank/activeContext.md) - Current work and decisions
- [Progress](memory-bank/progress.md) - Project status and tracking

## Features in Development

- Advanced filtering capabilities
- Enhanced error handling
- Performance optimizations
- Data validation improvements
- Export functionality

## Requirements

- Python 3.x
- See requirements.txt for package dependencies
