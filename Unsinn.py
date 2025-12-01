import streamlit as st
import random
import time

# Konfiguration der Seite
st.set_page_config(
    page_title="Unsinn-Radar 3000 Pro Max",
    page_icon="🚨",
    layout="centered"
)

# --- SEITENLEISTE (EINSTELLUNGEN) ---
with st.sidebar:
    # NEU: Ein Roboter GIF in der Seitenleiste
    st.image("https://media.giphy.com/media/26AHvvC1c7aR9tQ8U/giphy.gif", caption="Scanner aktiv")
    
    st.header("⚙️ Einstellungen")
    st.write("Konfiguriere den Scanner:")
    
    # Ein Schieberegler für die "Strenge"
    strenge = st.slider("Empfindlichkeit", 0, 100, 50)
    st.caption("0 = Alles ist sinnvoll | 100 = Alles ist Quatsch")
    
    # NEU: Turbo-Boost für 1000%
    turbo_boost = st.checkbox("🚀 Turbo-Boost aktivieren (bis 1000%)")
    
    # Checkbox für Experten-Modus
    experten_modus = st.checkbox("Wissenschaftliche Analyse anzeigen")
    
    st.markdown("---")
    st.info("Version 4.0 - Die 'Grafik-Update' Edition.")

# --- HAUPTBEREICH ---
st.title("🚨 Der Unsinn-Radar 3000 Pro Max")
# NEU: Großes Radar-Bild oben
st.image("https://media.giphy.com/media/3o7qE1YN7aQf3olljG/giphy.gif", use_column_width=True)
st.write("Dieses Hochtechnologie-Gerät prüft wissenschaftlich genau, ob dein Text schlau ist oder totaler Quatsch.")

# --- GENERATOR FÜR 1001 SÄTZE ---
# Wir nutzen session_state, um den Text im Feld zu speichern
if "text_inhalt" not in st.session_state:
    st.session_state.text_inhalt = ""

# 1. Die handgeschriebenen "Premium"-Sätze (die besten ~100)
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

# 2. Der Generator für Tausende von Kombinationen
subjekte = [
    "Ein Toaster", "Mein Hamster", "Der Bundeskanzler", "Ein Zombie", "Das Internet", 
    "Eine Kartoffel", "Mein linker Schuh", "Der Mond", "Ein Keks", "Die Katze", 
    "Ein Einhorn", "Mein WLAN", "Der Kühlschrank", "Ein Ninja", "Das Universum",
    "Ein Clown", "Der Mülleimer", "Eine Socke", "Der Busfahrer", "Ein Pinguin"
]
verben = [
    "heiratet", "verklagt", "verspeist", "ignoriert", "baut", "zerstört", "streichelt", 
    "beleidigt", "analysiert", "bemalt", "versteckt", "liebt", "fürchtet", "reitet auf", 
    "teleportiert", "diskutiert mit", "tanzt mit", "verkauft", "hypnotisiert", "sucht"
]
objekte = [
    "eine Banane", "die Relativitätstheorie", "einen Regenbogen", "meine Hausaufgaben", 
    "den Sinn des Lebens", "eine Atombombe", "einen Gummistiefel", "das Internet", 
    "eine Zeitmaschine", "den Weihnachtsmann", "einen Kaktus", "die Schwerkraft", 
    "ein schwarzes Loch", "die Matrix", "einen Drachen", "einen Löffel", "die Zukunft",
    "einen Goldfisch", "ein Ufo", "den Nachbarn"
]
endungen = [
    "im Weltraum.", "unter Wasser.", "mit Senf.", "gestern.", "aus Versehen.", 
    "mit Absicht.", "während der Apokalypse.", "in 4K Auflösung.", "ohne Hose.", 
    "rückwärts.", "im Dunkeln.", "auf dem Mars.", "mit viel Glitzer.", "ganz leise.", 
    "im Handstand.", "für 5 Euro.", "im Paralleluniversum.", "voller Panik.", 
    "mit Käse überbacken.", "im Livestream."
]

# Wir generieren Kombinationen, bis wir genug haben
generierte_liste = []
for s in subjekte:
    for v in verben:
        for o in objekte:
            for e in endungen:
                # Einen Satz bauen
                satz = f"{s} {v} {o} {e}"
                generierte_liste.append(satz)

# Mischen für Abwechslung
random.shuffle(generierte_liste)

# Die Liste zusammenbauen: Premium Sätze + so viele generierte wie nötig
# Wir schneiden bei 1001 ab
quatsch_beispiele = premium_quatsch + generierte_liste
quatsch_beispiele = quatsch_beispiele[:1001]

# --- NEU: UNSINN DES TAGES BUTTON ---
if st.button("📅 Unsinn des Tages anzeigen"):
    tages_unsinn = random.choice(quatsch_beispiele)
    st.success(f"### 🌟 Weisheit des Tages:\n\n> *{tages_unsinn}*")
    st.balloons()

def vorschlag_generieren():
    st.session_state.text_inhalt = random.choice(quatsch_beispiele)

# Der Knopf für Vorschläge
st.button(f"🎲 Mir fällt nichts ein - Schreib du mal Unsinn! (1 aus {len(quatsch_beispiele)})", on_click=vorschlag_generieren)

# Eingabefeld (verknüpft mit session_state)
user_text = st.text_area("Gib hier deinen Satz oder eine Geschichte ein:", key="text_inhalt", height=150)

# Liste mit lustigen "Gründen" für die Analyse (Massiv erweitert)
lustige_gruende = [
    "Zu viele Vokale an der falschen Stelle.",
    "Der Text riecht ein bisschen nach Käse.",
    "Die Logik hat gerade Urlaub genommen.",
    "Klingt verdächtig nach einem Alien.",
    "Grammatik wurde nicht gefunden.",
    "Dieser Satz dreht sich im Kreis.",
    "Enthält Spuren von Wahnsinn.",
    "Mein Hamster tippt sinnvoller.",
    "Gefahr von Gehirnknoten erkannt!",
    "Der Sinn hat sich unter dem Sofa versteckt.",
    "Zu wenig Glitzer im Satzbau.",
    "Das Verb hat Angst vor dem Subjekt.",
    "Klingt wie rückwärts gesungen.",
    "Ein Fall für das Galileo Mystery Team.",
    "Error 404: Bedeutung not found.",
    "Die Buchstaben tanzen Polka.",
    "Das würde selbst ein Toaster nicht verstehen.",
    "Verdacht auf Tastatur-Rollen mit dem Gesicht.",
    "Interpunktion ist wohl Glückssache.",
    "Klingt nach einem schlechten Rap-Text.",
    "Sogar Siri ist verwirrt.",
    "Der Text besteht zu 90% aus heißer Luft.",
    "Physikalisch unmöglich.",
    "Das verletzt die Gesetze der Thermodynamik."
]

if st.button("Auf Unsinn scannen"):
    if user_text.strip() == "":
        st.warning("Du musst erst etwas schreiben, sonst kann ich nichts scannen!")
    else:
        # 1. Ladebalken Animation
        progress_text = "Kalibriere Quatsch-Sensoren..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.005) # Schnellerer Scan für Profis
            # Text im Ladebalken ändern
            if percent_complete == 20: progress_text = "Analysiere Buchstaben..."
            if percent_complete == 40: progress_text = "Berechne Sinnlosigkeit..."
            if percent_complete == 60: progress_text = "Frage das Orakel..."
            if percent_complete == 80: progress_text = "Lade Blödsinn hoch..."
            my_bar.progress(percent_complete + 1, text=progress_text)
        
        my_bar.empty() # Balken ausblenden, wenn fertig

        # 2. Unsinn-Wert berechnen
        zufall = random.randint(0, 100)
        unsinn_level = int((zufall + strenge) / 2)
        
        # TURBO BOOST LOGIK
        if turbo_boost:
            multiplikator = random.randint(2, 10) # Mal 2 bis Mal 10
            unsinn_level = unsinn_level * multiplikator
            
        # 3. Ergebnis anzeigen
        st.markdown("---")
        
        # Große Zahl anzeigen
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(label="Unsinn-Level", value=f"{unsinn_level}%")
        
        with col2:
            if unsinn_level < 20:
                st.success("✅ Dieser Text ergibt absolut Sinn! (Langweilig...)")
                # NEU: Smart Guy Meme
                st.image("https://media.giphy.com/media/d3mlE7uhX8KFgEmY/giphy.gif") 
            elif unsinn_level < 50:
                st.info("🤔 Ein bisschen Quatsch ist dabei, aber okay.")
                # NEU: Thinking GIF
                st.image("https://media.giphy.com/media/3o7TKSjRrfPHj32nWA/giphy.gif")
            elif unsinn_level < 80:
                st.warning("⚠️ Vorsicht! Der Unsinn-Pegel ist kritisch!")
                # NEU: Confused GIF
                st.image("https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif")
            elif unsinn_level <= 100:
                st.error("🚨 ALARM! TOTALER BLÖDSINN ERKANNT! 🤯")
                # NEU: Laughing Minions
                st.image("https://media.giphy.com/media/10JhviFuU2gWD6/giphy.gif")
            elif unsinn_level <= 500:
                st.error("🔥 EXTREMER UNSINN! Mein Prozessor schmilzt!")
                st.image("https://media.giphy.com/media/NTur7XlVDUdqM/giphy.gif", caption="This is fine.")
            else:
                st.error("🌌 KOSMISCHER BLÖDSINN! (Über 500%)")
                st.write("Wir haben die Grenze der Realität verlassen.")
                st.balloons()
                st.snow() # Schnee und Ballons gleichzeitig für das Chaos
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGZ4eXF4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4ZXZ4/l0HlCqV9bVuyyGuiA/giphy.gif", caption="System überlastet!")

        # 4. Experten-Analyse (nur wenn angehakt)
        if experten_modus:
            st.markdown("---")
            st.subheader("🔬 Wissenschaftliche Analyse:")
            # Wir wählen jetzt bis zu 5 zufällige Gründe aus der erweiterten Liste
            anzahl_gruende = random.randint(3, 5)
            gruende = random.sample(lustige_gruende, anzahl_gruende)
            
            for grund in gruende:
                st.write(f"❌ {grund}")

# Fußzeile (Der freche Endsatz)
st.markdown("---")
st.caption("Der Unsinn-Radar 3000 Pro Max. Du Lappen.")
