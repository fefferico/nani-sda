import streamlit as st

# Configurazione pagina
st.set_page_config(
    page_title="Le Razze Naniche - Il Signore degli Anelli",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizzato
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #D4AF37;
        text-align: center;
        text-shadow: 2px 2px 4px #000;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #C0C0C0;
        text-align: center;
        margin-bottom: 2rem;
    }
    .casata-card {
        background-color: #1E1E1E;
        border-radius: 10px;
        padding: 20px;
        border-left: 5px solid #D4AF37;
        margin-bottom: 15px;
    }
    .info-box {
        background-color: #2D2D2D;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Dati delle Sette Casate
CASATE = {
    "Durin (Longbeard)": {
        "nome_khuzdul": "Sigin-tarâg",
        "colore": "#D4AF37",
        "montagna": "Khazad-dûm (Moria), Erebor, Colline del Ferro",
        "descrizione": "La più antica e nobile delle casate, fondata da Durin il Senza-Morte, il primo Nano svegliato da Aulë. I Nani di Durin sono i più famosi della Terra di Mezzo.",
        "caratteristiche": ["Alta statura tra i Nani", "Barbe lunghe e intrecciate", "Grande abilità in architettura e metallurgia", "Leader naturali"],
        "personaggi_famosi": ["Durin I (il Senza-Morte)", "Durin II", "Durin III", "Durin VI", "Durin VII", "Thorin I", "Thorin II Scudodiquercia", "Thorin III Elmo di Pietra", "Balin", "Dwalin", "Glóin", "Gimli", "Dáin I", "Dáin II Piediferro"],
        "storia": "Fondarono Khazad-dûm, la più grande città nanica mai costruita. Dopo la caduta di Moria, molti si trasferirono in Erebor. Durin il Senza-Morte fu il primo dei Sette Padri dei Nani, svegliato da Aulë stesso sotto il Monte Gundabad."
    },
    "Firebeard": {
        "nome_khuzdul": "Narâg-zigil",
        "colore": "#FF4500",
        "montagna": "Monti Azzurri",
        "descrizione": "Una delle due casate che abitavano i Monti Azzurri. Conosciuti per la loro barba rossastra e il temperamento focoso.",
        "caratteristiche": ["Barbe color rame o rosso fuoco", "Temperamento passionale", "Maestri nella lavorazione del rame", "Guerrieri valorosi"],
        "personaggi_famosi": ["Personaggi meno noti, ma parteciparono alla Grande Guerra dei Nani e degli Orchi"],
        "storia": "Abitarono i Monti Azzurri insieme ai Broadbeam. Dopo la Grande Guerra, i Monti Azzurri furono perduti e i superstiti si unirono ai Longbeard a Khazad-dûm."
    },
    "Broadbeam": {
        "nome_khuzdul": "Tharkûn-baraz",
        "colore": "#8B4513",
        "montagna": "Monti Azzurri",
        "descrizione": "L'altra casata dei Monti Azzurri, nota per corporatura robusta e forza fisica eccezionale. Costruirono le grandi sale di Belegost e Nogrod.",
        "caratteristiche": ["Corporatura massiccia e larga", "Forza fisica superiore", "Maestri nella lavorazione della pietra", "Costruttori di grandi fortezze"],
        "personaggi_famosi": ["Azaghâl, Signore di Belegost (uccise Glaurung)", "Mîm il Nano (forse di questa stirpe)"],
        "storia": "Fondarono le città di Belegost e Nogrod. Azaghâl, loro signore, ferì mortalmente Glaurung, il primo dei draghi, durante la Battaglia delle Innumerevoli Lacrime. Dopo la caduta dei Monti Azzurri, molti si rifugiarono a Khazad-dûm."
    },
    "Ironfist": {
        "nome_khuzdul": "Baruk-khîm",
        "colore": "#708090",
        "montagna": "Montagne Grigie orientali",
        "descrizione": "Casata orientale, meno conosciuta nella Terra di Mezzo occidentale. Abitavano nelle Montagne Grigie lontane.",
        "caratteristiche": ["Pugni forti come il ferro", "Guerrieri corpo a corpo", "Abilità nella lavorazione del ferro grezzo", "Riservati e isolati"],
        "personaggi_famosi": ["Pochi nomi sopravvissuti nei racconti occidentali"],
        "storia": "Una delle casate che si allontanarono verso oriente dopo il risveglio. Le loro terre erano lontane dagli eventi principali della Terra di Mezzo."
    },
    "Stiffbeard": {
        "nome_khuzdul": "Thikul-baraz",
        "colore": "#4682B4",
        "montagna": "Montagne Fredde del Nord",
        "descrizione": "Casata settentrionale che abitava nelle terre fredde. Conosciuti per le barbe rigide e la resistenza al gelo.",
        "caratteristiche": ["Barbe dure come ghiaccio", "Resistenza estrema al freddo", "Abilità nella lavorazione del ghiaccio e cristallo", "Cacciatori esperti"],
        "personaggi_famosi": ["Raramente menzionati nelle cronache del Terzo Era"],
        "storia": "Vivevano nelle regioni settentrionali, lontane dalla civiltà degli Elfi e degli Uomini. Le loro terre erano prossime ai reami del gelo."
    },
    "Blacklock": {
        "nome_khuzdul": "Mornuil",
        "colore": "#2F2F2F",
        "montagna": "Montagne dell'Oriente",
        "descrizione": "Casata orientale, chiamata così per i loro capelli e barbe scurissimi, quasi neri. Abili minatori in profondità.",
        "caratteristiche": ["Capelli e barbe neri come la pece", "Minatori delle profondità", "Esperti in gemme nere e ossidiana", "Silenziosi e metodici"],
        "personaggi_famosi": ["Pochi riferimenti nei testi occidentali"],
        "storia": "Scavarono nelle profondità delle montagne orientali. Si dice fossero tra i più abili nel trovare gemme nascoste nelle vene più profonde della terra."
    },
    "Stonefoot": {
        "nome_khuzdul": "Sulûn-ghâr",
        "colore": "#696969",
        "montagna": "Montagne del Sud-Est",
        "descrizione": "L'ultima delle sette casate, stanziata nelle montagne a sud-est della Terra di Mezzo. Piedi duri come pietra.",
        "caratteristiche": ["Piedi callosi e duri come roccia", "Arrampicatori nati", "Resistenza alla fatica", "Legami con le montagne meridionali"],
        "personaggi_famosi": ["Quasi sconosciuti nelle cronache del Nord-ovest"],
        "storia": "Vivevano lontano dagli altri, nelle montagne del sud-est. Come le altre casate orientali, sono poco menzionati nelle storie della Terra di Mezzo occidentale."
    }
}

PERSONAGGI_DETTAGLI = {
    "Thorin II Scudodiquercia": {
        "casata": "Durin (Longbeard)",
        "ruolo": "Re sotto la Montagna",
        "descrizione": "Figlio di Thráin II e nipote di Thrór. Condusse la spedizione di Erebor per reclamare il regno e il tesoro dal drago Smaug.",
        "arma": "Orcrist, la Spada Tagliagoblin",
        "morte": "Cadde nella Battaglia delle Cinque Armate (2941 T.E.)",
        "citazione": "Se più di noi valorizzassimo cibo, gioia e canti sopra l'oro ammassato, il mondo sarebbe più lieto"
    },
    "Gimli": {
        "casata": "Durin (Longbeard)",
        "ruolo": "Membro della Compagnia dell'Anello",
        "descrizione": "Figlio di Glóin, rappresentante dei Nani nella Compagnia dell'Anello. Unico Nano a partecipare al Consiglio di Elrond.",
        "arma": "Ascia da battaglia, Ascia da lancio",
        "morte": "Partì per le Terre Immortali con Legolas nel 120 Q.E., unico Nano a ricevere questo onore",
        "citazione": "Nulla è più affilato della lingua di un Elfo"
    },
    "Balin": {
        "casata": "Durin (Longbeard)",
        "ruolo": "Signore di Moria",
        "descrizione": "Compagno fedele di Thorin nella spedizione di Erebor. In seguito tentò di riconquistare Moria, dove trovò la morte.",
        "arma": "Spada",
        "morte": "Ucciso da un Orco (o dal Balrog) a Moria nel 2994 T.E.",
        "citazione": "Balin, Signore di Moria"
    },
    "Dáin II Piediferro": {
        "casata": "Durin (Longbeard)",
        "ruolo": "Re sotto la Montagna",
        "descrizione": "Cugino di Thorin, divenne Re di Erebor dopo la morte di Thorin. Cadde difendendo Erebor durante la Guerra dell'Anello.",
        "arma": "Ascia rossa",
        "morte": "Cadde difendendo Erebor nel 3019 T.E.",
        "citazione": "Il mondo sta cambiando"
    },
    "Durin il Senza-Morte": {
        "casata": "Durin (Longbeard)",
        "ruolo": "Primo dei Sette Padri",
        "descrizione": "Il primo Nano creato da Aulë il Fabbro. Svegliato sotto il Monte Gundabad, fondò Khazad-dûm. Si crede che reincarni nei suoi discendenti.",
        "arma": "Ascia di Aulë",
        "morte": "Immortale nei ricordi; il suo corpo morì ma il suo spirito si dice reincarni",
        "citazione": "Padre di tutti i Nani"
    },
    "Azaghâl": {
        "casata": "Broadbeam",
        "ruolo": "Signore di Belegost",
        "descrizione": "Signore dei Broadbeam, ferì mortalmente Glaurung, il primo dei draghi, durante la Battaglia delle Innumerevoli Lacrime.",
        "arma": "Spada o ascia (non specificata)",
        "morte": "Cadde dopo aver ferito Glaurung",
        "citazione": "Il più grande eroe Nano nella guerra contro Morgoth"
    }
}

# HEADER
st.markdown('<div class="main-header">⛏️ Le Sette Casate dei Nani ⛏️</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Un viaggio nelle razze naniche create da J.R.R. Tolkien</div>', unsafe_allow_html=True)

st.divider()

# Sidebar per navigazione
st.sidebar.title("🧭 Navigazione")
pagina = st.sidebar.radio(
    "Seleziona sezione:",
    ["🏔️ Le Sette Casate", "👑 Personaggi Famosi", "📜 Storia e Cultura", "🔍 Quiz Nanico"]
)

# PAGINA 1: LE SETTE CASATE
if pagina == "🏔️ Le Sette Casate":
    st.header("Le Sette Casate dei Nani")
    st.write("""
    Secondo la mitologia di Tolkien, Aulë il Fabbro creò i Nani prima del risveglio degli Elfi. 
    Poiché non poteva dare loro vita indipendente, Eru Ilúvatar li adottò e li pose in sonno fino al loro risveglio.
    I Sette Padri dei Nani fondarono le Sette Casate, ognuna con le proprie caratteristiche e terre.
    """)
    
    # Selettore casata
    casata_scelta = st.selectbox(
        "Scegli una casata per esplorarla:",
        list(CASATE.keys())
    )
    
    if casata_scelta:
        dati = CASATE[casata_scelta]
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(f"""
            <div style="background-color: {dati['colore']}; height: 150px; border-radius: 10px; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 4rem;">⛏️</span>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f"**Nome in Khuzdûl:** *{dati['nome_khuzdul']}*")
            st.markdown(f"**Montagne:** {dati['montagna']}")
        
        with col2:
            st.subheader(casata_scelta)
            st.write(dati['descrizione'])
            
            st.markdown("**Caratteristiche distintive:**")
            for car in dati['caratteristiche']:
                st.markdown(f"- {car}")
        
        with st.expander("📖 Storia completa"):
            st.write(dati['storia'])
            st.markdown("**Personaggi noti:**")
            for pers in dati['personaggi_famosi']:
                st.markdown(f"- {pers}")
    
    st.divider()
    st.info("💡 **Curiosità:** Solo i Nani di Durin (Longbeard) hanno nomi propri conosciuti nei racconti principali. Le altre casate orientali (Ironfist, Stiffbeard, Blacklock, Stonefoot) sono menzionate solo negli scritti postumi di Tolkien.")

# PAGINA 2: PERSONAGGI FAMOSI
elif pagina == "👑 Personaggi Famosi":
    st.header("👑 Personaggi Nanici Famosi")
    
    personaggio = st.selectbox(
        "Scegli un personaggio:",
        list(PERSONAGGI_DETTAGLI.keys())
    )
    
    if personaggio:
        dati = PERSONAGGI_DETTAGLI[personaggio]
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #D4AF37, #8B4513); height: 200px; border-radius: 15px; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 5rem;">🧔</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.subheader(personaggio)
            st.markdown(f"**Casata:** {dati['casata']}")
            st.markdown(f"**Ruolo:** {dati['ruolo']}")
            st.write(dati['descrizione'])
        
        col3, col4, col5 = st.columns(3)
        with col3:
            st.metric("⚔️ Arma", dati['arma'])
        with col4:
            st.metric("💀 Morte", dati['morte'])
        with col5:
            st.metric("🗣️ Citazione", dati['citazione'])
    
    st.divider()
    
    st.subheader("📊 Distribuzione dei Personaggi per Casata")
    
    # Conteggio per casata
    conteggio = {}
    for p, d in PERSONAGGI_DETTAGLI.items():
        c = d['casata']
        conteggio[c] = conteggio.get(c, 0) + 1
    
    import pandas as pd
    df = pd.DataFrame({
        'Casata': list(conteggio.keys()),
        'Personaggi': list(conteggio.values())
    })
    
    st.bar_chart(df.set_index('Casata'))

# PAGINA 3: STORIA E CULTURA
elif pagina == "📜 Storia e Cultura":
    st.header("📜 Storia e Cultura Nanica")
    
    tab1, tab2, tab3 = st.tabs(["🏛️ Fondazione", "⚔️ Guerre", "💎 Tesori"])
    
    with tab1:
        st.subheader("La Creazione dei Nani")
        st.write("""
        Aulë il Fabbro, impaziente di vedere le creature di Ilúvatar, creò i Nani nel segreto. 
        Quando Eru lo scoprì, Aulë fu pronto a distruggerli con il martello, ma Eru li adottò e li benedisse.
        
        I Sette Padri furono posti in sonno in luoghi diversi della Terra di Mezzo, per risvegliarsi 
        dopo la comparsa degli Elfi. Durin fu il primo a svegliarsi sotto il Monte Gundabad.
        """)
        
        st.info("🕐 **Linea temporale:** Creazione → Sonno → Risveglio dopo gli Elfi → Fondazione delle grandi città")
    
    with tab2:
        st.subheader("Le Grandi Guerre")
        
        guerre = {
            "Grande Guerra dei Nani e degli Orchi (2793-2799 T.E.)": 
                "I Nani vendicarono la morte di Thrór. Dáin I Piediferro uccise Azog a Azanulbizar. Costò cara ai Nani, che persero molti guerrieri.",
            "Battaglia delle Innumerevoli Lacrime (472 P.E.)":
                "Azaghâl di Belegost ferì mortalmente Glaurung, salvando gli eserciti degli Elfi e degli Uomini.",
            "Battaglia delle Cinque Armate (2941 T.E.)":
                "Thorin Scudodiquercia, i Nani, gli Elfi, gli Uomini di Lago e le Aquile contro gli Orchi e i Warg. Thorin cadde eroicamente.",
            "Guerra dell'Anello (3018-3019 T.E.)":
                "Erebor fu assediata. Dáin II Piediferro cadde difendendo il regno all'età di 252 anni."
        }
        
        for guerra, desc in guerre.items():
            with st.expander(guerra):
                st.write(desc)
    
    with tab3:
        st.subheader("Tesori e Artefatti")
        
        tesori = [
            ("Arkenstone", "La Pietra del Re, cuore di Erebor, brillante come la luna"),
            ("Mithril", "Metallo argenteo, leggero e indistruttibile, estratto a Moria"),
            ("Nauglamír", "Collana dei Nani, forgiata per Finrod ma maledetta"),
            ("Orcrist", "Spada degli Elfi, trovata a Trollshaws, appartenuta a Thorin"),
            ("Glamdring", "Spada del Folletto, trovata insieme a Orcrist")
        ]
        
        for nome, desc in tesori:
            st.markdown(f"**💎 {nome}:** {desc}")

# PAGINA 4: QUIZ
elif pagina == "🔍 Quiz Nanico":
    st.header("🔍 Quanto conosci i Nani?")
    
    punteggio = 0
    totale = 4
    
    with st.form("quiz"):
        st.subheader("Domanda 1")
        r1 = st.radio(
            "Chi creò i Nani?",
            ["Manwë", "Aulë il Fabbro", "Morgoth", "Ilúvatar direttamente"],
            index=None
        )
        
        st.subheader("Domanda 2")
        r2 = st.radio(
            "Quante casate naniche esistono?",
            ["Tre", "Cinque", "Sette", "Nove"],
            index=None
        )
        
        st.subheader("Domanda 3")
        r3 = st.radio(
            "Chi ferì mortalmente Glaurung?",
            ["Thorin Scudodiquercia", "Azaghâl di Belegost", "Durin il Senza-Morte", "Gimli"],
            index=None
        )
        
        st.subheader("Domanda 4")
        r4 = st.radio(
            "Quale Nano partì per le Terre Immortali?",
            ["Balin", "Thorin", "Gimli", "Dáin Piediferro"],
            index=None
        )
        
        submitted = st.form_submit_button("Verifica risposte!")
    
    if submitted:
        if r1 == "Aulë il Fabbro":
            punteggio += 1
            st.success("✅ Domanda 1 corretta!")
        else:
            st.error("❌ Domanda 1: Era Aulë il Fabbro!")
            
        if r2 == "Sette":
            punteggio += 1
            st.success("✅ Domanda 2 corretta!")
        else:
            st.error("❌ Domanda 2: Erano Sette casate!")
            
        if r3 == "Azaghâl di Belegost":
            punteggio += 1
            st.success("✅ Domanda 3 corretta!")
        else:
            st.error("❌ Domanda 3: Fu Azaghâl di Belegost!")
            
        if r4 == "Gimli":
            punteggio += 1
            st.success("✅ Domanda 4 corretta!")
        else:
            st.error("❌ Domanda 4: Fu Gimli, su invito di Galadriel!")
        
        st.divider()
        st.balloons()
        st.header(f"🏆 Punteggio: {punteggio}/{totale}")
        
        if punteggio == totale:
            st.success("Sei un vero esperto della Terra di Mezzo! 🧙‍♂️")
        elif punteggio >= 2:
            st.info("Buona conoscenza, giovane apprendista! 📚")
        else:
            st.warning("Devi studiare di più i testi di Tolkien! 📖")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.8rem;">
    <p>🧙‍♂️ App creata per gli appassionati del Signore degli Anelli</p>
    <p>Basata sugli scritti di J.R.R. Tolkien</p>
</div>
""", unsafe_allow_html=True)
