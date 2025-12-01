# Du brauchst dafür keinen Installations-Aufwand.
# Man kann das z.B. auf share.streamlit.io hochladen.

import streamlit as st
import time

st.title("🍪 Das Krümelmonster Abenteuer")

# Wir müssen den Zustand (wo bin ich?) speichern
if 'level' not in st.session_state:
    st.session_state.level = 'start'

def set_level(neues_level):
    st.session_state.level = neues_level

# --- LEVEL 1: VOR DEM HAUS ---
if st.session_state.level == 'start':
    st.write("Du stehst vor einem Haus. 3 Türen liegen vor dir.")
    
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
    st.write("Du bist drinnen! Die Türen haben sich verändert...")
    
    if st.session_state.vorgabe == "gruen":
        farben = ["🟢", "🟢", "🟢"]
    else:
        farben = ["🔴", "🔴", "🟢"]
        
    if st.button(f"Tür 1 {farben[0]}"): set_level('monster')
    if st.button(f"Tür 2 {farben[1]}"): set_level('monster')
    if st.button(f"Tür 3 {farben[2]}"): set_level('monster')

# --- LEVEL 3: MONSTER ---
elif st.session_state.level == 'monster':
    st.image("https://upload.wikimedia.org/wikipedia/en/6/62/Kermit_the_Frog.jpg", caption="(Stell dir hier das Krümelmonster vor)")
    st.header("KRÜMELMONSTER!")
    st.write("Willst du mir Kekse geben?")
    
    antwort = st.text_input("Deine Antwort:")
    
    if st.button("Antworten"):
        if antwort.lower().strip() == "kuchen":
            st.success("GEWONNEN! Kuchen ist super!")
        elif antwort.lower().strip() == "ja":
            st.error("Verloren! Es frisst die Kekse und DICH!")
        else:
            st.warning("Poldi kommt und frisst dich!")

    if st.button("Neustart"):
        set_level('start')
