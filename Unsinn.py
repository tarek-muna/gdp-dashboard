import streamlit as st
import random
import time

# Konfiguration der Seite
st.set_page_config(
    page_title="Unsinn-Radar 3000",
    page_icon="🚨",
    layout="centered"
)

# Überschrift und Erklärung
st.title("🚨 Der Unsinn-Radar 3000")
st.write("Dieses Hochtechnologie-Gerät prüft wissenschaftlich genau (nicht wirklich), ob dein Text schlau ist oder totaler Quatsch.")

# Eingabefeld für den Benutzer
user_text = st.text_area("Gib hier deinen Satz oder eine Geschichte ein:", height=150)

# Der Button zum Starten
if st.button("Auf Unsinn scannen"):
    if user_text.strip() == "":
        st.warning("Du musst erst etwas schreiben, sonst kann ich nichts scannen!")
    else:
        # 1. Spannung aufbauen (Ladebalken)
        progress_text = "Scanne auf Blödsinn..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01) # Kleine Pause für den Effekt
            my_bar.progress(percent_complete + 1, text=progress_text)
        
        # 2. Zufälligen Unsinn-Wert berechnen (0 bis 100)
        # random.randint(a, b) wählt eine zufällige Zahl zwischen a und b
        unsinn_level = random.randint(0, 100)

        # 3. Das Ergebnis anzeigen
        st.markdown("---") # Trennlinie
        st.header(f"Ergebnis: {unsinn_level}% Unsinn")
        
        # Je nach Höhe des Wertes eine andere Nachricht anzeigen
        if unsinn_level < 20:
            st.success("✅ Dieser Text ergibt Sinn! (Langweilig...)")
        elif unsinn_level < 50:
            st.info("🤔 Ein bisschen Quatsch ist dabei, aber es geht noch.")
        elif unsinn_level < 80:
            st.warning("⚠️ Vorsicht! Der Unsinn-Pegel steigt gefährlich an!")
        else:
            st.error("🚨 ALARM! TOTALER BLÖDSINN ERKANNT! 🤯")
            st.balloons() # Konfetti-Ballons fliegen lassen
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGZ4eXF4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4/l0HlCqV9bVuyyGuiA/giphy.gif", caption="System überlastet!")

# Fußzeile
st.markdown("---")
st.caption("Der Unsinn-Radar 3000 - Zertifiziert für Quatsch-Comedy.")
