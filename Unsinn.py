import streamlit as st
import random
import time

# Konfiguration der Seite
st.set_page_config(
    page_title="Unsinn-Radar 3000 Pro",
    page_icon="🚨",
    layout="centered"
)

# --- SEITENLEISTE (EINSTELLUNGEN) ---
with st.sidebar:
    st.header("⚙️ Einstellungen")
    st.write("Konfiguriere den Scanner:")
    
    # Ein Schieberegler für die "Strenge"
    strenge = st.slider("Empfindlichkeit", 0, 100, 50)
    st.caption("0 = Alles ist sinnvoll | 100 = Alles ist Quatsch")
    
    # Checkbox für Experten-Modus
    experten_modus = st.checkbox("Wissenschaftliche Analyse anzeigen")
    
    st.markdown("---")
    st.info("Version 2.0 - Jetzt mit KI (Keine Intelligenz)")

# --- HAUPTBEREICH ---
st.title("🚨 Der Unsinn-Radar 3000 Pro")
st.write("Dieses Hochtechnologie-Gerät prüft wissenschaftlich genau, ob dein Text schlau ist oder totaler Quatsch.")

# Eingabefeld
user_text = st.text_area("Gib hier deinen Satz oder eine Geschichte ein:", height=150)

# Liste mit lustigen "Gründen" für die Analyse
lustige_gruende = [
    "Zu viele Vokale an der falschen Stelle.",
    "Der Text riecht ein bisschen nach Käse.",
    "Die Logik hat gerade Urlaub genommen.",
    "Klingt verdächtig nach einem Alien.",
    "Grammatik wurde nicht gefunden.",
    "Dieser Satz dreht sich im Kreis.",
    "Enthält Spuren von Wahnsinn.",
    "Mein Hamster tippt sinnvoller.",
    "Gefahr von Gehirnknoten erkannt!"
]

if st.button("Auf Unsinn scannen"):
    if user_text.strip() == "":
        st.warning("Du musst erst etwas schreiben, sonst kann ich nichts scannen!")
    else:
        # 1. Ladebalken Animation
        progress_text = "Kalibriere Quatsch-Sensoren..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            # Text im Ladebalken ändern
            if percent_complete == 30: progress_text = "Analysiere Buchstaben..."
            if percent_complete == 60: progress_text = "Berechne Sinnlosigkeit..."
            my_bar.progress(percent_complete + 1, text=progress_text)
        
        my_bar.empty() # Balken ausblenden, wenn fertig

        # 2. Unsinn-Wert berechnen
        # Der Schieberegler beeinflusst das Ergebnis ein bisschen
        zufall = random.randint(0, 100)
        # Wir verrechnen den Zufall mit der eingestellten Strenge
        unsinn_level = int((zufall + strenge) / 2)
        
        # Sicherstellen, dass es zwischen 0 und 100 bleibt
        if unsinn_level > 100: unsinn_level = 100

        # 3. Ergebnis anzeigen
        st.markdown("---")
        
        # Große Zahl anzeigen
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(label="Unsinn-Level", value=f"{unsinn_level}%")
        
        with col2:
            if unsinn_level < 20:
                st.success("✅ Dieser Text ergibt absolut Sinn! (Langweilig...)")
            elif unsinn_level < 50:
                st.info("🤔 Ein bisschen Quatsch ist dabei, aber okay.")
            elif unsinn_level < 80:
                st.warning("⚠️ Vorsicht! Der Unsinn-Pegel ist kritisch!")
            else:
                st.error("🚨 ALARM! TOTALER BLÖDSINN ERKANNT! 🤯")
                st.balloons()
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGZ4eXF4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4/l0HlCqV9bVuyyGuiA/giphy.gif", caption="System überlastet!")

        # 4. Experten-Analyse (nur wenn angehakt)
        if experten_modus:
            st.markdown("---")
            st.subheader("🔬 Wissenschaftliche Analyse:")
            # Wir wählen 3 zufällige Gründe aus der Liste
            gruende = random.sample(lustige_gruende, 3)
            
            for grund in gruende:
                st.write(f"❌ {grund}")

# Fußzeile
st.markdown("---")
st.caption("Der Unsinn-Radar 3000 Pro - Jetzt noch bunter.")
