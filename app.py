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
        xls1 = pd.ExcelFile(file_url1)
        xls2 = pd.ExcelFile(file_url2)
        sheet_names1 = xls1.sheet_names
        sheet_names2 = xls2.sheet_names
        st.success(f"📄 Dateien erfolgreich geladen: `{selected_file1}` & `{selected_file2}`")
    except Exception as e:
        st.error(f"❌ Fehler beim Laden der Dateien: {str(e)}")
        st.stop()
    
     # 📑 **Tabellenblatt für jede Datei auswählen**
    st.subheader("📄 Wähle ein Tabellenblatt für jede Datei")
    selected_sheet1 = st.selectbox("📄 Tabellenblatt für die erste Datei:", sheet_names1, key="sheet1")
    selected_sheet2 = st.selectbox("📄 Tabellenblatt für die zweite Datei:", sheet_names2, key="sheet2")

    if selected_sheet1 and selected_sheet2:
        try:
            df1 = pd.read_excel(xls1, sheet_name=selected_sheet1, engine="openpyxl")
            df2 = pd.read_excel(xls2, sheet_name=selected_sheet2, engine="openpyxl")

            # Sicherstellen, dass Spalte B existiert
            if "Räume in Funktionsbereichen" not in df1.columns or "Räume in Funktionsbereichen" not in df2.columns:
                st.error("❌ Die Spalte 'Räume in Funktionsbereichen' (Spalte B) existiert nicht in einer oder beiden Dateien.")
                st.stop()

            # Daten nach "Räume in Funktionsbereichen" zusammenfassen
            df1_grouped = df1.set_index("Räume in Funktionsbereichen")
            df2_grouped = df2.set_index("Räume in Funktionsbereichen")

            # Gemeinsame Zeilen identifizieren
            common_rows = df1_grouped.index.intersection(df2_grouped.index)

            # Neue DataFrame für Vergleich erstellen
            comparison_results = []
            for row in common_rows:
                row1 = df1_grouped.loc[row]
                row2 = df2_grouped.loc[row]

                # Falls nur eine Zeile, sicherstellen, dass sie als DataFrame bleibt
                row1 = row1.to_frame().T if isinstance(row1, pd.Series) else row1
                row2 = row2.to_frame().T if isinstance(row2, pd.Series) else row2

                row_styles = []
                match_status = "🟢"  # Standard auf "komplett gleich"

                for col in row1.columns:
                    if col not in row2.columns:
                        continue
                    val1, val2 = row1[col].values[0], row2[col].values[0]

                    if pd.isna(val1) and pd.isna(val2):
                        row_styles.append(f"<td>{val1}</td>")
                    elif val1 == val2:
                        row_styles.append(f"<td style='background-color: #90EE90;'>{val1}</td>")  # Grün für gleiche Werte
                    else:
                        row_styles.append(f"<td style='background-color: #FF4500; font-weight:bold;'>{val1} | {val2}</td>")  # Rot für unterschiedliche Werte
                        match_status = "🟠"  # Falls Unterschiede existieren

                # Falls die gesamte Zeile gleich ist, bleibt "🟢", ansonsten "🟠"
                if all("#90EE90" in s for s in row_styles):
                    match_status = "🟢"
                elif any("#FF4500" in s for s in row_styles):
                    match_status = "🟠"
                else:
                    match_status = "🔴"

                comparison_results.append((match_status, row, row_styles))

            # 📌 Tabellen nebeneinander anzeigen
            st.subheader(f"📊 Vergleich der Tabellen: {selected_file1} vs. {selected_file2}")

            col1, col2 = st.columns(2)

            with col1:
                st.subheader(f"📄 {selected_file1}")
                st.dataframe(df1)

            with col2:
                st.subheader(f"📄 {selected_file2}")
                st.dataframe(df2)

            # 📌 Ergebnisse in HTML anzeigen
            if comparison_results:
                styled_rows = [f"<tr><td>{status}</td><td>{title}</td>{''.join(row_styles)}</tr>" for status, title, row_styles in comparison_results]
                table_html = f"""
                <table>
                    <tr>
                        <th>Vergleich</th>
                        <th>Räume in Funktionsbereichen</th>
                        <th>Details</th>
                    </tr>
                    {''.join(styled_rows)}
                </table>
                """
                st.markdown(table_html, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Fehler beim Einlesen der Tabellen: {str(e)}")
