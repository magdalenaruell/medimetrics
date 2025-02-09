import streamlit as st
import pandas as pd

# 🔗 GitHub-Repository mit den Excel-Dateien (ANPASSEN falls nötig)
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
    /* Zentriert die gesamte App */
    .block-container {
        max-width: 1200px;
        margin: auto;
        text-align: center;
    }

    /* Header Styling */
    .header-container {
        text-align: center;
        padding: 20px;
    }
    .header-title {
        font-size: 50px;
        font-weight: bold;
        color: white;
        background: linear-gradient(90deg, #1E90FF, #4B0082);
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.3);
    }

    /* Bild richtig zentrieren */
    .centered-image img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    /* Vergleichstabelle stylen */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: auto;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: center;
    }
    th {
        background-color: #f4f4f4;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 📌 Bild zentrieren
st.markdown('<div class="centered-image">', unsafe_allow_html=True)
st.image("IMG_07283.PNG", width=300)
st.markdown('</div>', unsafe_allow_html=True)

# 📌 Stilvollen Header anzeigen
st.markdown('<div class="header-container"><div class="header-title">MediMetrics </div></div>', unsafe_allow_html=True)

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
st.subheader("📂 Wähle die erste Excel-Datei")
selected_file1 = st.selectbox("📑 Erste Datei auswählen:", EXCEL_FILES, key="file1")

# 📂 **Zweite Excel-Datei auswählen**
st.subheader("📂 Wähle die zweite Excel-Datei")
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
