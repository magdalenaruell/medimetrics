import streamlit as st
import pandas as pd

# 🔗 GitHub-Repository mit den Excel-Dateien
GITHUB_BASE_URL = "https://raw.githubusercontent.com/magdalenaruell/medimetrics/main/"

# 📂 Liste der Excel-Dateien
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

# 🌟 Stil-Optimierung für die App
st.markdown(
    """
    <style>
    /* Gesamtanpassung */
    .block-container {
        max-width: 900px;
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
        text-align: center;
        padding: 10px;
    }

    /* Logo zentrieren */
    .logo-container {
        justify-content: center;
        align-items: center;
        margin-bottom: 10px;
    }

    .logo {
        width: 150px;
        background: white;
        padding: 8px;
        border-radius: 80%;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.15);
    }

    .header-title {
        font-size: 42px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }

    .header-subtitle {
        font-size: 18px;
        color: #4b5563;
        text-align: center;
        margin-top: 5px;
    }

    /* Vergleichstabelle */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: auto;
        border-radius: 10px;
        overflow: hidden;
        background: white;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }

    th, td {
        border: 1px solid #ddd;
        padding: 12px;
        text-align: center;
    }

    th {
        background-color: #e3f2fd;
        font-weight: bold;
    }

    td {
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 📌 Header mit zentriertem Logo anzeigen
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
st.image("https://raw.githubusercontent.com/magdalenaruell/medimetrics/main/IMG_07283.PNG", width=120)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="header-title">MediMetrics</div>
    <div class="header-subtitle">Optimierung der Raum- & Flächennutzung für maximale Effizienz im Krankenhaus</div>
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

        df1["Tabelle"] = selected_file1
        df2["Tabelle"] = selected_file2

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
                <th>Tabelle</th>
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

            row_html = f"<tr><td>{match_status}</td><td>{row}</td><td>{selected_file1}</td>{''.join(row_styles)}</tr>"
            comparison_html += row_html
            row_html = f"<tr><td>{match_status}</td><td>{row}</td><td>{selected_file2}</td>{''.join(row_styles)}</tr>"
            comparison_html += row_html

        # **Zeilen, die nur in der ersten Tabelle existieren**
        for row in unique_to_df1:
            row1 = ensure_dataframe(df1_grouped.loc[row])
            row_html = f"<tr><td>🔴</td><td>{row}</td><td>{selected_file1}</td>"
            for col in df1.columns:
                row_html += f"<td>{row1[col].values[0] if col in row1.columns else '—'}</td>"
            row_html += "</tr>"
            comparison_html += row_html

        # **Zeilen, die nur in der zweiten Tabelle existieren**
        for row in unique_to_df2:
            row2 = ensure_dataframe(df2_grouped.loc[row])
            row_html = f"<tr><td>🔴</td><td>{row}</td><td>{selected_file2}</td>"
            for col in df2.columns:
                row_html += f"<td>{row2[col].values[0] if col in row2.columns else '—'}</td>"
            row_html += "</tr>"
            comparison_html += row_html

        comparison_html += "</table>"

        st.subheader("📊 Vergleich der Tabellen")
        st.markdown(comparison_html, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Fehler beim Einlesen der Tabellen: {str(e)}")
st.subheader("MediMetrics ist ein Universitätsprojekt der University of Applied Sciences im Rahmen des Moduls Nachhaltiges Betreiben von Objekten. Betreut von Kirch und Abel, entworfen von Kirchhoff, Kuehn, Merz, Ruell und Wecker.")
