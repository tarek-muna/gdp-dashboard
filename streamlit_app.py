import streamlit as st
import time
import random 

# Konfiguration für mobile Geräte
st.set_page_config(
    page_title="Krümel-Abenteuer Deluxe",
    page_icon="🍪",
    layout="centered"
)

# Hilfsfunktion für riesige Emojis
def riesen_emoji(emoji):
    st.markdown(f"<div style='text-align: center; font-size: 100px;'>{emoji}</div>", unsafe_allow_html=True)

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
    
    # 2. JASPER DER GEIST
    st.header("👻 Jasper")
    riesen_emoji("👻")
    st.caption("Dein Geister-Freund")
    
    # Jaspers Tipps basierend auf dem Level
    st.write("**Jasper flüstert:**")
    
    lvl = st.session_state.level
    
    if lvl == 'start':
        st.info("'Psst! Ich glaube, die grünen Türen sind freundlicher als die roten.'")
    elif lvl == 'level2':
        st.info("'Da ist eine Leiter nach oben... Und eine Tür, hinter der jemand schnarcht?'")
    elif lvl == 'kitchen':
        if "🎂 Leckerer Kuchen" in st.session_state.inventory:
            st.success("'Ein Geschenk in der Hand öffnet vielleicht Türen...'")
        else:
            st.warning("'Niemals mit leeren Händen zu einem hungrigen Gastgeber gehen!'")
    elif lvl == 'living_room':
        st.info("'Hinter dem Bücherregal zieht es... gibt es da einen geheimen Raum?'")
    elif lvl == 'garden':
        st.error("'Hier ist es neblig. Klettere lieber hoch ins Baumhaus, da ist es sicher!'")
    elif lvl == 'monster':
        if "🎂 Leckerer Kuchen" in st.session_state.inventory:
            st.success("'Worte machen nicht satt. Taten (und Gebäck) schon.'")
        else:
            st.error("'Vorsicht mit dem, was du sagst. Er nimmt alles wörtlich - auch dich!'")
    elif lvl == 'cellar':
        st.info("'Im Zweifel ist das Rechte oft das Richtige... Aber links höre ich Stimmen?'")
    elif lvl == 'treasure':
        st.balloons()
        st.write("'Glitzer! Funkel! Wir haben es geschafft!'")
    elif lvl == 'prison':
        st.error("'Tja... Wände sind leider sehr fest.'")
    elif lvl == 'attic':
        st.info("'Pass auf den Kopf auf! Die Rutsche nach draußen sieht lustig aus.'")
    elif lvl == 'library':
        st.success("'Bücher sind der Schlüssel zur Weisheit... und manchmal auch zu geheimen Gängen.'")
    elif lvl == 'treehouse':
        st.info("'Die Seilbahn ist der schnellste Weg zurück ins Warme!'")
    elif lvl == 'bedroom':
        st.warning("'Pst! Nicht das Monster unter dem Bett wecken... Geh lieber ins Kinderzimmer.'")
    elif lvl == 'kids_room':
        st.info("'Die Spielzeugkiste sieht verdächtig aus... ob da ein Tunnel drin ist?'")
    elif lvl == 'dungeon':
        st.info("'Die beiden kenne ich aus dem Fernsehen! Wir müssen ihnen helfen!'")
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

# --- LEVEL 2: IM FLUR (ERWEITERT) ---
elif st.session_state.level == 'level2':
    st.write("Du bist drinnen! Ein langer Flur erstreckt sich vor dir...")
    st.info("Wohin möchtest du gehen?")
    
    if st.session_state.vorgabe == "gruen":
        farben = ["🟢", "🟢", "🟢"]
    else:
        farben = ["🔴", "🔴", "🟢"]
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"Tür 1 (Küche) {farben[0]}"): set_level('kitchen')
        if st.button(f"Tür 3 (Garten) {farben[2]}"): set_level('garden')
        if st.button("🚪 Tür 4 (Schlafzimmer)"): set_level('bedroom')
    with col2:
        if st.button(f"Tür 2 (Stube) {farben[1]}"): set_level('living_room')
        if st.button("🪜 Leiter nach oben"): set_level('attic')

# --- LEVEL: SCHLAFZIMMER ---
elif st.session_state.level == 'bedroom':
    st.header("🛏️ Das alte Schlafzimmer")
    st.write("Ein riesiges Himmelbett steht hier. Es staubt gewaltig.")
    riesen_emoji("🛏️💤")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔙 Zurück zum Flur"):
            set_level('level2')
        if st.button("▼ Unters Bett schauen (Keller)"):
            set_level('cellar')
    with col2:
        if st.button("🧸 Tür zum Kinderzimmer"):
            set_level('kids_room')

# --- LEVEL: KINDERZIMMER ---
elif st.session_state.level == 'kids_room':
    st.header("🧸 Das unheimliche Kinderzimmer")
    st.write("Überall liegen alte Puppen und Bauklötze. Eine Puppe blinzelt dich an...")
    riesen_emoji("🧸🚂")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔙 Zurück ins Schlafzimmer"):
            set_level('bedroom')
        if st.button("🚂 Mit der Eisenbahn spielen (Poldi kommt)"):
            set_level('poldi_trap')
    with col2:
        if st.button("📦 In die Spielzeugkiste klettern"):
            st.success("Die Kiste hat keinen Boden! Du rutschst in einen Tunnel...")
            time.sleep(1.5)
            set_level('library')

# --- LEVEL: DACHBODEN ---
elif st.session_state.level == 'attic':
    st.header("🕸️ Der staubige Dachboden")
    st.write("Hier oben ist es dunkel und voller Spinnweben. Alte Kisten stehen herum.")
    riesen_emoji("🕷️📦")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🪜 Leiter runter (Flur)"):
            set_level('level2')
    with col2:
        if st.button("🛝 Rutsche in den Garten"):
            set_level('garden')

# --- LEVEL: KÜCHE ---
elif st.session_state.level == 'kitchen':
    st.header("🍽️ Die Küche")
    st.write("Es duftet herrlich, aber es ist niemand hier.")
    
    if "🎂 Leckerer Kuchen" not in st.session_state.inventory:
        riesen_emoji("🎂")
        if st.button("Kuchen einstecken"):
            st.session_state.inventory.append("🎂 Leckerer Kuchen")
            st.success("Du hast den Kuchen eingesteckt!")
            time.sleep(1)
            st.rerun()
    else:
        riesen_emoji("🍽️")
        st.write("Die Küche ist leer. Den Kuchen hast du schon.")
        
    st.write("**Deine Optionen:**")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➡️ Zum Wohnzimmer gehen"):
            set_level('living_room')
    with col2:
        if st.button("▼ In den Keller absteigen"):
            set_level('cellar')

# --- LEVEL WOHNZIMMER ---
elif st.session_state.level == 'living_room':
    st.header("🛋️ Das Wohnzimmer")
    st.write("Ein gemütliches Sofa steht hier. Aber du hörst ein schweres Atmen aus dem nächsten Raum...")
    riesen_emoji("🛋️")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Zur Küche"):
            set_level('kitchen')
        if st.button("🚪 Zum Monster"):
            set_level('monster')
    with col2:
        if st.button("📚 Alte Holztür öffnen"):
            set_level('library')
        if st.button("▼ Keller-Luke öffnen"):
            set_level('cellar')

# --- LEVEL: BIBLIOTHEK ---
elif st.session_state.level == 'library':
    st.header("📚 Die Bibliothek")
    st.write("Tausende von Büchern! Jasper scheint diesen Ort zu mögen.")
    riesen_emoji("📚🕯️")
    
    st.info("Ein Buch im Regal sieht locker aus...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔙 Zurück ins Wohnzimmer"):
            set_level('living_room')
    with col2:
        if st.button("📖 Am Buch ziehen (Geheimgang)"):
            st.success("Die Wand dreht sich! Ein Geheimgang zur Küche!")
            time.sleep(1.5)
            set_level('kitchen')

# --- LEVEL GARTEN ---
elif st.session_state.level == 'garden':
    st.header("🌳 Der neblige Garten")
    st.write("Draußen ist es kalt und neblig. Hinter einem Busch leuchten zwei Augen...")
    riesen_emoji("🌳🌫️")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔎 Hinter den Busch schauen"):
            set_level('poldi_trap')
        if st.button("▼ In das Erdloch (Keller)"):
            set_level('cellar')
    with col2:
        if st.button("🪜 Ins Baumhaus klettern"):
            set_level('treehouse')

# --- LEVEL: BAUMHAUS ---
elif st.session_state.level == 'treehouse':
    st.header("🏡 Das Baumhaus")
    st.write("Hier oben bist du sicher vor dem Nebel. Was für eine Aussicht!")
    riesen_emoji("🔭🏡")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🪜 Runterklettern"):
            set_level('garden')
    with col2:
        if st.button("🪢 Seilbahn ins Wohnzimmer"):
            set_level('living_room')

# --- LEVEL 3: MONSTER BEGEGNUNG ---
elif st.session_state.level == 'monster':
    riesen_emoji("👹🍪")
    
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
    riesen_emoji("🐉🔥")
    st.error("Du bist Poldi in die Arme gelaufen!")
    st.write("'Ich will dir fressen!'")
    
    if st.button("🏃 Versuch in den Keller zu entkommen!"):
        set_level('cellar')
    
    if st.button("Aufgeben (Neustart)"):
        st.session_state.inventory = [] 
        set_level('start')

# --- LEVEL KELLER ---
elif st.session_state.level == 'cellar':
    st.header("🕸️ Der dunkle Keller")
    st.write("Du bist im Keller gelandet. Es ist dunkel, aber du siehst zwei Tunnel.")
    riesen_emoji("🔦")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("Linker Tunnel")
        # Hier geht es jetzt zu Bert & Ernie statt direkt ins Gefängnis
        if st.button("👈 Nach Links gehen"):
            set_level('dungeon')
            
    with col2:
        st.success("Rechter Tunnel")
        if st.button("👉 Nach Rechts gehen"):
            set_level('treasure')

# --- NEU: BERT & ERNIE IM VERLIES ---
elif st.session_state.level == 'dungeon':
    st.header("⛓️ Das Verlies")
    st.write("Du siehst zwei bekannte Gesichter hinter Gittern...")
    riesen_emoji("😠🦜") # Bert und Ernie (symbolisch)
    st.write("**Bert:** 'Ernie hat den Drachen geärgert!'")
    st.write("**Ernie:** 'Ich wollte nur spielen! Hilf uns!'")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔓 Beide befreien"):
            set_level('win_friends')
    with col2:
        if st.button("🤷 Weitergehen (Ignorieren)"):
            set_level('prison')

# --- NEU: GEWONNEN MIT FREUNDEN ---
elif st.session_state.level == 'win_friends':
    st.balloons()
    st.header("🎉 FREUNDE GERETTET!")
    riesen_emoji("👯‍♂️🚪")
    st.success("Du hast Bert und Ernie befreit!")
    st.write("Ernie quietscht so laut mit seinem Quietscheentchen, dass Poldi erschreckt wegrennt.")
    st.write("Ihr entkommt zusammen durch einen geheimen Lüftungsschacht.")
    
    if st.button("Neues Abenteuer starten"):
        st.session_state.inventory = []
        set_level('start')

# --- LEVEL GEFÄNGNIS (GAME OVER MIT POLDI) ---
elif st.session_state.level == 'prison':
    st.header("⛓️ GEFÄNGNIS... UND POLDI!")
    riesen_emoji("⛓️🐉") 
    st.error("Sackgasse! Poldi hat hier auf dich gewartet.")
    st.subheader("'Ich will dir fressen!'")
    
    if st.button("Neues Abenteuer starten"):
        st.session_state.inventory = []
        set_level('start')

# --- NEU: LEVEL SCHATZKAMMER (WIN) ---
elif st.session_state.level == 'treasure':
    st.balloons()
    st.header("💎 SCHATZKAMMER!")
    riesen_emoji("💎💰")
    st.success("Du hast den geheimen Ausgang gefunden!")
    st.write("Hier liegt ein riesiger Haufen Goldkekse. Du bist reich!")
    
    if st.button("Reich und glücklich neustarten"):
        st.session_state.inventory = []
        set_level('start')

# --- ENDE: GEWONNEN (MONSTER) ---
elif st.session_state.level == 'win':
    st.balloons()
    st.header("🎉 GEWONNEN!")
    riesen_emoji("💖🎉")
    st.success("Das Monster liebt Kuchen!")
    st.write("Es mampft glücklich vor sich hin und lässt dich frei.")
    
    if st.button("Neues Abenteuer starten"):
        st.session_state.inventory = []
        set_level('start')

# --- ENDE: GEFRESSEN ---
elif st.session_state.level == 'game_over_monster':
    st.header("💀 GAME OVER")
    riesen_emoji("💀🍪")
    st.error("Das Monster hat dich gefressen!")
    
    if st.button("Nochmal versuchen"):
        st.session_state.inventory = []
        set_level('start')
