import streamlit as st
import time

# Konfiguration für mobile Geräte
st.set_page_config(
    page_title="Krümel-Abenteuer Deluxe",
    page_icon="🍪",
    layout="centered"
)

st.title("🍪 Das Krümelmonster Abenteuer XL")

# --- ZUSTAND SPEICHERN ---
if 'level' not in st.session_state:
    st.session_state.level = 'start'
# NEU: Ein Inventar (Rucksack)
if 'inventory' not in st.session_state:
    st.session_state.inventory = []

def set_level(neues_level):
    st.session_state.level = neues_level
    st.rerun()

# --- SEITENLEISTE (RUCKSACK) ---
with st.sidebar:
    st.header("🎒 Dein Rucksack")
    if len(st.session_state.inventory) == 0:
        st.write("Leer")
    else:
        for item in st.session_state.inventory:
            st.write(f"- {item}")

# --- LEVEL 1: VOR DEM HAUS ---
if st.session_state.level == 'start':
    st.write("Du stehst vor einem gruseligen Haus. 3 Türen liegen vor dir.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Tür 1 (Grün) 🟢"):
            st.session_state.vorgabe = "gruen"
            set_level('level2')
    with col2:
        if st.button("Tür 2 (Rot) 🔴"):
            st.session_state.vorgabe = "rot"
            set_level('level2')
    with col3:
        if st.button("Tür 3 (Rot) 🔴"):
            st.session_state.vorgabe = "rot"
            set_level('level2')

# --- LEVEL 2: IM FLUR (ERWEITERT) ---
elif st.session_state.level == 'level2':
    st.write("Du bist drinnen! Die Türen haben sich verändert...")
    st.info("Tipp: Eine dieser Türen führt vielleicht an einen sicheren Ort...")
    
    if st.session_state.vorgabe == "gruen":
        farben = ["🟢", "🟢", "🟢"]
    else:
        farben = ["🔴", "🔴", "🟢"]
        
    col1, col2, col3 = st.columns(3)

    # Tür 1: Führt zur Küche (NEU!)
    with col1:
        if st.button(f"Tür 1 {farben[0]}"): 
            set_level('kitchen')
            
    # Tür 2: Führt direkt zum Monster (Gefahr!)
    with col2:
        if st.button(f"Tür 2 {farben[1]}"): 
            set_level('monster')

    # Tür 3: Führt zu Poldi (Sofort Game Over)
    with col3:
        if st.button(f"Tür 3 {farben[2]}"): 
            set_level('poldi_trap')

# --- NEUES LEVEL: DIE KÜCHE ---
elif st.session_state.level == 'kitchen':
    st.header("🍽️ Die Küche")
    st.write("Du stehst in einer alten Küche. Es riecht herrlich!")
    
    if "🎂 Leckerer Kuchen" not in st.session_state.inventory:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Pound_layer_cake.jpg/320px-Pound_layer_cake.jpg", caption="Ein Kuchen!")
        if st.button("Kuchen einstecken"):
            st.session_state.inventory.append("🎂 Leckerer Kuchen")
            st.success("Du hast den Kuchen eingesteckt!")
            time.sleep(1)
            st.rerun()
    else:
        st.write("Die Küche ist leer. Du hast den Kuchen schon.")
        
    st.write("Es gibt hier nur eine Tür weiter...")
    if st.button("Durch die Hintertür gehen"):
        set_level('monster')

# --- LEVEL: POLDI FALLE ---
elif st.session_state.level == 'poldi_trap':
    st.header("🐉 POLDI IST HIER!")
    # Neues Bild für Poldi
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Poldi_the_dragon.jpg/320px-Poldi_the_dragon.jpg", caption="Poldi der Drache")
    st.error("Du bist direkt in Poldis Arme gelaufen!")
    st.write("'Ich will dich fressen!'")
    
    if st.button("Nochmal versuchen"):
        st.session_state.inventory = [] # Inventar leeren
        set_level('start')

# --- LEVEL 3: MONSTER ---
elif st.session_state.level == 'monster':
    # Funktionierendes Bild für das Krümelmonster
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Cookie_Monster.jpg/320px-Cookie_Monster.jpg", caption="Das Krümelmonster!")
    
    st.header("KRÜMELMONSTER!")
    st.write("Willst du mir Kekse geben?")
    
    # Automatische Option: Wenn man den Kuchen hat
    if "🎂 Leckerer Kuchen" in st.session_state.inventory:
        st.info("💡 Du hast einen Kuchen im Rucksack!")
        if st.button("🎂 Den Kuchen geben (Sieg)"):
            st.balloons()
            st.success("GEWONNEN! Das Monster liebt den Kuchen mehr als Kekse!")
            st.write("Es lässt dich frei und mampft glücklich den Kuchen.")
            if st.button("Neues Abenteuer starten"):
                st.session_state.inventory = []
                set_level('start')
            st.stop() # Hier aufhören, damit das Formular unten nicht mehr kommt

    # Normale Eingabe (falls man den Kuchen NICHT gefunden hat)
    with st.form(key='antwort_form'):
        antwort = st.text_input("Deine Antwort (ja/nein):")
        submit_button = st.form_submit_button(label='Antworten')
        
        if submit_button:
            # Cheat Code existiert immer noch
            if antwort.lower().strip() == "kuchen":
                st.success("GEWONNEN! (Du kanntest das Geheimwort!)")
                st.balloons()
            elif antwort.lower().strip() == "ja":
                st.error("Verloren! Es frisst die Kekse... und DICH! 💀")
            else:
                st.warning("Poldi kommt und frisst dich! 🐉")

    if st.button("Neustart"):
        st.session_state.inventory = []
        set_level('start')
