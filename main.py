import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

# Configureer de pagina
st.set_page_config(page_title="Financiën Dashboard", page_icon="💰", layout="wide")

category_file = "categories.json"

# Initialiseer categorieën
if "categories" not in st.session_state:
    st.session_state.categories = {
        "Niet Gecategoriseerd": [],
    }
    
# Laad bestaande categorieën
if os.path.exists(category_file):
    with open(category_file, "r") as f:
        st.session_state.categories = json.load(f)
        
def save_categories():
    """Sla categorieën op in JSON bestand"""
    with open(category_file, "w") as f:
        json.dump(st.session_state.categories, f)

def categorize_transactions(df):
    """Categoriseer transacties op basis van trefwoorden"""
    df["Categorie"] = "Niet Gecategoriseerd"
    
    for category, keywords in st.session_state.categories.items():
        if category == "Niet Gecategoriseerd" or not keywords:
            continue
        
        lowered_keywords = [keyword.lower().strip() for keyword in keywords]
        
        for idx, row in df.iterrows():
            details = row["Naam / Omschrijving"].lower().strip()
            if details in lowered_keywords:
                df.at[idx, "Categorie"] = category
                
    return df  

def load_transactions(file):
    """Laad en verwerk transacties uit CSV bestand"""
    try:
        # Lees CSV met juiste scheidingsteken en kolommen
        df = pd.read_csv(file, sep=";")
        
        # Hernoem kolommen naar Nederlandse namen
        column_mapping = {
            "Date": "Datum",
            "Name / Description": "Naam / Omschrijving",
            "Account": "Rekening",
            "Counterparty": "Tegenrekening",
            "Code": "Code",
            "Debit/credit": "Debet/credit",
            "Amount (EUR)": "Bedrag (EUR)",
            "Transaction type": "Transactiesoort",
            "Notifications": "Mededelingen",
            "Resulting balance": "Resultaatsaldo",
            "Tag": "Label"
        }
        df.rename(columns=column_mapping, inplace=True)
        
        # Converteer bedrag (verwijder € teken en vervang komma door punt)
        df["Bedrag (EUR)"] = df["Bedrag (EUR)"].str.replace("€", "").str.replace(",", ".").astype(float)
        
        # Converteer datum (van YYYYMMDD formaat)
        df["Datum"] = pd.to_datetime(df["Datum"], format="%Y%m%d")
        
        return categorize_transactions(df)
    except Exception as e:
        st.error(f"Fout bij verwerken bestand: {str(e)}")
        return None

def add_keyword_to_category(category, keyword):
    """Voeg een trefwoord toe aan een categorie"""
    keyword = keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True
    return False

def main():
    st.title("Financiën Dashboard")
    
    uploaded_file = st.file_uploader("Upload je transactie CSV bestand", type=["csv"])
    
    if uploaded_file is not None:
        df = load_transactions(uploaded_file)
        
        if df is not None:
            # Split in uitgaven en inkomsten
            debits_df = df[df["Debet/credit"] == "Debit"].copy()
            credits_df = df[df["Debet/credit"] == "Credit"].copy()
            
            st.session_state.debits_df = debits_df.copy()
            
            tab1, tab2 = st.tabs(["Uitgaven", "Inkomsten"])
            with tab1:
                new_category = st.text_input("Nieuwe Categorie Naam")
                add_button = st.button("Voeg Categorie Toe")
                
                if add_button and new_category:
                    if new_category not in st.session_state.categories:
                        st.session_state.categories[new_category] = []
                        save_categories()
                        st.rerun()
                
                st.subheader("Jouw Uitgaven")
                edited_df = st.data_editor(
                    st.session_state.debits_df[["Datum", "Naam / Omschrijving", "Bedrag (EUR)", "Categorie"]],
                    column_config={
                        "Datum": st.column_config.DateColumn("Datum", format="DD/MM/YYYY"),
                        "Naam / Omschrijving": "Omschrijving",
                        "Bedrag (EUR)": st.column_config.NumberColumn(
                            "Bedrag", 
                            format="€%.2f",
                            help="Bedrag in euro's"
                        ),
                        "Categorie": st.column_config.SelectboxColumn(
                            "Categorie",
                            options=list(st.session_state.categories.keys()),
                            help="Selecteer een categorie"
                        )
                    },
                    hide_index=True,
                    use_container_width=True,
                    key="category_editor"
                )
                
                save_button = st.button("Wijzigingen Toepassen", type="primary")
                if save_button:
                    for idx, row in edited_df.iterrows():
                        new_category = row["Categorie"]
                        if new_category == st.session_state.debits_df.at[idx, "Categorie"]:
                            continue
                        
                        details = row["Naam / Omschrijving"]
                        st.session_state.debits_df.at[idx, "Categorie"] = new_category
                        add_keyword_to_category(new_category, details)
                        
                st.subheader('Uitgaven Overzicht')
                category_totals = st.session_state.debits_df.groupby("Categorie")["Bedrag (EUR)"].sum().reset_index()
                category_totals = category_totals.sort_values("Bedrag (EUR)", ascending=False)
                
                st.dataframe(
                    category_totals,
                    column_config={
                        "Categorie": "Categorie",
                        "Bedrag (EUR)": st.column_config.NumberColumn(
                            "Totaal Bedrag",
                            format="€%.2f"
                        )
                    },
                    use_container_width=True,
                    hide_index=True
                )
                
                fig = px.pie(
                    category_totals,
                    values="Bedrag (EUR)",
                    names="Categorie",
                    title="Uitgaven per Categorie"
                )
                st.plotly_chart(fig, use_container_width=True)
                
            with tab2:
                st.subheader("Inkomsten Overzicht")
                total_payments = credits_df["Bedrag (EUR)"].sum()
                st.metric("Totaal Inkomsten", f"€{total_payments:,.2f}")
                
                st.dataframe(
                    credits_df[["Datum", "Naam / Omschrijving", "Bedrag (EUR)"]],
                    column_config={
                        "Datum": st.column_config.DateColumn("Datum", format="DD/MM/YYYY"),
                        "Naam / Omschrijving": "Omschrijving",
                        "Bedrag (EUR)": st.column_config.NumberColumn(
                            "Bedrag",
                            format="€%.2f"
                        )
                    },
                    use_container_width=True,
                    hide_index=True
                )
        
if __name__ == "__main__":
    main()
