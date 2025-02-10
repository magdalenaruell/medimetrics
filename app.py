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

# 🔥 Vollbild-Optimierung mit CSS
st.markdown(
    """
    <style>
    /* Gesamt-Layout auf volle Breite setzen */
    .main-container {
        width: 100%;
        padding: 0;
        margin: 0;
    }

    /* Header-Hintergrund flächendeckend */
    .header-background {
        width: 100%;
        height: 250px;
        background: linear-gradient(to right, #1A237E, #4A8C45);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Logo & Titel im Header */
    .header-content {
        text-align: center;
        color: white;
        font-family: 'Arial', sans-serif;
    }

    .header-title {
        font-size: 55px;
        font-weight: bold;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    }

    .header-subtitle {
        font-size: 22px;
        font-weight: 300;
        color: #f0f0f0;
    }

    /* Grüne Infobox über volle Breite */
    .info-box {
        width: 100%;
        background: #4A8C45;
        color: white;
        padding: 20px;
        text-align: center;
        font-size: 20px;
        box-shadow: 3px 3px 15px rgba(0,0,0,0.2);
    }

    /* Szenario-Text auf volle Breite */
    .content-section {
        width: 80%;
        margin: auto;
        font-size: 18px;
        line-height: 1.6;
        text-align: justify;
    }

    /* Footer auf gesamte Breite */
    .footer {
        width: 100%;
        text-align: center;
        background: #1A237E;
        color: white;
        padding: 10px;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# 📌 *Header mit voller Breite*
st.markdown('<div class="header-background">', unsafe_allow_html=True)

# Logo & Titel im Header
st.markdown(
    """
    <div class="header-content">
        <img src="https://raw.githubusercontent.com/magdalenaruell/medimetrics/main/IMG_07283.PNG" width="130">
        <div class="header-title">MediMetrics</div>
        <div class="header-subtitle">Evaluierung der Raum- & Flächennutzung für maximale Effizienz im Krankenhaus</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

# 📌 *Grüne Infobox mit Funktionen*
st.markdown(
    """
    <div class="info-box">
        ✅ Online-Tool zum Vergleich der Funktionsbereiche und Flächenanforderungen  
        ✅ Szenarien zur Untersuchung verschiedener Bedarfe eines Krankenhauses  
        ✅ Gibt mögliche Flächen aus
    </div>
    """,
    unsafe_allow_html=True
)

# 📌 *Szenario-Bereich auf volle Breite*
st.markdown('<div class="content-section">', unsafe_allow_html=True)

st.markdown("""
    ### 🦠 Szenario: Pandemie
    Ein Krankenhaus erlebt eine massive Zunahme an Patienten aufgrund einer *hochansteckenden Atemwegserkrankung*, 
    die sich zu einer *Pandemie* ausgeweitet hat. Manche Patienten haben einen *milden Verlauf, andere einen **schwerwiegenden*.  
      
    *Erhöhte Flächennutzung:*  
    - *Intensivmedizin (2.03)* benötigt mehr Betten  
    - *Isolationskrankenpflege (2.06)* muss erweitert werden  
    - Andere Funktionsbereiche müssen flexibel umgewidmet werden  
""")

st.markdown('</div>', unsafe_allow_html=True)

# 📌 *Footer*
st.markdown(
    """
    <div class="footer">
        📅 11.02.2025 | Flächenmanagement im <span style="color:#FFCDD2;">Healthcare</span>-Sektor
    </div>
    """,
    unsafe_allow_html=True
)

       
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

# 📂 **Erste Datei auswählen oder hochladen**
st.subheader("📂 Wählen Sie die erste Datei für den Vergleich")
use_uploaded_file1 = st.checkbox("📤 Eigene Datei für erste Tabelle hochladen")
if use_uploaded_file1:
    uploaded_file1 = st.file_uploader("Laden Sie die erste Excel-Datei hoch", type=["xlsx"], key="upload1")
    selected_file1 = "Benutzerdefinierte Datei 1" if uploaded_file1 else None
else:
    selected_file1 = st.selectbox("📑 Erste Datei auswählen:", EXCEL_FILES, key="file1")

# 📂 **Zweite Datei auswählen oder hochladen**
st.subheader("📂 Wählen Sie die Vergleichstabelle")
use_uploaded_file2 = st.checkbox("📤 Eigene Datei für zweite Tabelle hochladen")
if use_uploaded_file2:
    uploaded_file2 = st.file_uploader("Laden Sie die zweite Excel-Datei hoch", type=["xlsx"], key="upload2")
    selected_file2 = "Benutzerdefinierte Datei 2" if uploaded_file2 else None
else:
    selected_file2 = st.selectbox("📑 Zweite Datei auswählen:", [f for f in EXCEL_FILES if f != selected_file1], key="file2")

# **Vergleich starten, wenn zwei gültige Dateien vorhanden sind**
if selected_file1 and selected_file2:
    try:
        # **Tabellenblatt "Paulina" laden**
        sheet_name = "Paulina"
        
        # Erste Datei laden
        if use_uploaded_file1 and uploaded_file1:
            df1 = pd.read_excel(uploaded_file1, sheet_name=sheet_name, engine="openpyxl")
        else:
            file_url1 = GITHUB_BASE_URL + selected_file1
            df1 = pd.read_excel(file_url1, sheet_name=sheet_name, engine="openpyxl")

        # Zweite Datei laden
        if use_uploaded_file2 and uploaded_file2:
            df2 = pd.read_excel(uploaded_file2, sheet_name=sheet_name, engine="openpyxl")
        else:
            file_url2 = GITHUB_BASE_URL + selected_file2
            df2 = pd.read_excel(file_url2, sheet_name=sheet_name, engine="openpyxl")

        st.success(f"📄 Dateien erfolgreich geladen: `{selected_file1}` & `{selected_file2}` (Tabellenblatt: {sheet_name})")

        # **Spaltennamen bereinigen & abgleichen**
        df1.columns = df1.columns.str.strip()
        df2.columns = df2.columns.str.strip()

        # **Nur gemeinsame Spalten behalten**
        common_columns = df1.columns.intersection(df2.columns)
        df1 = df1[common_columns]
        df2 = df2[common_columns]

        # **Beide Tabellen nach "Räume in Funktionsbereichen" indexieren**
        if "Räume in Funktionsbereichen" not in common_columns:
            st.error("❌ Die Spalte 'Räume in Funktionsbereichen' existiert nicht in beiden Dateien.")
            st.stop()

        df1_grouped = df1.set_index("Räume in Funktionsbereichen")
        df2_grouped = df2.set_index("Räume in Funktionsbereichen")

        # **Gemeinsame & individuelle Zeilen identifizieren**
        common_rows = df1_grouped.index.intersection(df2_grouped.index)
        unique_to_df1 = df1_grouped.index.difference(df2_grouped.index)
        unique_to_df2 = df2_grouped.index.difference(df1_grouped.index)

        # **Vergleichstabelle als HTML generieren**
        comparison_html = "<table border='1' style='width:100%; border-collapse: collapse;'><thead><tr>"
        comparison_html += "<th>Vergleich</th><th>Räume in Funktionsbereichen</th>"

        for col in common_columns:
            if col != "Räume in Funktionsbereichen":
                comparison_html += f"<th>{col}</th>"
        comparison_html += "</tr></thead><tbody>"

        def ensure_dataframe(row):
            """ Sicherstellen, dass jede Zeile als DataFrame verarbeitet wird """
            return row.to_frame().T if isinstance(row, pd.Series) else row

        # **Vergleich gemeinsame Zeilen**
        for row in common_rows:
            row1 = ensure_dataframe(df1_grouped.loc[row])
            row2 = ensure_dataframe(df2_grouped.loc[row])
            row_styles = []
            match_status = "🟢"

            for col in common_columns:
                if col == "Räume in Funktionsbereichen":
                    continue
                val1 = row1[col].values[0] if col in row1.columns else "—"
                val2 = row2[col].values[0] if col in row2.columns else "—"

                if val1 == val2:
                    row_styles.append(f"<td style='background-color: #90EE90;'>{val1}</td>")
                else:
                    row_styles.append(f"<td style='background-color: #FF4500; font-weight:bold;'>{val1} | {val2}</td>")
                    match_status = "🟠"

            comparison_html += f"<tr><td>{match_status}</td><td>{row}</td>{''.join(row_styles)}</tr>"

        # **Zeilen, die nur in der ersten Tabelle existieren**
        for row in unique_to_df1:
            row1 = ensure_dataframe(df1_grouped.loc[row])
            row_html = f"<tr><td>🔴</td><td>{row}</td>"
            for col in common_columns:
                if col != "Räume in Funktionsbereichen":
                    row_html += f"<td>{row1[col].values[0] if col in row1.columns else '—'}</td>"
            row_html += "</tr>"
            comparison_html += row_html

        # **Zeilen, die nur in der zweiten Tabelle existieren**
        for row in unique_to_df2:
            row2 = ensure_dataframe(df2_grouped.loc[row])
            row_html = f"<tr><td>🔴</td><td>{row}</td>"
            for col in common_columns:
                if col != "Räume in Funktionsbereichen":
                    row_html += f"<td>{row2[col].values[0] if col in row2.columns else '—'}</td>"
            row_html += "</tr>"
            comparison_html += row_html

        comparison_html += "</tbody></table>"
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
