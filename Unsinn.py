import streamlit as st
import random
import time

# Konfiguration der Seite
st.set_page_config(
    page_title="Unsinn-Radar 3000 Pro Max",
    page_icon="🚨",
    layout="centered"
)

# --- FUNKTION: KAUDERWELSCH ÜBERSETZER ---
def mach_kauderwelsch(text):
    woerter = text.split()
    if not woerter:
        return "Nichts da zum Verwursten!"
    
    lustige_einschuebe = ["Schnitzel", "Pups", "Blubb", "Knödel", "Glitzer", "Moppelkotze", "Hmpf"]
    neuer_text = []
    
    for wort in woerter:
        # Wahrscheinlichkeit erhöht, damit man den Effekt besser sieht
        if random.random() < 0.35:
            neuer_text.append(random.choice(lustige_einschuebe))
        elif len(wort) > 3 and random.random() < 0.35:
            mitte = list(wort[1:-1])
            random.shuffle(mitte)
            vermixt = wort[0] + "".join(mitte) + wort[-1]
            neuer_text.append(vermixt)
        else:
            neuer_text.append(wort)
            
    return " ".join(neuer_text)

# --- STATE INITIALISIERUNG ---
if "text_inhalt" not in st.session_state:
    st.session_state.text_inhalt = ""
# NEU: Variablen für den Test
if "test_status" not in st.session_state:
    st.session_state.test_status = "inactive" # inactive, running, finished
if "frage_index" not in st.session_state:
    st.session_state.frage_index = 0
if "test_score" not in st.session_state:
    st.session_state.test_score = 0

# --- FRAGENKATALOG ---
unsinn_fragen = [
    "Ist der Mond eigentlich aus grünem Käse?",
    "Kann man mit Spaghetti telefonieren?",
    "Ist es Nachts kälter als draußen?",
    "Haben Pinguine Knie?",
    "Teleportieren deine Socken in der Waschmaschine?",
    "Gibt es Bielefeld wirklich?",
    "Schmeckt die Farbe Blau nach Blaubeeren?",
    "Sind Einhörner nur Pferde mit Partyhütchen?",
    "Kann man Zeit in Marmeladengläsern speichern?",
    "Bin ich eigentlich ein hochentwickelter Toaster?"
]

# --- SEITENLEISTE ---
with st.sidebar:
    st.image("https://media.giphy.com/media/QvBoMEcQ7DQXK/giphy.gif", caption="Scanner aktiv")
    st.header("⚙️ Einstellungen")
    strenge = st.slider("Empfindlichkeit", 0, 100, 50)
    turbo_boost = st.checkbox("🚀 Turbo-Boost aktivieren")
    ki_modus = st.checkbox("🤖 KI-Analyse aktivieren", value=True)
    sound_modus = st.checkbox("🔊 Sound-Effekte (Visuell)", value=True)
    experten_modus = st.checkbox("Wissenschaftliche Analyse anzeigen")
    
    st.markdown("---")
    # NEU: Knopf zum Starten des Tests in der Sidebar
    if st.button("🧠 Großen Unsinn-Test starten"):
        st.session_state.test_status = "running"
        st.session_state.frage_index = 0
        st.session_state.test_score = 0
        st.rerun() # Aktualisiert auf st.rerun()

    st.markdown("---")
    st.info("Version 5.2.1 - Bugfix Edition.")

# --- HAUPTBEREICH ---
st.title("🚨 Der Unsinn-Radar 3000 Pro Max")

# --- LOGIK: ENTWEDER TEST ODER SCANNER ANZEIGEN ---

if st.session_state.test_status == "running":
    # === HIER LÄUFT DER TEST ===
    st.subheader("📝 Der offizielle Unsinn-Persönlichkeitstest")
    
    # Fortschrittsbalken
    fortschritt = (st.session_state.frage_index / len(unsinn_fragen))
    st.progress(fortschritt)
    st.caption(f"Frage {st.session_state.frage_index + 1} von {len(unsinn_fragen)}")
    
    # Die aktuelle Frage
    aktuelle_frage = unsinn_fragen[st.session_state.frage_index]
    st.markdown(f"### {aktuelle_frage}")
    
    col1, col2 = st.columns(2)
    
    # Funktion für Antwort-Klick
    def antwort(ja):
        if ja:
            st.session_state.test_score += 10 # Ja gibt Punkte für "Unsinn-Glaube"
        else:
            st.session_state.test_score += 2 # Nein ist langweilig
            
        st.session_state.frage_index += 1
        if st.session_state.frage_index >= len(unsinn_fragen):
            st.session_state.test_status = "finished"
    
    with col1:
        st.button("✅ Ja, klar!", use_container_width=True, on_click=antwort, args=(True,))
    with col2:
        st.button("❌ Quatsch!", use_container_width=True, on_click=antwort, args=(False,))

elif st.session_state.test_status == "finished":
    # === TEST ERGEBNIS ===
    st.subheader("🎓 Dein Testergebnis")
    score = st.session_state.test_score
    st.write(f"Du hast **{score} von 100** möglichen Unsinn-Punkten erreicht.")
    
    if score > 80:
        st.success("🏆 Du bist ein absoluter **UNSINN-PROFI**! Dein Gehirn besteht zu 90% aus Knete.")
        st.balloons()
    elif score > 40:
        st.info("🤪 Du bist ein **Quatschkopf-Lehrling**. Da geht noch mehr!")
    else:
        st.warning("😐 Du bist sehr **seriös**. Langweilig!")
        
    if st.button("Zurück zum Radar"):
        st.session_state.test_status = "inactive"
        st.rerun() # Aktualisiert auf st.rerun()

else:
    # === NORMALER SCANNER MODUS ===
    st.image("https://media.giphy.com/media/l0HlJ7aAQyvjxM6B2/giphy.gif", use_column_width=True)
    st.write("Dieses Hochtechnologie-Gerät prüft wissenschaftlich genau, ob dein Text schlau ist oder totaler Quatsch.")

    # 1. Die handgeschriebenen "Premium"-Sätze
    premium_quatsch = [
        "Nachts ist es kälter als draußen, weil die Häuser im Freien stehen.",
        "Mein Goldfisch spielt Klavier, aber nur unter Wasser.",
        "Wenn Fliegen hinter Fliegen fliegen, fliegen Fliegen Fliegen nach.",
        "Bananen sind krumm, weil niemand in den Urwald zog und die Banane gerade bog.",
        "Ich habe meinen Joghurt fallen lassen, jetzt ist er müde.",
        "Mein Luftkissenfahrzeug ist voller Aale.",
        "Die Katze tritt auf die Treppe, die Treppe wird krumm.",
        "Grüße an die Füße, die Hände waschen sich von allein.",
        "Draußen ist es dunkel, deshalb leuchtet mein Käsebrot.",
        "Wer anderen eine Grube gräbt, hat ein Grubengrabgerät.",
        "Cola schmeckt besser als aus dem Glas.",
        "Zu Fuß ist es kürzer als über den Berg.",
        "Der Mond ist eigentlich ein Pfannkuchen, der zu lange in der Pfanne lag.",
        "Ich bin nicht faul, ich bin im Energiesparmodus.",
        "Einhörner sind auch nur Pferde mit Partyhütchen.",
        "Wenn man im Kreis läuft, spart man sich den Rückweg.",
        "Schokolade ist Gottes Entschuldigung für Brokkoli.",
        "Ich spreche fließend Ironisch, und das sogar mit Akzent.",
        "Gestern war heute noch morgen.",
        "Fische sind Freunde, kein Futter (außer Thunfisch).",
        "Warum liegt hier eigentlich Stroh?",
        "Mein Staubsauger hat eine Stauballergie entwickelt.",
        "Kuchenkrümel sind nur Kekse, die das Leben aufgegeben haben.",
        "Nasse Pinguine rutschen schneller als trockene Steine.",
        "Der frühe Vogel kann mich mal.",
        "Das Licht am Ende des Tunnels ist ein entgegenkommender Zug.",
        "Ich bin nicht dick, ich bin flauschig.",
        "Realität ist was für Leute, die mit Drogen nicht klarkommen.",
        "Ich habe keine Macken, das sind Special Effects.",
        "Mein Einhorn pupst Glitzer.",
        "Aliens haben meine Hausaufgaben gefressen.",
        "Die Pizza war zu heiß, jetzt habe ich keine Fingerabdrücke mehr.",
        "Ich bin so satt, ich mag kein Blatt.",
        "Das Runde muss ins Eckige, sagte das Dreieck.",
        "Nachts feiern die Ratten Party im Keller.",
        "Der Mond ist aus Käse, ich war da.",
        "Sterne sind nur Löcher im Himmelszelt.",
        "Wolken sind die Gedanken des Himmels.",
        "Wenn ich groß bin, werde ich eine Feuerwehr.",
        "Mein Auto fährt auch ohne Benzin, aber nur bergab.",
        "Ich habe den Schlüssel zum Erfolg verloren.",
        "Wer das liest, kann lesen.",
        "Optimismus ist nur ein Mangel an Informationen.",
        "Ich bin nicht schizophren, ich bin auch nicht.",
        "Stimmen im Kopf sind okay, solange sie Miete zahlen.",
        "Faulheit ist die Kunst, sich auszuruhen, bevor man müde wird.",
        "Ordnung ist das halbe Leben, ich lebe in der anderen Hälfte.",
        "Chaos ist nur eine Ordnung, die man nicht versteht.",
        "Ich bin nicht unordentlich, ich bin kreativ.",
        "Mein Zimmer ist nicht unaufgeräumt, das ist ein Hindernisparcours.",
        "Ich bin wach, mehr darfst du nicht erwarten.",
        "Kaffee ist nur Wasser mit Stressgeschmack.",
        "Montage sind des Teufels.",
        "Döner macht schöner.",
        "Currywurst ist ein Grundnahrungsmittel.",
        "Wasser ist nass, aber Feuer ist nicht trocken.",
        "Wenn Tomaten Beeren sind, ist Ketchup dann Marmelade?",
        "Ich habe das Internet gelöscht, sorry.",
        "Der Boden ist Lava, aber die Lava ist kalt.",
        "Schlafen ist wie Blinzeln, nur sehr lange.",
        "Meine Socken fressen die Waschmaschine.",
        "Zeit ist Geld, aber Geld hat keine Uhr.",
        "Warum ist der Himmel blau und nicht gepunktet?",
        "Elefanten verstecken sich in Kirschbäumen, deshalb sieht man sie nie.",
        "Kekse sind gebackenes Glück.",
        "Ich atme in 4K Auflösung.",
        "Mein WLAN-Kabel ist verknotet.",
        "Viereckige Kreise sind die besten Dreiecke.",
        "Der Kühlschrank ist das Fernsehen für Essen.",
        "Spaghetti wachsen auf Bäumen, das weiß doch jeder.",
        "Ich habe die Unendlichkeit gezählt, zweimal.",
        "Tomaten werden rot, weil sie die Luft anhalten.",
        "Gras ist eigentlich nur grünes Haar der Erde.",
        "Vögel sind Überwachungskameras der Regierung.",
        "Ich habe versucht, Wasser zu verbrennen.",
        "Mein Gehirn hat heute Ruhetag.",
        "Die Realität ist nur eine Simulation mit schlechter Grafik.",
        "Schwerkraft ist nur eine Theorie, ich fliege gleich weg.",
        "Dinosaurier haben sich nur gut versteckt.",
        "Mein Kaktus braucht eine Umarmung.",
        "Regenbögen sind die Rutschen der Einhörner.",
        "Schnee ist nur gefrorenes Wolkenpipi.",
        "Wenn man die Augen zumacht, sieht man nichts.",
        "Mein linker Fuß ist rechts von meinem rechten Fuß.",
        "Spiegel sind Portale in eine Welt, wo alles falsch herum ist.",
        "Ich spreche fließend Klingonisch.",
        "Warum ist 'Abkürzung' so ein langes Wort?",
        "Stille Wasser sind tief, aber dreckig.",
        "Hochmut kommt vor dem Fallschirm.",
        "Morgenstund hat Gold im Mund, aber Blei im Hintern.",
        "Das Leben ist kein Ponyhof, sondern eine Achterbahn ohne Bügel.",
        "Ich habe Lag im Reallife.",
        "Mein Ping ist zu hoch für Hausaufgaben.",
        "AFK, Leben genießen.",
        "Die Antwort auf alles ist 42.",
        "Wer A sagt, muss nicht B sagen. Er kann auch erkennen, dass A falsch war.",
        "Lächeln ist die schönste Art, Zähne zu zeigen.",
        "Ich kam, sah und vergaß, was ich wollte.",
        "Räume auf, bevor das Chaos dich aufräumt.",
        "Schokolade fragt nicht, Schokolade versteht.",
        "Ein Tag ohne Lachen ist ein verlorener Tag, aber ein Tag ohne Handy ist die Hölle."
    ]

    # Generator für Sätze
    subjekte = ["Ein Toaster", "Mein Hamster", "Der Bundeskanzler", "Ein Zombie", "Das Internet", "Eine Kartoffel", "Mein linker Schuh", "Der Mond", "Ein Keks", "Die Katze"]
    verben = ["heiratet", "verklagt", "verspeist", "ignoriert", "baut", "zerstört", "streichelt", "beleidigt", "analysiert", "bemalt"]
    objekte = ["eine Banane", "die Relativitätstheorie", "einen Regenbogen", "meine Hausaufgaben", "den Sinn des Lebens", "eine Atombombe", "einen Gummistiefel"]
    endungen = ["im Weltraum.", "unter Wasser.", "mit Senf.", "gestern.", "aus Versehen.", "mit Absicht.", "während der Apokalypse."]

    generierte_liste = []
    for s in subjekte:
        for v in verben:
            for o in objekte:
                for e in endungen:
                    satz = f"{s} {v} {o} {e}"
                    generierte_liste.append(satz)
    
    random.shuffle(generierte_liste)
    quatsch_beispiele = premium_quatsch + generierte_liste
    quatsch_beispiele = quatsch_beispiele[:1001]

    if st.button("📅 Unsinn des Tages anzeigen"):
        tages_unsinn = random.choice(quatsch_beispiele)
        st.success(f"### 🌟 Weisheit des Tages:\n\n> *{tages_unsinn}*")
        st.balloons()

    def vorschlag_generieren():
        st.session_state.text_inhalt = random.choice(quatsch_beispiele)

    st.button(f"🎲 Mir fällt nichts ein - Schreib du mal Unsinn! (1 aus {len(quatsch_beispiele)})", on_click=vorschlag_generieren)
    user_text = st.text_area("Gib hier deinen Satz oder eine Geschichte ein:", key="text_inhalt", height=150)

    if st.button("🔀 In Kauderwelsch übersetzen"):
        if user_text.strip() == "":
            st.warning("Schreib erst was, du Experte!")
        else:
            unsinn_text = mach_kauderwelsch(user_text)
            st.session_state.text_inhalt = unsinn_text
            st.rerun() # Aktualisiert auf st.rerun()

    lustige_gruende = [
        "Zu viele Vokale an der falschen Stelle.", "Der Text riecht ein bisschen nach Käse.",
        "Die Logik hat gerade Urlaub genommen.", "Klingt verdächtig nach einem Alien.",
        "Grammatik wurde nicht gefunden.", "Dieser Satz dreht sich im Kreis.",
        "Enthält Spuren von Wahnsinn.", "Mein Hamster tippt sinnvoller."
    ]

    def ki_analyse(text):
        woerter = text.split()
        if len(woerter) > 0: wort = random.choice(woerter)
        else: wort = "Nichts"
        ki_saetze = [
            f"Meine neuronalen Netze vibrieren bei dem Wort '{wort}'.",
            f"Ich habe '{wort}' durch den Quantenbeschleuniger gejagt. Ergebnis: Lila.",
            f"Die emotionale Dichte von '{wort}' beträgt 42.7 Mega-Lappen."
        ]
        return random.choice(ki_saetze)

    if st.button("Auf Unsinn scannen"):
        if user_text.strip() == "":
            st.warning("Du musst erst etwas schreiben, sonst kann ich nichts scannen!")
        else:
            progress_text = "Kalibriere Quatsch-Sensoren..."
            my_bar = st.progress(0, text=progress_text)
            if sound_modus: st.toast("🔊 *Trommelwirbel...*")

            for percent_complete in range(100):
                time.sleep(0.005) 
                if percent_complete == 40: progress_text = "Berechne Sinnlosigkeit..."
                my_bar.progress(percent_complete + 1, text=progress_text)
            my_bar.empty()

            zufall = random.randint(0, 100)
            unsinn_level = int((zufall + strenge) / 2)
            if turbo_boost: unsinn_level = unsinn_level * random.randint(2, 10)
            
            st.markdown("---")
            col1, col2 = st.columns([1, 2])
            with col1:
                st.metric(label="Unsinn-Level", value=f"{unsinn_level}%")
            
            with col2:
                if unsinn_level < 50:
                    st.info("🤔 Ein bisschen Quatsch ist dabei, aber okay.")
                    st.image("https://media.giphy.com/media/xT5LMzIK1AdZJ4cYW4/giphy.gif")
                elif unsinn_level <= 100:
                    st.error("🚨 ALARM! TOTALER BLÖDSINN ERKANNT! 🤯")
                    st.image("https://media.giphy.com/media/10JhviFuU2gWD6/giphy.gif")
                else:
                    st.error("🌌 KOSMISCHER BLÖDSINN!")
                    st.balloons()
                    st.snow()
                    st.image("https://media.giphy.com/media/P7JmDW7IkB7TW/giphy.gif")

            if unsinn_level > 100:
                st.markdown(f"""<div style="border: 5px double gold; padding: 20px; text-align: center; background-color: #fff8dc; color: black; border-radius: 10px;"><h1>🎓 U R K U N D E 🎓</h1><p>Hiermit wird bestätigt: Das ist</p><h2 style="color: red;">TOTALER QUATSCH</h2></div>""", unsafe_allow_html=True)

            if ki_modus:
                st.markdown("---")
                with st.spinner("Verbinde mit dem Mutterschiff..."):
                    time.sleep(1.0)
                    st.info(f"💡 **KI-Erkenntnis:** {ki_analyse(user_text)}")

            if experten_modus:
                st.markdown("---")
                st.subheader("🔬 Analyse:")
                st.write(f"❌ {random.choice(lustige_gruende)}")

st.markdown("---")
st.caption("Der Unsinn-Radar 3000 Pro Max. Du Lappen.")
