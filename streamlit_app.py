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

# --- LEVEL: KÜCHE ---
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

# --- LEVEL 3: MONSTER BEGEGNUNG ---
elif st.session_state.level == 'monster':
    st.image("https://scontent-ber1-1.xx.fbcdn.net/v/t1.6435-9/107968189_3082919061797626_1526527550134192230_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=833d8c&_nc_ohc=HAtUpzOklfkQ7kNvwFTU4zH&_nc_oc=Adksa_eXSXC71dPytMddq4ee2jd7MzibxAtVA2vweHvWDeAA28sHgbeHeJo2Ek-opVQ&_nc_zt=23&_nc_ht=scontent-ber1-1.xx&_nc_gid=Kyl_sDN-03dL2fbCSA184g&oh=00_AfggCKhmcVsvBcaEsTRXzPvhl9QMp8nYsP_N9JwEG_Hr5Q&oe=695515C5", caption="Das Krümelmonster!")
    
    st.header("KRÜMELMONSTER!")
    st.info('"Egal, was die Frage ist, die Antwort ist Keks!"')
    st.write('"Irgendwo ist immer Kekszeit..."')
    st.write("Willst du mir Kekse geben?")
    
    # 1. Option: Kuchen geben (Sicherer Sieg)
    if "🎂 Leckerer Kuchen" in st.session_state.inventory:
        st.info("💡 Du hast einen Kuchen im Rucksack!")
        if st.button("🎂 Den Kuchen geben (Sieg)"):
            set_level('win')

    # 2. Option: Text-Eingabe (Risiko)
    with st.form(key='antwort_form'):
        antwort = st.text_input("Deine Antwort (ja/nein):")
        submit_button = st.form_submit_button(label='Antworten')
        
        if submit_button:
            eingabe = antwort.lower().strip()
            
            if eingabe == "kuchen":
                set_level('win') # Geheimwort -> Sieg
            elif eingabe == "ja":
                set_level('game_over_monster') # Falsche Antwort -> Gefressen
            else:
                set_level('poldi_trap') # Andere Antwort -> Poldi

# --- ENDE: GEWONNEN ---
elif st.session_state.level == 'win':
    st.balloons()
    st.header("🎉 GEWONNEN!")
    st.success("Das Monster liebt Kuchen (und das Geheimwort) viel mehr als Kekse!")
    st.write("Es mampft glücklich vor sich hin und lässt dich frei.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Heart_coraz%C3%B3n.svg/120px-Heart_coraz%C3%B3n.svg.png")
    
    if st.button("Neues Abenteuer starten"):
        st.session_state.inventory = []
        set_level('start')

# --- ENDE: GEFRESSEN VOM MONSTER ---
elif st.session_state.level == 'game_over_monster':
    st.header("💀 GAME OVER")
    st.error("Du hast 'Ja' gesagt...")
    st.write("Das Monster hat die Kekse gegessen... und weil es immer noch Hunger hatte, auch DICH!")
    
    if st.button("Nochmal versuchen"):
        st.session_state.inventory = []
        set_level('start')

# --- ENDE: POLDI FALLE ---
elif st.session_state.level == 'poldi_trap':
    st.header("🐉 POLDI IST HIER!")
    st.image("https://static.wikia.nocookie.net/drachen/images/1/12/162Poldi.JPG/revision/latest?cb=20150513111928&path-prefix=de", caption="Poldi der Drache")
    st.error("Falsche Entscheidung! Poldi hat dich erwischt.")
    st.write("'Ich will dir fressen!'")
    
    if st.button("Nochmal versuchen"):
        st.session_state.inventory = [] 
        set_level('start')
