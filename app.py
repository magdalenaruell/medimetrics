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

# 🌟 Stil-Optimierung für den Header
st.markdown(
    """
    <style>
    /* Gesamt-Header */
    .header-container {
        width: 100%;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding-top: 30px;
        padding-bottom: 40px;
        position: relative;
        background-color: #F2F3F4; /* Hellgrauer Hintergrund */
    }

    /* Farbverlauf-Hintergrund */
    .header-background {
        width: 100%;
        height: 280px;
        background: linear-gradient(to bottom, #ffffff, #4A8C45);
        border-bottom-left-radius: 40px;
        border-bottom-right-radius: 40px;
        position: absolute;
        top: 0;
        left: 0;
        z-index: -1;
    }

    /* Logo-Position oben rechts */
    .logo-container {
        position: absolute;
        top: 20px;
        right: 30px;
        z-index: 10;
    }

    .logo {
        width: 130px;
        height: 130px;
    }

    /* Titel */
    .header-title {
        font-size: 55px;
        font-weight: bold;
        font-family: 'Arial', sans-serif;
        color: #1A237E; /* Dunkelblau */
        margin-top: 50px;
        letter-spacing: 1px;
        text-shadow: 1px 1px 5px rgba(0,0,0,0.2);
    }

    /* Untertitel */
    .header-subtitle {
        font-size: 22px;
        font-weight: 300;
        color: #2C3E50;
        margin-bottom: 30px;
    }

    /* Grüne Infobox */
    .info-box {
        width: 80%;
        background: #4A8C45;
        color: white;
        padding: 20px;
        border-radius: 15px;
        font-size: 18px;
        text-align: left;
        margin-top: 20px;
        box-shadow: 3px 3px 15px rgba(0,0,0,0.2);
    }

    .info-box ul {
        padding-left: 20px;
    }

    .info-box li {
        padding: 5px 0;
    }

    /* Footer */
    .footer {
        width: 100%;
        text-align: center;
        background: #1A237E;
        color: white;
        padding: 10px;
        font-size: 14px;
        position: absolute;
        bottom: 0;
        left: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 📌 **Header mit PowerPoint-Design**
st.markdown('<div class="header-container">', unsafe_allow_html=True)

# Hintergrund hinzufügen
st.markdown('<div class="header-background"></div>', unsafe_allow_html=True)

# Logo rechts oben
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
st.image("https://raw.githubusercontent.com/magdalenaruell/medimetrics/main/IMG_07283.PNG", width=130)
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

# 📌 **Grüne Infobox mit Funktionen**
st.markdown(
    """
    <div class="info-box">
        <ul>
            <li>Online-Tool zum Vergleich der Funktionsbereiche und Flächenanforderungen</li>
            <li>Szenarien zur Untersuchung verschiedener Bedarfe eines Krankenhauses</li>
            <li>Gibt mögliche Flächen aus</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# 📌 **Footer**
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
        # **Tabellenblatt "Paulina" laden**
        sheet_name = "Paulina"
        df1 = pd.read_excel(file_url1, sheet_name=sheet_name, engine="openpyxl")
        df2 = pd.read_excel(file_url2, sheet_name=sheet_name, engine="openpyxl")

        st.success(f"📄 Dateien erfolgreich geladen: `{selected_file1}` & `{selected_file2}` (Tabellenblatt: {sheet_name})")

        # **Spaltennamen bereinigen & abgleichen**
        df1.columns = df1.columns.str.strip()
        df2.columns = df2.columns.str.strip()

        # **Nur gemeinsame Spalten behalten, um Versatz zu vermeiden**
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
            if col != "Räume in Funktionsbereichen":  # Diese Spalte wurde bereits indexiert
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
                    continue  # Diese Spalte wurde bereits indexiert
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
