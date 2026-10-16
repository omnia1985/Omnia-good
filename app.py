"""lang_data.py — مركز الترجمات (10 باقات × 6 لغات × رموز كروية)"""
import streamlit as st

LANGS = {
    "🇸🇦 العربية": [
        "🏟️ منصة Omnia DeepArena الرقمية العالمية", "🎵 مشغل الأجواء والموسيقى",
        "🥅 باقة الناشئين والأطفال: 20$/ش (مجاناً دون 16 سنة بموافقة الولي والـ GDPR)",
        "👟 باقة اللاعبين الكبار وسينيور: 30$/ش (تتبع حركة YOLO26 والجاهزية البدنية)",
        "📡 باقة الكشافين ووكلاء الأندية: 50$/ش (رادار الفرز وقنوات التفاوض المشفرة)",
        "🏟️ باقة أندية الهواة والأكاديميات: 150$/ش (لوحة المدرب ومحرك الريمونتادا)",
        "🎽 باقة الأندية المتوسطة والدرجة الأولى: 500$/ش (بث الدرون والتوأم الرقمي)",
        "🏆 باقة أندية البطولات والكؤوس الكبرى: 1500$/ش (الدخول السيبراني المعزول)",
        "📋 بوابة الامتثال والتضامن الفيفا + بورصة اللاعبين: %2.5 عمولة بورصة | %5 للمنصة + %2.5 لحق النشأة",
        "📣 إدارة المستشهرين والرعاة: 500$/ش أو 5000$/سنوياً (مبلغ الاستشهار منفصل خارجاً)",
        "🏅 باقة الاتحاد الكروي والمنتخبات: 150,000$ سنوياً علني (تقارير الفيفا)",
        "🚌 إدارة الفروع والربط اللوجستي: 30$/شهرياً (تتبع حافلات ومعدات الفريق)",
    ],
    "🇬🇧 English": [
        "🏟️ Omnia DeepArena Global Platform", "🎵 Audio HUD & Atmosphere",
        "🥅 Youth Pack: $20/Mo (FREE under 16 with Parental Consent & GDPR)",
        "👟 Seniors Pack: $30/Mo (YOLO26 Kinematic Tracking & Readiness)",
        "📡 Scouts Market: $50/Mo (Advanced Ingestion Radar & Encrypted Channels)",
        "🏟️ Amateur Clubs: $150/Mo (Coach HUD & 50,000 Remontada Simulations)",
        "🎽 Division 1 Clubs: $500/Mo (Drone Feed & Digital Twins Orchestration)",
        "🏆 Championship Clubs: $1500/Mo (Military-Grade Cyber Sandbox)",
        "📋 FIFA Compliance & Solidarity + Tokenization: 2.5% Token | 5% Platform + 2.5% Youth Training",
        "📣 Sponsors Management: $500/Mo or $5000/Yr (fund isolated outside)",
        "🏅 National Association: $150,000/Yr Public (FIFA Tech Reports)",
        "🚌 Logistics & Branches: $30/Mo (Team Bus & Assets Tracking)",
    ],
    "🇫🇷 Français": [
        "🏟️ Plateforme Globale Omnia DeepArena", "🎵 Audio HUD & Ambiance",
        "🥅 Pack Jeunes: 20$/Mois (GRATUIT -16 ans avec Consentement & GDPR)",
        "👟 Pack Seniors: 30$/Mois (Suivi YOLO26 & Préparation Physique)",
        "📡 Marché Recruteurs: 50$/Mois (Radar d'Ingestion & Canaux Chiffrés)",
        "🏟️ Clubs Amateurs: 150$/Mois (HUD Entraîneur & Simulations Remontada)",
        "🎽 Division 1 Clubs: 500$/Mois (Flux Drone & Jumeaux Numériques)",
        "🏆 Top Clubs: 1500$/Mois (Cyber Sandbox Militaire)",
        "📋 Conformité FIFA & Solidarité + Tokenisation: 2.5% Token | 5% Plateforme + 2.5% Formation",
        "📣 Gestion Sponsors: 500$/Mois ou 5000$/An (fonds isolé dehors)",
        "🏅 Fédération Souveraine: 150 000$/An Public (Rapports FIFA)",
        "🚌 Logistique & Filiales: 30$/Mois (Suivi de flotte & bus d'équipe)",
    ],
    "🇪🇸 Español": [
        "🏟️ Plataforma Global Omnia DeepArena", "🎵 Audio HUD y Atmósfera",
        "🥅 Paquete Juvenil: 20$/Mes (GRATIS -16 años con Consentimiento & GDPR)",
        "👟 Paquete Seniors: 30$/Mes (YOLO26 y Preparación Física)",
        "📡 Mercado Agentes: 50$/Mes (Radar Ingestión y Canales Cifrados)",
        "🏟️ Clubs Amateurs: 150$/Mes (HUD Entrenador y Simulaciones Remontada)",
        "🎽 Primera División: 500$/Mes (Drones y Gemelos Digitales)",
        "🏆 Clubs Grandes: 1500$/Mes (Cyber Sandbox Militar)",
        "📋 Cumplimiento FIFA & Solidaridad + Tokenización: 2.5% Token | 5% Plataforma + 2.5% Formación",
        "📣 Patrocinadores: 500$/Mes o 5000$/Año (fondo aislado afuera)",
        "🏅 Asociación Nacional: 150,000$/Año Público (Informes FIFA)",
        "🚌 Hub Logístico: 30$/Mes (Autobús del equipo y flota)",
    ],
    "🇮🇹 Italiano": [
        "🏟️ Piattaforma Globale Omnia DeepArena", "🎵 Audio HUD & Atmosfera",
        "🥅 Pacchetto Giovani: 20$/Mese (GRATIS -16 con Consenso & GDPR)",
        "👟 Pacchetto Seniors: 30$/Mese (Tracciamento YOLO26 & Prontezza)",
        "📡 Mercato Scout: 50$/Mese (Radar Ingestione & Canali Crittografati)",
        "🏟️ Club Dilettanti: 150$/Mese (HUD Allenatore & Simulazioni Remontada)",
        "🎽 Prima Divisione: 500$/Mese (Feed Drone & Gemelli Digitali)",
        "🏆 Grandi Club: 1500$/Mese (Cyber Sandbox Militare)",
        "📋 Conformità FIFA & Solidarietà + Tokenizzazione: 2.5% Token | 5% Piattaforma + 2.5% Formazione",
        "📣 Gestione Sponsor: 500$/Mese o 5000$/Anno (fondo isolato)",
        "🏅 Federazione Sovrana: 150.000$/Anno Pubblico (Report FIFA)",
        "🚌 Logistica & Filiali: 30$/Mese (Pullman squadra e flotta)",
    ],
    "🇵🇹 Português": [
        "🏟️ Plataforma Global Omnia DeepArena", "🎵 Áudio HUD & Atmosfera",
        "🥅 Pack Juvenil: 20$/Mês (GRÁTIS -16 com Consentimento & GDPR)",
        "👟 Pack Seniors: 30$/Mês (Rastreamento YOLO26 & Prontidão)",
        "📡 Mercado Agentes: 50$/Mês (Radar Ingestão & Canais Cifrados)",
        "🏟️ Clubes Amadores: 150$/Mês (HUD Treinador & Simulações Remontada)",
        "🎽 Primeira Divisão: 500$/Mês (Feed Drone & Gêmeos Digitais)",
        "🏆 Grandes Clubes: 1500$/Mês (Cyber Sandbox Militar)",
        "📋 Conformidade FIFA & Solidariedade + Tokenização: 2.5% Token | 5% Plataforma + 2.5% Formação",
        "📣 Patrocinadores: 500$/Mês ou 5000$/Ano (fundo isolado)",
        "🏅 Associação Nacional: 150.000$/Ano Visível (Relatórios FIFA)",
        "🚌 Hub Logístico: 30$/Mês (Ônibus da equipe e frota)",
    ],
}

PRICES = {
    "🇸🇦 العربية": {1:"20$/ش", 2:"30$/ش", 3:"50$/ش", 4:"150$/ش", 5:"500$/ش", 6:"1500$/ش",
                   7:"%2.5 + %5", 8:"500$/ش", 9:"150,000$/سنة", 10:"30$/ش"},
    "🇬🇧 English": {1:"$20/Mo", 2:"$30/Mo", 3:"$50/Mo", 4:"$150/Mo", 5:"$500/Mo", 6:"$1500/Mo",
                   7:"2.5% + 5%", 8:"$500/Mo", 9:"$150K/Yr", 10:"$30/Mo"},
    "🇫🇷 Français": {1:"20$/M", 2:"30$/M", 3:"50$/M", 4:"150$/M", 5:"500$/M", 6:"1500$/M",
                   7:"2.5% + 5%", 8:"500$/M", 9:"150K$/An", 10:"30$/M"},
    "🇪🇸 Español": {1:"20$/M", 2:"30$/M", 3:"50$/M", 4:"150$/M", 5:"500$/M", 6:"1500$/M",
                   7:"2.5% + 5%", 8:"500$/M", 9:"150K$/Año", 10:"30$/M"},
    "🇮🇹 Italiano": {1:"20$/M", 2:"30$/M", 3:"50$/M", 4:"150$/M", 5:"500$/M", 6:"1500$/M",
                   7:"2.5% + 5%", 8:"500$/M", 9:"150K$/Anno", 10:"30$/M"},
    "🇵🇹 Português": {1:"20$/M", 2:"30$/M", 3:"50$/M", 4:"150$/M", 5:"500$/M", 6:"1500$/M",
                   7:"2.5% + 5%", 8:"500$/M", 9:"150K$/Ano", 10:"30$/M"},
}

UI = {
    "🇸🇦 العربية": {"sub":"⚽ كل ما يهم كرة القدم — وكرة القدم فقط.","search":"🔎 ابحث عن باقة...",
        "open":"⚽ فتح الخدمة","soon":"🛠️ قيد الإعداد","empty":"لا توجد نتائج","back":"⬅️ العودة للرئيسية",
        "details":"تفاصيل الباقة","features":"✨ المميزات","price":"💰 السعر","pitch":"⚽ الخريطة التكتيكية",
        "tagline":"قصة كرة القدم تُروى هنا",
        "cats":["🌍 الكل","⚽ اللاعبون","🏟️ الأندية","📡 الكشافة","📋 المال والامتثال","🏅 الاتحادات والرعاة"]},
    "🇬🇧 English": {"sub":"⚽ Everything that matters in football — and only football.","search":"🔎 Search...",
        "open":"⚽ Open service","soon":"🛠️ Coming soon","empty":"No results","back":"⬅️ Back to Home",
        "details":"Package Details","features":"✨ Features","price":"💰 Price","pitch":"⚽ Tactical Map",
        "tagline":"The story of football told here",
        "cats":["🌍 All","⚽ Players","🏟️ Clubs","📡 Scouts","📋 Finance & Compliance","🏅 Federations"]},
    "🇫🇷 Français": {"sub":"⚽ Tout ce qui compte pour le football — et rien que le football.","search":"🔎 Rechercher...",
        "open":"⚽ Ouvrir","soon":"🛠️ Bientôt","empty":"Aucun résultat","back":"⬅️ Retour",
        "details":"Détails","features":"✨ Caractéristiques","price":"💰 Prix","pitch":"⚽ Carte Tactique",
        "tagline":"L'histoire du football racontée ici",
        "cats":["🌍 Tout","⚽ Joueurs","🏟️ Clubs","📡 Recruteurs","📋 Finance","🏅 Fédérations"]},
    "🇪🇸 Español": {"sub":"⚽ Todo lo que importa en el fútbol — y solo fútbol.","search":"🔎 Buscar...",
        "open":"⚽ Abrir","soon":"🛠️ Próximamente","empty":"Sin resultados","back":"⬅️ Volver",
        "details":"Detalles","features":"✨ Características","price":"💰 Precio","pitch":"⚽ Mapa Táctico",
        "tagline":"La historia del fútbol contada aquí",
        "cats":["🌍 Todo","⚽ Jugadores","🏟️ Clubs","📡 Ojeadores","📋 Finanzas","🏅 Federaciones"]},
    "🇮🇹 Italiano": {"sub":"⚽ Tutto ciò che conta nel calcio — e solo il calcio.","search":"🔎 Cerca...",
        "open":"⚽ Apri","soon":"🛠️ In arrivo","empty":"Nessun risultato","back":"⬅️ Indietro",
        "details":"Dettagli","features":"✨ Caratteristiche","price":"💰 Prezzo","pitch":"⚽ Mappa Tattica",
        "tagline":"La storia del calcio raccontata qui",
        "cats":["🌍 Tutto","⚽ Giocatori","🏟️ Club","📡 Scout","📋 Finanza","🏅 Federazioni"]},
    "🇵🇹 Português": {"sub":"⚽ Tudo o que importa no futebol — e só futebol.","search":"🔎 Pesquisar...",
        "open":"⚽ Abrir","soon":"🛠️ Em breve","empty":"Sem resultados","back":"⬅️ Voltar",
        "details":"Detalhes","features":"✨ Características","price":"💰 Preço","pitch":"⚽ Mapa Tático",
        "tagline":"A história do futebol contada aqui",
        "cats":["🌍 Tudo","⚽ Jogadores","🏟️ Clubes","📡 Olheiros","📋 Finanças","🏅 Federações"]},
}

RTL = {"🇸🇦 العربية"}
CATS = [None, {1,2}, {4,5,6,10}, {3}, {7}, {8,9}]

PACK_IMG = {
    1:  "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop",
    2:  "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop",
    3:  "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop",
    4:  "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop",
    5:  "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop",
    6:  "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop",
    7:  "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop",
    8:  "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop",
    9:  "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop",
    10: "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop",
}

HERO_IMG = "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=1920&q=85&auto=format&fit=crop"

AUDIO = {
    "🏆 Champions League": "https://static.calcionapoli1926.it/202109/Uefa-Champions-League.mp3",
    "🔊 Experituelle Stadium": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
}
CHAMPIONS_AUDIO = AUDIO["🏆 Champions League"]

def get_lang() -> str:
    names = list(LANGS)
    saved = st.session_state.get("lang", names[0])
    return saved if saved in names else names[0]

def set_lang(lang: str) -> None: st.session_state["lang"] = lang
def get_ui() -> dict: return UI[get_lang()]
def get_titles() -> list: return LANGS[get_lang()]
def get_prices() -> dict: return PRICES[get_lang()]
def is_rtl() -> bool: return get_lang() in RTL
def dir_attr() -> str: return "rtl" if is_rtl() else "ltr"

def render_music_player() -> None:
    import urllib.request
    if "music_playing" not in st.session_state:
        st.session_state.music_playing = False
    lang = get_lang()
    labels = {
        "🇸🇦 العربية": {"title":"🎵 دوري الأبطال","play":"▶️ تشغيل","stop":"⏸️ إيقاف",
            "download":"⬇️ تحميل","playing":"🎶 يعزف","stopped":"🔇 متوقف",
            "dl_loading":"⏳ جاري...","dl_ready":"✅ الملف جاهز"},
        "🇬🇧 English": {"title":"🎵 UCL Anthem","play":"▶️ Play","stop":"⏸️ Pause",
            "download":"⬇️ Download","playing":"🎶 Playing","stopped":"🔇 Stopped",
            "dl_loading":"⏳ Loading...","dl_ready":"✅ Ready"},
        "🇫🇷 Français": {"title":"🎵 Hymne UCL","play":"▶️ Lecture","stop":"⏸️ Pause",
            "download":"⬇️ Télécharger","playing":"🎶 En lecture","stopped":"🔇 Arrêté",
            "dl_loading":"⏳ Chargement...","dl_ready":"✅ Prêt"},
        "🇪🇸 Español": {"title":"🎵 Himno UCL","play":"▶️ Reproducir","stop":"⏸️ Pausar",
            "download":"⬇️ Descargar","playing":"🎶 Reproduciendo","stopped":"🔇 Detenido",
            "dl_loading":"⏳ Cargando...","dl_ready":"✅ Listo"},
        "🇮🇹 Italiano": {"title":"🎵 Inno UCL","play":"▶️ Riproduci","stop":"⏸️ Pausa",
            "download":"⬇️ Scarica","playing":"🎶 In riproduzione","stopped":"🔇 Fermato",
            "dl_loading":"⏳ Caricamento...","dl_ready":"✅ Pronto"},
        "🇵🇹 Português": {"title":"🎵 Hino UCL","play":"▶️ Reproduzir","stop":"⏸️ Pausar",
            "download":"⬇️ Baixar","playing":"🎶 Reproduzindo","stopped":"🔇 Parado",
            "dl_loading":"⏳ Carregando...","dl_ready":"✅ Pronto"},
    }
    lbl = labels.get(lang, labels["🇬🇧 English"])
    st.sidebar.markdown(f"### {lbl['title']}")
    c1, c2 = st.sidebar.columns(2)
    with c1:
        if st.button(lbl["play"], key="btn_play_ucl", use_container_width=True):
            st.session_state.music_playing = True; st.rerun()
    with c2:
        if st.button(lbl["stop"], key="btn_stop_ucl", use_container_width=True):
            st.session_state.music_playing = False; st.rerun()
    if st.session_state.music_playing:
        st.sidebar.audio(CHAMPIONS_AUDIO, format="audio/mp3")
        st.sidebar.success(lbl["playing"])
    else:
        st.sidebar.info(lbl["stopped"])
    st.sidebar.markdown("---")
    @st.cache_data(ttl=3600, show_spinner=False)
    def _fetch(url: str) -> bytes:
        try:
            req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as r:
                return r.read()
        except Exception:
            return b""
    if st.sidebar.button(lbl["download"], key="btn_dl_ucl", use_container_width=True):
        with st.spinner(lbl["dl_loading"]):
            data = _fetch(CHAMPIONS_AUDIO)
        if data:
            st.session_state["music_bytes"] = data; st.rerun()
        else:
            st.sidebar.error("⚠️ Download failed")
    if st.session_state.get("music_bytes"):
        st.sidebar.download_button(
            label=lbl["dl_ready"], data=st.session_state["music_bytes"],
            file_name="champions_league_anthem.mp3", mime="audio/mpeg",
            key="dl_ucl_final", use_container_width=True)
