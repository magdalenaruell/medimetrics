import streamlit as st
import pandas as pd

# 🔗 GitHub-Repository mit den Excel-Dateien
GITHUB_BASE_URL = "https://raw.githubusercontent.com/magdalenaruell/medimetrics/main/"

# 📂 Liste der Excel-Dateien
EXCEL_FILES = [
    "2.01_Allgemeine_Pflege.xlsx",
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

# 🌟 Stil-Optimierung für die App
st.markdown(
    """
    <style>
     /* Gesamtanpassung */
    .block-container {
        max-width: 1000px;
        margin: auto;
        text-align: center;
        font-family: 'Arial', sans-serif;
        background: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 3px 3px 15px rgba(0,0,0,0.1);
    }

    /* Header Styling */
    .header-container {
        background: linear-gradient(90deg, #D1C4E9, #66BB6A, #1A237E);
        color: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
        text-align: center;
    }

    .header-title {
        font-size: 48px;
        font-weight: bold;
        margin: 0;
        letter-spacing: 1px;
    }

    .header-subtitle {
        font-size: 18px;
        margin-top: 5px;
        font-weight: 300;
    }

    /* Logo Styling */
    .logo-container {
        display: flex;
        justify-content: center;
        margin-top: -30px;
    }

    .logo {
        width: 120px;
        background: white;
        padding: 10px;
        border-radius: 50%;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    }

    /* Vergleichstabelle */
    table {
        width: 50%;
        justify-content: center;
        border-collapse: collapse;
        margin: auto;
        border-radius: 10px;
        overflow: hidden;
        background: white;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }

    th, td {
        border: 1px solid #ddd;
        padding: 10px;
        text-align: center;
    }

    th {
        background-color: #e3f2fd;  /* Hellblauer Hintergrund */
        font-weight: bold;
        padding: 12px;
        text-align: center;
        border: 1px solid #ddd;
        font-size: 12px;  /* Größe des Textes */
    }

    td {
        font-size: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 📌 Header mit Logo anzeigen
st.markdown('<div class="header-container">', unsafe_allow_html=True)

# Logo einfügen
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
st.image("https://raw.githubusercontent.com/magdalenaruell/medimetrics/main/IMG_07283.PNG", width=100)
st.markdown('</div>', unsafe_allow_html=True)

# Titel und Untertitel
st.markdown(
    """
    <div class="header-title">MediMetrics</div>
    <div class="header-subtitle">Evaluierung der Raum- & Flächennutzung für maximale Effizienz im Krankenhaus</div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

       
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

# 📂 **Erste Excel-Datei auswählen**
st.subheader("📂 Wählen Sie die erste Teilstelle")
selected_file1 = st.selectbox("📑 Erste Datei auswählen:", EXCEL_FILES, key="file1")

# 📂 **Zweite Excel-Datei auswählen**
st.subheader("📂 Wählen Sie eine Vergleichsteilstelle")
selected_file2 = st.selectbox("📑 Zweite Datei auswählen:", [f for f in EXCEL_FILES if f != selected_file1], key="file2")

if selected_file1 and selected_file2:
    file_url1 = GITHUB_BASE_URL + selected_file1
    file_url2 = GITHUB_BASE_URL + selected_file2

    try:
        # Immer Tabellenblatt "Paulina" laden
        sheet_name = "Paulina"

        df1 = pd.read_excel(file_url1, sheet_name=sheet_name, engine="openpyxl")
        df2 = pd.read_excel(file_url2, sheet_name=sheet_name, engine="openpyxl")

        st.success(f"📄 Dateien erfolgreich geladen: `{selected_file1}` & `{selected_file2}` (Tabellenblatt: {sheet_name})")

        # Sicherstellen, dass Spalte "Räume in Funktionsbereichen" existiert
        if "Räume in Funktionsbereichen" not in df1.columns or "Räume in Funktionsbereichen" not in df2.columns:
            st.error("❌ Die Spalte 'Räume in Funktionsbereichen' (Spalte B) existiert nicht in einer oder beiden Dateien.")
            st.stop()

        # Beide Tabellen nach "Räume in Funktionsbereichen" gruppieren
        df1_grouped = df1.set_index("Räume in Funktionsbereichen")
        df2_grouped = df2.set_index("Räume in Funktionsbereichen")

        # Gemeinsame & individuelle Zeilen identifizieren
        common_rows = df1_grouped.index.intersection(df2_grouped.index)
        unique_to_df1 = df1_grouped.index.difference(df2_grouped.index)
        unique_to_df2 = df2_grouped.index.difference(df1_grouped.index)

        # HTML für Vergleichstabelle erstellen
        comparison_html = """
        <table>
            <tr>
                <th>Vergleich</th>
                <th>Räume in Funktionsbereichen</th>
        """

        # Spaltenüberschriften aus der ersten Datei übernehmen
        for col in df1.columns:
            comparison_html += f"<th>{col}</th>"
        comparison_html += "</tr>"

        # **Fix für Zeilen, die nur eine Instanz haben**
        def ensure_dataframe(row):
            return row.to_frame().T if isinstance(row, pd.Series) else row

        # **Gemeinsame Zeilen (Untereinander)**
        for row in common_rows:
            row1 = ensure_dataframe(df1_grouped.loc[row])
            row2 = ensure_dataframe(df2_grouped.loc[row])

            row_styles = []
            match_status = "🟢"

            for col in row1.columns:
                if col not in row2.columns:
                    continue
                val1, val2 = row1[col].values[0], row2[col].values[0]

                if val1 == val2:
                    row_styles.append(f"<td style='background-color: #90EE90;'>{val1}</td>")
                else:
                    row_styles.append(f"<td style='background-color: #FF4500; font-weight:bold;'>{val1} | {val2}</td>")
                    match_status = "🟠"

            row_html = f"<tr><td>{match_status}</td><td>{row}</td>{''.join(row_styles)}</tr>"
            comparison_html += row_html

        # **Zeilen, die nur in einer Tabelle existieren**
        for row in unique_to_df1:
            row_html = f"<tr><td>🔴</td><td>{row}</td></tr>"
            comparison_html += row_html

        for row in unique_to_df2:
            row_html = f"<tr><td>🔴</td><td>{row}</td></tr>"
            comparison_html += row_html

        comparison_html += "</table>"

        st.subheader("📊 Vergleich der Tabellen")

        st.markdown("""
        Die folgende Tabelle vergleicht die Anforderungen der einzelnen Räume aus den gewählten Teilstellen. Grün hinterlegte Zellen kennzeichnen übereinstimmende Anforderungen, während rot markierte Zellen Unterschiede hervorheben. Diese Unterschiede werden detailliert in der Form „Anforderung erste Teilstelle | Anforderung Vergleichsteilstelle“ dargestellt. Im unteren Abschnitt der Tabelle sind Räume aufgeführt, die lediglich in einer der Teilstellen erforderlich sind.


        Die Symbole am Beginn der Zeilen haben folgende Bedeutungen:
        
        **Gleiche Werte in beiden Tabellen = 🟩**  
        **Unterschiedliche Werte in beiden Tabellen = 🟥**  
        **Komplette Zeilen-Übereinstimmung = 🟢**  
        **Teilweise Übereinstimmung = 🟠**  
        **Keine Übereinstimmung = 🔴**  
        """)

        st.markdown(comparison_html, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Fehler beim Einlesen der Tabellen: {str(e)}")
    except Exception as e:
        st.error(f"❌ Fehler beim Einlesen der Tabellen: {str(e)}")
st.markdown("MediMetrics ist ein Universitätsprojekt der University of Applied Sciences im Rahmen des Moduls Nachhaltiges Betreiben von Objekten. Betreut von Kirch und Abel, entworfen von Kirchhoff, Kuehn, Merz, Ruell und Wecker.")
