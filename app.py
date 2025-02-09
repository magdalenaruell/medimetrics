import streamlit as st
import pandas as pd

# 🔗 GitHub-Repository, in dem die Excel-Dateien liegen
GITHUB_BASE_URL = "https://raw.githubusercontent.com/user/repository/main/"  # <-- ÄNDERE das Repo

# 📂 Liste der Excel-Dateien im GitHub-Repo (MUSS manuell gepflegt werden oder mit einer API automatisiert werden)
EXCEL_FILES = [
    "01_WebAnwendung_250128_NBO_DIN.xlsx",
    "02_WebAnwendung_250128_NBO_DIN.xlsx",
    "03_WebAnwendung_250128_NBO_DIN.xlsx",
    "04_WebAnwendung_250128_NBO_DIN.xlsx",
    "05_WebAnwendung_250128_NBO_DIN.xlsx",
    "06_WebAnwendung_250128_NBO_DIN.xlsx",
    "07_WebAnwendung_250128_NBO_DIN.xlsx",
    "08_WebAnwendung_250128_NBO_DIN.xlsx",
    "09_WebAnwendung_250128_NBO_DIN.xlsx",
    "10_WebAnwendung_250128_NBO_DIN.xlsx",
    "11_WebAnwendung_250128_NBO_DIN.xlsx",
    "12_WebAnwendung_250128_NBO_DIN.xlsx",
    "13_WebAnwendung_250128_NBO_DIN.xlsx",
    "14_WebAnwendung_250128_NBO_DIN.xlsx",
]

# 📌 **Excel-Datei auswählen**
st.subheader("📂 Wähle eine Excel-Datei")
selected_file = st.selectbox("📑 Wähle eine Datei:", EXCEL_FILES)

if selected_file:
    file_url = GITHUB_BASE_URL + selected_file  # URL zur Datei generieren

    try:
        # Lade die Excel-Datei direkt aus GitHub
        xls = pd.ExcelFile(file_url)
        sheet_names = xls.sheet_names
        st.success(f"📄 Datei erfolgreich geladen: `{selected_file}`")
    except Exception as e:
        st.error(f"❌ Fehler beim Laden der Datei: {str(e)}")
        st.stop()
    
    # 📊 **Tabellenblatt auswählen**
    st.subheader("📄 Wähle ein Tabellenblatt")
    selected_sheet = st.selectbox("📄 Tabellenblatt:", sheet_names)

    # 📊 **Daten aus dem gewählten Tabellenblatt anzeigen**
    if selected_sheet:
        df = pd.read_excel(xls, sheet_name=selected_sheet)
        st.subheader(f"📊 Daten aus: {selected_sheet} in `{selected_file}`")
        st.dataframe(df, use_container_width=True, height=500)
