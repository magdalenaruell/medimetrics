import streamlit as st
import pandas as pd

# 🏥 Titelbild laden und zentrieren
st.markdown(
    """
    <style>
    .centered-image {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Bild zentriert mit `st.image()` laden
st.markdown('<div class="centered-image">', unsafe_allow_html=True)
st.image("IMG_07283.PNG", width=300)  # Stelle sicher, dass das Bild im App-Ordner liegt
st.markdown('</div>', unsafe_allow_html=True)

# Titel der Anwendung
st.title("MediMetrics")

# 🦠 **Szenario Pandemie** (Schöner formatiert)
st.markdown("""
    <h3>🦠 Szenario: Pandemie</h3>
    <p style="font-size:18px; line-height:1.6;">
    Ein Krankenhaus erlebt eine massive Zunahme an Patienten aufgrund einer <b>hochansteckenden Atemwegserkrankung</b>, 
    die sich zu einer <b>Pandemie</b> ausgeweitet hat. Bei manchen Patienten löst die Krankheit einen 
    <span style="color:green;"><b>milden Verlauf</b></span> aus, bei anderen einen <span style="color:red;"><b>schwerwiegenden</b></span>.
    </p>
    
    <p style="font-size:18px;">
    Einige dieser Patienten benötigen <b>intensivmedizinische Betreuung</b>, während andere mit leichteren Symptomen isoliert werden müssen, 
    um eine weitere Verbreitung der Krankheit zu verhindern. Gleichzeitig müssen weiterhin Patienten mit anderen Erkrankungen versorgt werden, 
    wie <b>Unfallopfer, Herzinfarkt- oder Krebspatienten</b>, die ebenfalls auf lebenswichtige Behandlungen angewiesen sind.
    </p>
    
    <p style="font-size:18px;">
    Durch die Pandemie erhöht sich der Bedarf an Flächen der <b>Intensivmedizin (2.03)</b> und der <b>Isolationskrankenpflege (2.06)</b>. 
    Um eine ausreichende Versorgung zu schaffen, müssen kurzfristig und übergangsweise neue Flächen zur Verfügung gestellt werden, 
    die die Pflege von erkrankten Patienten sicherstellen. Dazu können kurzzeitig andere Flächen umgenutzt werden.
    </p>
    """, unsafe_allow_html=True)


# 🔗 GitHub-Repository mit den Excel-Dateien (ANPASSEN falls nötig)
GITHUB_BASE_URL = "https://raw.githubusercontent.com/magdalenaruell/medimetrics/main/"  # Ändere das Repo falls nötig

# 📂 Liste der Excel-Dateien aus deinem Screenshot
EXCEL_FILES = [
    "2.02_Woechnerinnen-_und_Neugeborenenpflege.xlsx",
    "2.03_Intensivmedizin.xlsx",
    "2.04_Dialyse.xlsx",
    "2.05_Saeuglings-,_Kinder-_und_Jugendkrankenpflege.xlsx",
    "2.06_Isolationskrankenpflege.xlsx",
    "2.07_Pflege_psychisch_Kranker.xlsx",
    "2.08_Nuklearmedizin.xlsx",
    "2.09_Aufnahme.xlsx",
    "2.11_Geriatrie.xlsx",
    "2.12_Palliativmedizin.xlsx",
    "2.13_Rehabilitation.xlsx",
    "2.14_Komfortstation.xlsx",
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
