"""Omnia DeepArena IA — السينما الكروية (نسخة محدّثة)"""
import streamlit as st
import html

st.set_page_config(page_title="Omnia DeepArena IA", page_icon="⚽",
                   layout="wide", initial_sidebar_state="expanded")


def esc(t):
    return html.escape(str(t)).replace("$", "&#36;")


# ══════════════════════════════════════════════════════════════
# 🎬 CSS سينمائي
# ══════════════════════════════════════════════════════════════
st.markdown("""
<style>
:root {
    --neon:#00ff88; --cyan:#00d4ff; --gold:#ffaa00;
    --ink:#eaf6f0; --muted:#b4c7bf;
}
.stApp {
    background:
        radial-gradient(ellipse at 20% 10%, rgba(0,212,255,.10), transparent 55%),
        radial-gradient(ellipse at 85% 90%, rgba(255,170,0,.08), transparent 55%),
        radial-gradient(circle at 50% 50%, #0a1a15 0%, #020604 70%, #000 100%);
    background-attachment: fixed;
    color: var(--ink);
    font-family: 'Inter', 'Segoe UI', sans-serif;
}
.stApp::before {
    content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 9999; opacity: .06;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E");
    mix-blend-mode: overlay;
}
.stApp::after {
    content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 9998;
    background: radial-gradient(ellipse at center, transparent 45%, rgba(0,0,0,.65) 100%);
}
.letterbox {
    position: fixed; left: 0; right: 0; height: 32px;
    background: linear-gradient(180deg, #000 0%, rgba(0,0,0,.85) 70%, transparent 100%);
    z-index: 9997; pointer-events: none;
}
.letterbox.top { top: 0; }
.letterbox.bottom {
    bottom: 0;
    background: linear-gradient(0deg, #000 0%, rgba(0,0,0,.85) 70%, transparent 100%);
}
[data-testid="stHeader"] { background: transparent; }
footer { visibility: hidden; }
.block-container { padding-top: 3rem; padding-bottom: 3rem; }
.rtl { direction: rtl; text-align: right; }

/* شريط التحكم العلوي (لغة + موسيقى) */
.top-controls {
    background: linear-gradient(135deg, rgba(0,255,136,.08) 0%, rgba(0,212,255,.04) 100%);
    border: 1px solid rgba(0,255,136,.30);
    border-radius: 18px;
    padding: 18px 22px;
    margin-bottom: 20px;
    box-shadow: 0 8px 30px rgba(0,0,0,.5);
    backdrop-filter: blur(15px);
}
.top-controls-title {
    color: var(--neon);
    font-size: .75rem;
    letter-spacing: 5px;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 10px;
    text-shadow: 0 0 15px rgba(0,255,136,.6);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(4,10,12,.95) 0%, rgba(0,20,15,.92) 100%) !important;
    border-inline-end: 1px solid rgba(0,255,136,.20);
}
[data-testid="stSidebar"] label p { color: var(--ink) !important; }
[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background: rgba(0,255,136,.05) !important;
    border: 1px solid rgba(0,255,136,.30) !important;
}
[data-testid="stSidebar"] div[data-baseweb="select"] * { color: var(--ink) !important; }

/* HERO */
.hero {
    position: relative; overflow: hidden;
    padding: 60px 40px 50px 40px; margin-bottom: 24px;
    border-radius: 28px;
    border: 1px solid rgba(0,255,136,.22);
    background-image:
        linear-gradient(180deg, rgba(0,0,0,.35) 0%, rgba(0,10,8,.75) 60%, rgba(0,0,0,.95) 100%),
        url("https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=1920&q=85&auto=format&fit=crop");
    background-size: cover; background-position: center;
    box-shadow: 0 30px 90px rgba(0,0,0,.85), 0 0 80px rgba(0,255,136,.08);
    animation: heroFade 1.6s ease-out;
}
@keyframes heroFade { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.hero::before {
    content: ""; position: absolute; inset: 0; pointer-events: none; opacity: .30;
    background:
        radial-gradient(circle at 50% 50%, transparent 0 90px, rgba(0,255,136,.55) 91px 92px, transparent 93px),
        linear-gradient(0deg, transparent calc(50% - 1px), rgba(0,255,136,.30) calc(50% - 1px) calc(50% + 1px), transparent calc(50% + 1px));
}
.hero > * { position: relative; z-index: 3; }
.hero-eyebrow {
    color: var(--neon); font-size: .78rem; letter-spacing: 8px;
    text-transform: uppercase; font-weight: 700; margin-bottom: 14px;
    text-shadow: 0 0 20px rgba(0,255,136,.7);
}
.hero-title {
    font-size: clamp(1.8rem, 5.5vw, 3.5rem); font-weight: 900;
    line-height: 1.05; letter-spacing: -1.5px;
    text-shadow: 0 8px 30px rgba(0,0,0,.9);
}
.hero-text {
    background: linear-gradient(90deg, var(--neon) 0%, var(--cyan) 50%, var(--gold) 100%);
    background-size: 200% auto;
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 5s linear infinite;
}
@keyframes shimmer { 0%{background-position:0% center} 100%{background-position:200% center} }
.hero-tagline {
    color: var(--gold); font-size: clamp(.9rem, 2vw, 1.1rem);
    font-weight: 700; letter-spacing: 4px; text-transform: uppercase;
    margin-top: 14px; text-shadow: 0 0 24px rgba(255,170,0,.6);
}
.hero-credit {
    position: absolute; bottom: 14px; right: 24px;
    color: rgba(255,255,255,.35); font-size: .68rem;
    letter-spacing: 4px; text-transform: uppercase;
}
.ball-float {
    position: absolute; top: 30px; right: 40px;
    width: 58px; height: 58px; border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, #fff 0%, #d8d8d8 35%, #444 100%);
    box-shadow: 0 0 30px rgba(0,255,136,.8), 0 0 60px rgba(0,255,136,.4),
                inset -6px -8px 16px rgba(0,0,0,.6), inset 4px 4px 10px rgba(255,255,255,.4);
    animation: ballSpin 8s linear infinite, ballFloat 3.5s ease-in-out infinite;
    z-index: 4; display: flex; align-items: center; justify-content: center; font-size: 30px;
}
@keyframes ballSpin { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }
@keyframes ballFloat { 0%,100%{margin-top:0} 50%{margin-top:-12px} }
.lens-flare {
    position: absolute; top: 15%; right: 8%;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(0,212,255,.35) 0%, transparent 65%);
    border-radius: 50%; pointer-events: none;
    animation: flare 6s ease-in-out infinite; z-index: 2;
}
@keyframes flare { 0%,100% { opacity: .35; transform: scale(1); } 50% { opacity: .8; transform: scale(1.15); } }

/* 🎭 تأثير تغبيش الوجه (للناشئين - GDPR) */
.blur-face img {
    filter: blur(8px) brightness(.7) saturate(1.1) !important;
    transition: filter .5s ease !important;
}
.blur-face:hover img {
    filter: blur(2px) brightness(.85) saturate(1.2) !important;
}
.blur-badge {
    position: absolute; bottom: 10px; left: 10px;
    background: rgba(0,0,0,.85); color: #00ff88;
    font-size: .65rem; font-weight: 700;
    padding: 4px 10px; border-radius: 12px;
    letter-spacing: 1px; text-transform: uppercase;
    border: 1px solid rgba(0,255,136,.5);
    z-index: 4;
    backdrop-filter: blur(10px);
}
.glass-card.rtl .blur-badge { left: auto; right: 10px; }

/* Cards */
.glass-card {
    position: relative; overflow: hidden;
    background: linear-gradient(180deg, rgba(20,25,22,.75) 0%, rgba(5,10,8,.95) 100%);
    border: 1px solid rgba(0,255,136,.20);
    border-radius: 20px; padding: 0; margin-bottom: 18px;
    box-shadow: 0 20px 50px rgba(0,0,0,.7), inset 0 1px 0 rgba(255,255,255,.06);
    transition: transform .4s cubic-bezier(.2,.8,.2,1), border-color .4s ease, box-shadow .4s ease;
}
.glass-card:hover {
    transform: translateY(-8px) scale(1.01);
    border-color: var(--neon);
    box-shadow: 0 30px 70px rgba(0,0,0,.85), 0 0 50px rgba(0,255,136,.30);
}
.card-img-wrap { position: relative; overflow: hidden; height: 150px; }
.card-img {
    width: 100%; height: 100%; object-fit: cover; display: block;
    filter: brightness(.55) saturate(1.2) contrast(1.1);
    transition: filter .5s ease, transform 1.2s cubic-bezier(.2,.8,.2,1);
}
.glass-card:hover .card-img { filter: brightness(.9) saturate(1.35); transform: scale(1.08); }
.card-img-wrap::after {
    content: ""; position: absolute; inset: 0;
    background: linear-gradient(180deg, transparent 30%, rgba(5,10,8,.95) 100%);
}
.card-icon {
    position: absolute; top: 12px; left: 14px; font-size: 20px;
    background: rgba(0,0,0,.7); border-radius: 50%;
    width: 42px; height: 42px; display: flex; align-items: center; justify-content: center;
    border: 1.5px solid rgba(0,255,136,.6); box-shadow: 0 0 18px rgba(0,255,136,.5); z-index: 3;
}
.glass-card.rtl .card-icon { left: auto; right: 14px; }
.card-body { padding: 16px 20px 20px 20px; }
.card-title { color: #fff; font-weight: 800; font-size: 1.05rem; line-height: 1.35; }
.card-desc { color: rgba(220,235,225,.75); font-size: .84rem; line-height: 1.7; margin-top: 8px; }
.card-tape {
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, var(--neon), var(--cyan), var(--gold), var(--neon));
    background-size: 300% auto; animation: shimmer 4s linear infinite; z-index: 4;
}
.card-price-wrap {
    text-align: center; margin-top: 12px; padding-top: 12px;
    border-top: 1px dashed rgba(255,170,0,.3);
}
.price-badge {
    display: inline-block;
    background: linear-gradient(135deg, #ffcc44 0%, #ffaa00 35%, #ff6600 100%);
    color: #000; font-weight: 900; font-size: 1.15rem; letter-spacing: 1px;
    padding: 7px 20px; border-radius: 40px;
    border: 1px solid rgba(255,255,255,.4);
    animation: badgePulse 2.4s ease-in-out infinite;
}
@keyframes badgePulse {
    0%,100% { box-shadow: 0 6px 25px rgba(255,170,0,.65), 0 0 40px rgba(255,170,0,.30); }
    50% { box-shadow: 0 6px 30px rgba(255,170,0,.95), 0 0 60px rgba(255,170,0,.55); }
}

/* Buttons */
div.stButton > button {
    width: 100%;
    background: linear-gradient(180deg, rgba(0,255,136,.14) 0%, rgba(0,255,136,.04) 100%);
    color: var(--neon);
    border: 1.5px solid rgba(0,255,136,.5);
    border-radius: 12px; font-weight: 700;
    letter-spacing: 1.5px; text-transform: uppercase; font-size: .8rem; padding: 12px;
    transition: all .3s ease;
    box-shadow: 0 4px 15px rgba(0,0,0,.4);
}
div.stButton > button:hover {
    background: linear-gradient(180deg, rgba(0,255,136,.30) 0%, rgba(0,255,136,.10) 100%);
    border-color: var(--neon); color: #fff;
    box-shadow: 0 8px 30px rgba(0,255,136,.5); transform: translateY(-2px);
}
[data-testid="stSidebar"] div.stButton > button {
    background: linear-gradient(180deg, rgba(255,170,0,.18) 0%, rgba(255,170,0,.05) 100%) !important;
    color: var(--gold) !important;
    border: 1px solid rgba(255,170,0,.5) !important;
}
[data-testid="stSidebar"] div.stButton > button:hover {
    background: linear-gradient(180deg, rgba(255,170,0,.35) 0%, rgba(255,170,0,.15) 100%) !important;
    color: #fff !important;
    box-shadow: 0 0 25px rgba(255,170,0,.7) !important;
}

/* Search */
div[data-baseweb="input"] {
    background: rgba(0,255,136,.04) !important;
    border: 1px solid rgba(0,255,136,.25) !important;
    border-radius: 14px !important;
}
div[data-baseweb="input"] > div { background: transparent !important; }
div[data-baseweb="input"]:focus-within {
    border-color: var(--neon) !important;
    box-shadow: 0 0 0 1px var(--neon), 0 0 30px rgba(0,255,136,.4);
}
div[data-baseweb="input"] input {
    color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important;
    padding: 14px !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] { gap: 8px; border-bottom: 1px solid rgba(0,255,136,.15); }
.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,.02); border-radius: 10px 10px 0 0;
    padding: 12px 18px; transition: all .3s ease;
}
.stTabs [data-baseweb="tab"] p {
    color: var(--muted) !important; font-weight: 700;
    letter-spacing: 1px; font-size: .78rem; text-transform: uppercase;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] { background: rgba(0,255,136,.08); }
.stTabs [data-baseweb="tab"][aria-selected="true"] p {
    color: var(--neon) !important; text-shadow: 0 0 15px rgba(0,255,136,.7);
}
.stTabs [data-baseweb="tab-highlight"] {
    background-color: var(--neon) !important; box-shadow: 0 0 20px var(--neon); height: 3px;
}
.stTabs [data-baseweb="tab-border"] { background-color: transparent !important; }
</style>

<div class="letterbox top"></div>
<div class="letterbox bottom"></div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 6 لغات × 10 باقات
# ══════════════════════════════════════════════════════════════
L = {
    "🇸🇦 العربية": {
        "title": "منصة Omnia DeepArena الرقمية العالمية",
        "tagline": "قصة كرة القدم تُروى هنا",
        "search": "🔎 ابحث عن باقة...",
        "open": "⚽ فتح الخدمة",
        "back": "⬅️ العودة إلى الرئيسية",
        "playing": "🎶 يعزف الآن",
        "stopped": "🔇 متوقف",
        "play": "▶️ تشغيل",
        "stop": "⏸️ إيقاف",
        "controls": "التحكم السريع",
        "lang_label": "🌐 اللغة",
        "music_label": "🎵 موسيقى دوري الأبطال",
        "gdpr": "🔒 وجه مُغبّش (حماية الأطفال)",
        "packs": [
            ("🥅 باقة الناشئين", "20$/ش", "مجاناً دون 16 سنة بموافقة الولي والـ GDPR", "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop", True),
            ("👟 باقة اللاعبين الكبار", "30$/ش", "تتبع YOLO26 والجاهزية البدنية الكاملة", "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop", False),
            ("📡 باقة الكشافين", "50$/ش", "رادار الفرز وقنوات التفاوض المشفرة", "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop", False),
            ("🏟️ أندية الهواة", "150$/ش", "لوحة المدرب ومحرك الريمونتادا (VIP)", "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop", False),
            ("🎽 أندية القسم الأول", "500$/ش", "بث الدرون والتوأم الرقمي للمباريات", "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop", False),
            ("🏆 أندية البطولات الكبرى", "1500$/ش", "الدخول السيبراني المعزول Cyber Sandbox", "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop", False),
            ("📋 الامتثال + بورصة اللاعبين", "%2.5 + %5", "عمولة بورصة %2.5 | %5 للمنصة + %2.5 للنشأة", "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop", False),
            ("📣 الرعاة والمستشهرين", "500$/ش", "500$ شهرياً أو 5000$ سنوياً (منفصل خارجياً)", "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop", False),
            ("🏅 الاتحاد الكروي", "150,000$/سنة", "تقارير الفيفا العلنية للتكنولوجيا", "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop", False),
            ("🚌 اللوجستية والفروع", "30$/ش", "تتبع حافلات الفريق والمعدات الميدانية", "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop", False),
        ],
        "cats": ["🌍 الكل", "⚽ اللاعبون", "🏟️ الأندية", "📡 الكشافة", "📋 المال", "🏅 الاتحادات"],
    },
    "🇬🇧 English": {
        "title": "Omnia DeepArena Global Platform",
        "tagline": "The story of football told here",
        "search": "🔎 Search a pack...",
        "open": "⚽ Open service",
        "back": "⬅️ Back to Home",
        "playing": "🎶 Playing now",
        "stopped": "🔇 Stopped",
        "play": "▶️ Play",
        "stop": "⏸️ Pause",
        "controls": "Quick Controls",
        "lang_label": "🌐 Language",
        "music_label": "🎵 UCL Anthem",
        "gdpr": "🔒 Face blurred (child protection)",
        "packs": [
            ("🥅 Youth Pack", "$20/Mo", "FREE under 16 with Parental Consent & GDPR", "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop", True),
            ("👟 Seniors Pack", "$30/Mo", "YOLO26 Kinematic Tracking & Readiness", "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop", False),
            ("📡 Scouts Market", "$50/Mo", "Ingestion Radar & Encrypted Channels", "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop", False),
            ("🏟️ Amateur Clubs", "$150/Mo", "Coach HUD & Remontada Engine (VIP)", "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop", False),
            ("🎽 Division 1 Clubs", "$500/Mo", "Drone Feed & Digital Twins", "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop", False),
            ("🏆 Championship Clubs", "$1500/Mo", "Military-Grade Cyber Sandbox", "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop", False),
            ("📋 Compliance + Token", "2.5% + 5%", "2.5% Token | 5% Platform + 2.5% Youth", "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop", False),
            ("📣 Sponsors", "$500/Mo", "$500/Mo or $5000/Yr (fund isolated)", "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop", False),
            ("🏅 Federation", "$150K/Yr", "FIFA Tech-Penetration Reports", "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop", False),
            ("🚌 Logistics", "$30/Mo", "Team Bus & Field Assets Tracking", "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop", False),
        ],
        "cats": ["🌍 All", "⚽ Players", "🏟️ Clubs", "📡 Scouts", "📋 Finance", "🏅 Federations"],
    },
    "🇫🇷 Français": {
        "title": "Plateforme Globale Omnia DeepArena",
        "tagline": "L'histoire du football racontée ici",
        "search": "🔎 Rechercher...",
        "open": "⚽ Ouvrir",
        "back": "⬅️ Retour",
        "playing": "🎶 En lecture",
        "stopped": "🔇 Arrêté",
        "play": "▶️ Lecture",
        "stop": "⏸️ Pause",
        "controls": "Contrôles Rapides",
        "lang_label": "🌐 Langue",
        "music_label": "🎵 Hymne UCL",
        "gdpr": "🔒 Visage flouté (protection enfant)",
        "packs": [
            ("🥅 Pack Jeunes", "20$/M", "GRATUIT -16 ans avec Consentement", "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop", True),
            ("👟 Pack Seniors", "30$/M", "Suivi YOLO26 & Préparation Physique", "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop", False),
            ("📡 Recruteurs", "50$/M", "Radar d'Ingestion & Canaux Chiffrés", "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop", False),
            ("🏟️ Clubs Amateurs", "150$/M", "HUD Entraîneur & Remontada (VIP)", "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop", False),
            ("🎽 Division 1", "500$/M", "Flux Drone & Jumeaux Numériques", "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop", False),
            ("🏆 Top Clubs", "1500$/M", "Cyber Sandbox Militaire", "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop", False),
            ("📋 Conformité + Token", "2.5% + 5%", "2.5% Token | 5% Plateforme + 2.5% Formation", "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop", False),
            ("📣 Sponsors", "500$/M", "500$/M ou 5000$/An (fonds isolé)", "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop", False),
            ("🏅 Fédération", "150K$/An", "Rapports FIFA Publics", "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop", False),
            ("🚌 Logistique", "30$/M", "Suivi Bus Équipe & Actifs", "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop", False),
        ],
        "cats": ["🌍 Tout", "⚽ Joueurs", "🏟️ Clubs", "📡 Recruteurs", "📋 Finance", "🏅 Fédérations"],
    },
    "🇪🇸 Español": {
        "title": "Plataforma Global Omnia DeepArena",
        "tagline": "La historia del fútbol contada aquí",
        "search": "🔎 Buscar...",
        "open": "⚽ Abrir",
        "back": "⬅️ Volver",
        "playing": "🎶 Reproduciendo",
        "stopped": "🔇 Detenido",
        "play": "▶️ Reproducir",
        "stop": "⏸️ Pausar",
        "controls": "Controles Rápidos",
        "lang_label": "🌐 Idioma",
        "music_label": "🎵 Himno UCL",
        "gdpr": "🔒 Rostro difuminado (protección infantil)",
        "packs": [
            ("🥅 Juvenil", "20$/M", "GRATIS -16 con Consentimiento", "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop", True),
            ("👟 Seniors", "30$/M", "YOLO26 y Preparación Física", "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop", False),
            ("📡 Ojeadores", "50$/M", "Radar y Canales Cifrados", "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop", False),
            ("🏟️ Amateurs", "150$/M", "HUD Entrenador y Remontada (VIP)", "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop", False),
            ("🎽 Primera Div", "500$/M", "Drones y Gemelos Digitales", "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop", False),
            ("🏆 Grandes Clubes", "1500$/M", "Cyber Sandbox Militar", "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop", False),
            ("📋 Cumplimiento + Token", "2.5% + 5%", "2.5% Token | 5% Plataforma + 2.5% Formación", "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop", False),
            ("📣 Patrocinadores", "500$/M", "500$/M o 5000$/Año (aislado)", "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop", False),
            ("🏅 Federación", "150K$/Año", "Informes FIFA Públicos", "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop", False),
            ("🚌 Logística", "30$/M", "Autobús y Activos del Equipo", "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop", False),
        ],
        "cats": ["🌍 Todo", "⚽ Jugadores", "🏟️ Clubs", "📡 Ojeadores", "📋 Finanzas", "🏅 Federaciones"],
    },
    "🇮🇹 Italiano": {
        "title": "Piattaforma Globale Omnia DeepArena",
        "tagline": "La storia del calcio raccontata qui",
        "search": "🔎 Cerca...",
        "open": "⚽ Apri",
        "back": "⬅️ Indietro",
        "playing": "🎶 In riproduzione",
        "stopped": "🔇 Fermato",
        "play": "▶️ Riproduci",
        "stop": "⏸️ Pausa",
        "controls": "Controlli Rapidi",
        "lang_label": "🌐 Lingua",
        "music_label": "🎵 Inno UCL",
        "gdpr": "🔒 Volto sfocato (protezione minori)",
        "packs": [
            ("🥅 Giovani", "20$/M", "GRATIS -16 con Consenso", "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop", True),
            ("👟 Seniors", "30$/M", "YOLO26 e Preparazione Fisica", "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop", False),
            ("📡 Scout", "50$/M", "Radar e Canali Crittografati", "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop", False),
            ("🏟️ Dilettanti", "150$/M", "HUD Allenatore e Remontada (VIP)", "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop", False),
            ("🎽 Prima Div", "500$/M", "Drone e Gemelli Digitali", "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop", False),
            ("🏆 Grandi Club", "1500$/M", "Cyber Sandbox Militare", "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop", False),
            ("📋 Conformità + Token", "2.5% + 5%", "2.5% Token | 5% Piattaforma + 2.5% Formazione", "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop", False),
            ("📣 Sponsor", "500$/M", "500$/M o 5000$/Anno (isolato)", "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop", False),
            ("🏅 Federazione", "150K$/Anno", "Report FIFA Pubblici", "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop", False),
            ("🚌 Logistica", "30$/M", "Bus Squadra e Asset", "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop", False),
        ],
        "cats": ["🌍 Tutto", "⚽ Giocatori", "🏟️ Club", "📡 Scout", "📋 Finanza", "🏅 Federazioni"],
    },
    "🇵🇹 Português": {
        "title": "Plataforma Global Omnia DeepArena",
        "tagline": "A história do futebol contada aqui",
        "search": "🔎 Pesquisar...",
        "open": "⚽ Abrir",
        "back": "⬅️ Voltar",
        "playing": "🎶 Reproduzindo",
        "stopped": "🔇 Parado",
        "play": "▶️ Reproduzir",
        "stop": "⏸️ Pausar",
        "controls": "Controles Rápidos",
        "lang_label": "🌐 Idioma",
        "music_label": "🎵 Hino UCL",
        "gdpr": "🔒 Rosto desfocado (proteção infantil)",
        "packs": [
            ("🥅 Juvenil", "20$/M", "GRÁTIS -16 com Consentimento", "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop", True),
            ("👟 Seniors", "30$/M", "YOLO26 e Prontidão Física", "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop", False),
            ("📡 Olheiros", "50$/M", "Radar e Canais Cifrados", "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop", False),
            ("🏟️ Amadores", "150$/M", "HUD Treinador e Remontada (VIP)", "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop", False),
            ("🎽 Primeira Div", "500$/M", "Drone e Gêmeos Digitais", "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop", False),
            ("🏆 Grandes", "1500$/M", "Cyber Sandbox Militar", "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop", False),
            ("📋 Conformidade + Token", "2.5% + 5%", "2.5% Token | 5% Plataforma + 2.5% Formação", "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop", False),
            ("📣 Patrocinadores", "500$/M", "500$/M ou 5000$/Ano (isolado)", "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop", False),
            ("🏅 Federação", "150K$/Ano", "Relatórios FIFA Públicos", "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop", False),
            ("🚌 Logística", "30$/M", "Ônibus e Ativos da Equipe", "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop", False),
        ],
        "cats": ["🌍 Tudo", "⚽ Jogadores", "🏟️ Clubes", "📡 Olheiros", "📋 Finanças", "🏅 Federações"],
    },
}

CATS_MAP = [None, {0,1}, {3,4,5,9}, {2}, {6}, {7,8}]

# ══════════════════════════════════════════════════════════════
# الحالة
# ══════════════════════════════════════════════════════════════
if "lang" not in st.session_state:
    st.session_state.lang = "🇸🇦 العربية"
if "page" not in st.session_state:
    st.session_state.page = None
if "playing" not in st.session_state:
    st.session_state.playing = False


# ══════════════════════════════════════════════════════════════
# الشريط الجانبي
# ══════════════════════════════════════════════════════════════
st.sidebar.image("https://img.icons8.com/fluency/96/000000/football2.png", width=70)

lang = st.sidebar.selectbox(
    "🌐 Language / اللغة",
    list(L.keys()),
    index=list(L.keys()).index(st.session_state.lang)
)
st.session_state.lang = lang
t = L[lang]
rtl = (lang == "🇸🇦 العربية")

st.sidebar.markdown("### 🎵 دوري أبطال أوروبا")
c1, c2 = st.sidebar.columns(2)
with c1:
    if st.button(t["play"], key="play_btn_sb"):
        st.session_state.playing = True
        st.rerun()
with c2:
    if st.button(t["stop"], key="stop_btn_sb"):
        st.session_state.playing = False
        st.rerun()

if st.session_state.playing:
    st.sidebar.audio(
        "https://static.calcionapoli1926.it/202109/Uefa-Champions-League.mp3",
        format="audio/mp3"
    )
    st.sidebar.success(t["playing"])
else:
    st.sidebar.info(t["stopped"])


# ══════════════════════════════════════════════════════════════
# عرض الصفحات
# ══════════════════════════════════════════════════════════════
def show_home():
    d = "rtl" if rtl else "ltr"

    # ═══ شريط التحكم العلوي (لغة + موسيقى) ═══
    st.markdown(f'<div class="top-controls"><div class="top-controls-title">⚙️ {esc(t["controls"])}</div></div>', unsafe_allow_html=True)

    colA, colB = st.columns([1, 1])
    with colA:
        st.markdown(f"**{t['lang_label']}**")
        new_lang = st.selectbox(
            "", list(L.keys()),
            index=list(L.keys()).index(st.session_state.lang),
            key="top_lang"
        )
        if new_lang != st.session_state.lang:
            st.session_state.lang = new_lang
            st.rerun()

    with colB:
        st.markdown(f"**{t['music_label']}**")
        cc1, cc2 = st.columns(2)
        with cc1:
            if st.button(t["play"], key="play_btn_top", use_container_width=True):
                st.session_state.playing = True
                st.rerun()
        with cc2:
            if st.button(t["stop"], key="stop_btn_top", use_container_width=True):
                st.session_state.playing = False
                st.rerun()

    if st.session_state.playing:
        st.audio(
            "https://static.calcionapoli1926.it/202109/Uefa-Champions-League.mp3",
            format="audio/mp3"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ═══ HERO ═══
    st.markdown(f"""
    <div class="hero {d}" dir="{d}">
        <div class="ball-float">⚽</div>
        <div class="lens-flare"></div>
        <div class="hero-eyebrow">OMNIA DEEPARENA • 2030</div>
        <div class="hero-title"><span class="hero-text">{esc(t['title'])}</span></div>
        <div class="hero-tagline">✦ {esc(t['tagline'])} ✦</div>
        <div class="hero-credit">A FOOTBALL STORY</div>
    </div>
    """, unsafe_allow_html=True)

    # ═══ البحث ═══
    query = st.text_input(t["search"], label_visibility="collapsed")
    needle = query.strip().casefold()

    # ═══ التبويبات ═══
    tabs = st.tabs(t["cats"])
    packs = t["packs"]
    for idx, (tab, members) in enumerate(zip(tabs, CATS_MAP)):
        with tab:
            shown = []
            for i, pack in enumerate(packs):
                if members is not None and i not in members:
                    continue
                if needle and needle not in pack[0].casefold() and needle not in pack[2].casefold():
                    continue
                shown.append(i)

            if not shown:
                st.info("—")
                continue

            for row_start in range(0, len(shown), 2):
                cols = st.columns(2, gap="large")
                for col, i in zip(cols, shown[row_start:row_start + 2]):
                    name, price, desc, img, blur = packs[i]
                    blur_class = "blur-face" if blur else ""
                    blur_badge = f'<span class="blur-badge">{esc(t["gdpr"])}</span>' if blur else ""
                    with col:
                        st.markdown(f"""
                        <div class="glass-card {d} {blur_class}" dir="{d}">
                            <div class="card-tape"></div>
                            <div class="card-img-wrap">
                                <img class="card-img" src="{img}" loading="lazy" alt="football">
                                <div class="card-icon">{name.split()[0]}</div>
                                {blur_badge}
                            </div>
                            <div class="card-body">
                                <div class="card-title">{esc(' '.join(name.split()[1:]))}</div>
                                <div class="card-desc">{esc(desc)}</div>
                                <div class="card-price-wrap">
                                    <span class="price-badge">💰 {esc(price)}</span>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        if st.button(t["open"], key=f"open_{idx}_{i}"):
                            st.session_state.page = i
                            st.rerun()


def show_pack(i):
    d = "rtl" if rtl else "ltr"
    name, price, desc, img, blur = t["packs"][i]

    st.markdown(f"""
    <div class="hero {d}" dir="{d}" style="padding:40px 30px;">
        <div class="hero-eyebrow">PACK #P{i+1}</div>
        <div class="hero-title"><span class="hero-text">{esc(name)}</span></div>
        <div class="hero-tagline" style="margin-top:10px;">💰 {esc(price)}</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        blur_class = "blur-face" if blur else ""
        st.markdown(f'<div class="{blur_class}">', unsafe_allow_html=True)
        st.image(img, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        if blur:
            st.caption(f"🔒 {t['gdpr']}")
    with col2:
        st.markdown(f"""
        <div class="glass-card {d}" dir="{d}" style="padding:20px;">
            <div class="card-body">
                <h3 style="color:#00ff88; margin-top:0;">💰 {esc(price)}</h3>
                <p style="color:#dbe7e1; line-height:1.8;">{esc(desc)}</p>
                <hr style="border-color:rgba(0,255,136,.2);">
                <p style="color:#dbe7e1; line-height:1.8;">
                    ✅ تجربة كاملة للمنصة<br>
                    ✅ دعم فني على مدار الساعة<br>
                    ✅ تحديثات مجانية مستمرة<br>
                    ✅ تكامل مع كل اللوائح
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button(t["back"], use_container_width=True, key="back_home"):
        st.session_state.page = None
        st.rerun()


# ══════════════════════════════════════════════════════════════
# التنفيذ
# ══════════════════════════════════════════════════════════════
if st.session_state.page is None:
    show_home()
else:
    show_pack(st.session_state.page)
