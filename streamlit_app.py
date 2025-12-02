import streamlit as st
import time
import random # Neu importiert für zufällige Sprüche

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
# Ein Inventar (Rucksack)
if 'inventory' not in st.session_state:
    st.session_state.inventory = []

def set_level(neues_level):
    st.session_state.level = neues_level
    st.rerun()

# --- SEITENLEISTE (RUCKSACK & JASPER) ---
with st.sidebar:
    # 1. Das Inventar
    st.header("🎒 Dein Rucksack")
    if len(st.session_state.inventory) == 0:
        st.write("Leer")
    else:
        for item in st.session_state.inventory:
            st.write(f"- {item}")
            
    st.markdown("---")
    
    # 2. NEU: JASPER DER GEIST
    st.header("👻 Jasper")
    st.image("https://media.giphy.com/media/13pHvYs3p4tQBO/giphy.gif", caption="Dein Geister-Freund")
    
    # Jaspers Tipps basierend auf dem Level
    st.write("**Jasper flüstert:**")
    
    lvl = st.session_state.level
    
    if lvl == 'start':
        st.info("'Psst! Ich glaube, die grünen Türen sind freundlicher als die roten.'")
    elif lvl == 'level2':
        st.info("'Es riecht nach Essen aus einer Richtung... vielleicht gibt es da was Nützliches?'")
    elif lvl == 'kitchen':
        if "🎂 Leckerer Kuchen" in st.session_state.inventory:
            st.success("'Lecker! Den Kuchen sollten wir dem Monster bringen!'")
        else:
            st.warning("'Siehst du den Kuchen? Steck ihn ein, bevor wir gehen!'")
    elif lvl == 'living_room':
        st.warning("'Sei ganz leise... das Monster ist im nächsten Raum!'")
    elif lvl == 'garden':
        st.error("'Achtung! Ich spüre Drachen-Atem. Geh nicht hinter den Busch!'")
    elif lvl == 'monster':
        if "🎂 Leckerer Kuchen" in st.session_state.inventory:
            st.success("'Gib ihm den Kuchen! Schnell!'")
        else:
            st.error("'Oh nein! Ohne Kuchen sind wir verloren... Sag bloß nicht JA!'")
    elif lvl == 'cellar':
        st.info("'Der linke Tunnel sieht düster aus... Ich würde nach RECHTS gehen.'")
    elif lvl == 'treasure':
        st.balloons()
        st.write("'Wir sind reich! Juhu!'")
    elif lvl == 'prison':
        st.write("'Ups... da kann ich uns auch nicht durchwände-glitschen.'")
    else:
        st.write("'Ich passe auf dich auf!'")

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

# --- LEVEL 2: IM FLUR ---
elif st.session_state.level == 'level2':
    st.write("Du bist drinnen! Ein langer Flur erstreckt sich vor dir...")
    st.info("Wohin möchtest du gehen?")
    
    if st.session_state.vorgabe == "gruen":
        farben = ["🟢", "🟢", "🟢"]
    else:
        farben = ["🔴", "🔴", "🟢"]
        
    col1, col2, col3 = st.columns(3)

    # Tür 1: Zur Küche
    with col1:
        if st.button(f"Tür 1 (Küche) {farben[0]}"): 
            set_level('kitchen')
            
    # Tür 2: Zum Wohnzimmer
    with col2:
        if st.button(f"Tür 2 (Stube) {farben[1]}"): 
            set_level('living_room')

    # Tür 3: Zum Garten
    with col3:
        if st.button(f"Tür 3 (Garten) {farben[2]}"): 
            set_level('garden')

# --- LEVEL: KÜCHE ---
elif st.session_state.level == 'kitchen':
    st.header("🍽️ Die Küche")
    st.write("Es duftet herrlich, aber es ist niemand hier.")
    
    if "🎂 Leckerer Kuchen" not in st.session_state.inventory:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Pound_layer_cake.jpg/320px-Pound_layer_cake.jpg", caption="Ein Kuchen!")
        if st.button("Kuchen einstecken"):
            st.session_state.inventory.append("🎂 Leckerer Kuchen")
            st.success("Du hast den Kuchen eingesteckt!")
            time.sleep(1)
            st.rerun()
    else:
        st.write("Die Küche ist leer. Den Kuchen hast du schon.")
        
    st.write("**Deine Optionen:**")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➡️ Zum Wohnzimmer gehen"):
            set_level('living_room')
    with col2:
        if st.button("▼ In den Keller absteigen"):
            set_level('cellar')

# --- NEU: LEVEL WOHNZIMMER ---
elif st.session_state.level == 'living_room':
    st.header("🛋️ Das Wohnzimmer")
    st.write("Ein gemütliches Sofa steht hier. Aber du hörst ein schweres Atmen aus dem nächsten Raum...")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Living_room_with_fireplace.jpg/320px-Living_room_with_fireplace.jpg")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬅️ Zur Küche"):
            set_level('kitchen')
    with col2:
        if st.button("🚪 Tür öffnen (Geräusch)"):
            set_level('monster')
    with col3:
        if st.button("▼ Keller-Luke öffnen"):
            set_level('cellar')

# --- NEU: LEVEL GARTEN ---
elif st.session_state.level == 'garden':
    st.header("🌳 Der neblige Garten")
    st.write("Draußen ist es kalt und neblig. Hinter einem Busch leuchten zwei Augen...")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Ash_Tree_in_Mist%2C_Whitney_-_geograph.org.uk_-_1068884.jpg/320px-Ash_Tree_in_Mist%2C_Whitney_-_geograph.org.uk_-_1068884.jpg")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔎 Hinter den Busch schauen"):
            set_level('poldi_trap')
    with col2:
        if st.button("▼ In das Erdloch springen (Keller)"):
            set_level('cellar')

# --- LEVEL 3: MONSTER BEGEGNUNG ---
elif st.session_state.level == 'monster':
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Cookie_Monster.jpg/320px-Cookie_Monster.jpg", caption="Das Krümelmonster!")
    
    st.header("KRÜMELMONSTER!")
    st.info('"Egal, was die Frage ist, die Antwort ist Keks!"')
    st.write("Willst du mir Kekse geben?")
    
    # Flucht
    if st.button("🏃 Schnell weg hier! (In den Keller flüchten)"):
        set_level('cellar')
    
    # 1. Option: Kuchen
    if "🎂 Leckerer Kuchen" in st.session_state.inventory:
        st.info("💡 Du hast einen Kuchen im Rucksack!")
        if st.button("🎂 Den Kuchen geben (Sieg)"):
            set_level('win')

    # 2. Option: Eingabe
    with st.form(key='antwort_form'):
        antwort = st.text_input("Deine Antwort (ja/nein):")
        submit_button = st.form_submit_button(label='Antworten')
        
        if submit_button:
            eingabe = antwort.lower().strip()
            if eingabe == "kuchen": set_level('win')
            elif eingabe == "ja": set_level('game_over_monster')
            else: set_level('poldi_trap')

# --- LEVEL: POLDI FALLE ---
elif st.session_state.level == 'poldi_trap':
    st.header("🐉 POLDI IST HIER!")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Poldi_the_dragon.jpg/320px-Poldi_the_dragon.jpg", caption="Poldi der Drache")
    st.error("Du bist Poldi in die Arme gelaufen!")
    st.write("'Ich will dir fressen!'")
    
    if st.button("🏃 Versuch in den Keller zu entkommen!"):
        set_level('cellar')
    
    if st.button("Aufgeben (Neustart)"):
        st.session_state.inventory = [] 
        set_level('start')

# --- LEVEL KELLER (ERWEITERT) ---
elif st.session_state.level == 'cellar':
    st.header("🕸️ Der dunkle Keller")
    st.write("Du bist im Keller gelandet. Es ist dunkel, aber du siehst zwei Tunnel.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("Linker Tunnel")
        if st.button("👈 Nach Links gehen"):
            set_level('prison')
            
    with col2:
        st.success("Rechter Tunnel")
        if st.button("👉 Nach Rechts gehen"):
            set_level('treasure')

# --- LEVEL GEFÄNGNIS (GAME OVER) ---
elif st.session_state.level == 'prison':
    st.header("⛓️ GEFÄNGNIS")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Prison_bars.jpg/320px-Prison_bars.jpg", caption="Gefangen!")
    st.error("Sackgasse! Du bist in einer alten Zelle gelandet.")
    st.write("**Du hast verloren.**")
    
    if st.button("Neues Abenteuer starten"):
        st.session_state.inventory = []
        set_level('start')

# --- NEU: LEVEL SCHATZKAMMER (WIN) ---
elif st.session_state.level == 'treasure':
    st.balloons()
    st.header("💎 SCHATZKAMMER!")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Treasure_chest_closed.svg/320px-Treasure_chest_closed.svg.png")
    st.success("Du hast den geheimen Ausgang gefunden!")
    st.write("Hier liegt ein riesiger Haufen Goldkekse. Du bist reich!")
    
    if st.button("Reich und glücklich neustarten"):
        st.session_state.inventory = []
        set_level('start')

# --- ENDE: GEWONNEN (MONSTER) ---
elif st.session_state.level == 'win':
    st.balloons()
    st.header("🎉 GEWONNEN!")
    st.success("Das Monster liebt Kuchen!")
    st.write("Es mampft glücklich vor sich hin und lässt dich frei.")
    
    if st.button("Neues Abenteuer starten"):
        st.session_state.inventory = []
        set_level('start')

# --- ENDE: GEFRESSEN ---
elif st.session_state.level == 'game_over_monster':
    st.header("💀 GAME OVER")
    st.error("Das Monster hat dich gefressen!")
    
    if st.button("Nochmal versuchen"):
        st.session_state.inventory = []
        set_level('start')
