"""Omnia DeepArena IA — السينما الكروية الكاملة (ملف واحد)"""
import streamlit as st
import html

st.set_page_config(page_title="Omnia DeepArena IA", page_icon="⚽",
                   layout="wide", initial_sidebar_state="expanded")


def esc(t):
    return html.escape(str(t)).replace("$", "&#36;")


# ══════════════════════════════════════════════════════════════
# 🎬 CSS سينمائي كامل
# ══════════════════════════════════════════════════════════════
st.markdown("""
<style>
:root {
    --neon:#00ff88; --cyan:#00d4ff; --gold:#ffaa00;
    --ink:#eaf6f0; --muted:#b4c7bf;
}

/* خلفية سينمائية */
.stApp {
    background:
        radial-gradient(ellipse at 20% 10%, rgba(0,212,255,.10), transparent 55%),
        radial-gradient(ellipse at 85% 90%, rgba(255,170,0,.08), transparent 55%),
        radial-gradient(circle at 50% 50%, #0a1a15 0%, #020604 70%, #000 100%);
    background-attachment: fixed;
    color: var(--ink);
    font-family: 'Inter', 'Segoe UI', sans-serif;
}
/* Film Grain */
.stApp::before {
    content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 9999; opacity: .06;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E");
    mix-blend-mode: overlay;
}
/* Vignette */
.stApp::after {
    content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 9998;
    background: radial-gradient(ellipse at center, transparent 45%, rgba(0,0,0,.65) 100%);
}
/* Letterbox */
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
.block-container { padding-top: 3.5rem; padding-bottom: 3rem; }
.rtl { direction: rtl; text-align: right; }

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

/* HERO سينمائي */
.hero {
    position: relative; overflow: hidden;
    padding: 70px 40px 60px 40px; margin-bottom: 24px;
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
.hero-sub {
    color: rgba(234,246,240,.85); margin-top: 18px;
    font-size: 1rem; line-height: 1.8; max-width: 780px;
}
.hero-credit {
    position: absolute; bottom: 14px; right: 24px;
    color: rgba(255,255,255,.35); font-size: .68rem;
    letter-spacing: 4px; text-transform: uppercase;
}

/* كرة طائرة */
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

/* Lens Flare */
.lens-flare {
    position: absolute; top: 15%; right: 8%;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(0,212,255,.35) 0%, transparent 65%);
    border-radius: 50%; pointer-events: none;
    animation: flare 6s ease-in-out infinite; z-index: 2;
}
@keyframes flare { 0%,100% { opacity: .35; transform: scale(1); } 50% { opacity: .8; transform: scale(1.15); } }

/* Pitch 3D */
.pitch-wrap { max-width: 760px; margin: 40px auto; perspective: 1100px; }
.pitch {
    position: relative; width: 100%; aspect-ratio: 3/2; border-radius: 20px;
    background:
        radial-gradient(ellipse at center, rgba(0,255,136,.08) 0%, transparent 70%),
        repeating-linear-gradient(90deg,
            rgba(0,45,20,.92) 0px, rgba(0,45,20,.92) 42px,
            rgba(0,60,28,.92) 42px, rgba(0,60,28,.92) 84px);
    border: 2px solid rgba(0,255,136,.40);
    box-shadow: 0 40px 100px rgba(0,0,0,.75), inset 0 0 80px rgba(0,0,0,.7), 0 0 50px rgba(0,255,136,.15);
    transform: rotateX(8deg);
    animation: pitchRise 1.8s ease-out;
}
@keyframes pitchRise { from { opacity: 0; transform: rotateX(8deg) scale(.95); } to { opacity: 1; transform: rotateX(8deg) scale(1); } }
.pitch::before {
    content: ""; position: absolute; inset: 0; pointer-events: none;
    background:
        linear-gradient(90deg, transparent calc(50% - 1px), rgba(255,255,255,.55) calc(50% - 1px) calc(50% + 1px), transparent calc(50% + 1px)),
        radial-gradient(circle at 50% 50%, transparent 0 52px, rgba(255,255,255,.55) 53px 55px, transparent 56px);
}
.pitch-label {
    text-align: center; color: var(--neon); font-size: .78rem;
    letter-spacing: 8px; margin-bottom: 16px; font-weight: 700;
    text-transform: uppercase; text-shadow: 0 0 20px rgba(0,255,136,.8);
}

/* Cards سينمائية */
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

/* شارة ذهبية نابضة */
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

/* أزرار */
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
[data-testid="stSidebar"] div.stDownloadButton > button {
    background: linear-gradient(180deg, rgba(0,255,136,.18) 0%, rgba(0,255,136,.05) 100%) !important;
    color: var(--neon) !important;
    border: 1px solid rgba(0,255,136,.5) !important;
    width: 100% !important;
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
# 6 لغات × 10 باقات (كامل داخل الملف)
# ══════════════════════════════════════════════════════════════
L = {
    "🇸🇦 العربية": {
        "title": "منصة Omnia DeepArena الرقمية العالمية",
        "tagline": "قصة كرة القدم تُروى هنا",
        "sub": "⚽ كل ما يهم كرة القدم — وكرة القدم فقط.",
        "search": "🔎 ابحث عن باقة...",
        "open": "⚽ فتح الخدمة",
        "back": "⬅️ العودة إلى الرئيسية",
        "pitch": "الخريطة التكتيكية",
        "playing": "🎶 يعزف الآن",
        "stopped": "🔇 متوقف",
        "play": "▶️ تشغيل",
        "stop": "⏸️ إيقاف",
        "dl": "⬇️ تحميل",
        "packs": [
            ("🥅 باقة الناشئين", "20$/ش", "مجاناً دون 16 سنة بموافقة الولي والـ GDPR", "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop"),
            ("👟 باقة اللاعبين الكبار", "30$/ش", "تتبع YOLO26 والجاهزية البدنية الكاملة", "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop"),
            ("📡 باقة الكشافين", "50$/ش", "رادار الفرز وقنوات التفاوض المشفرة", "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop"),
            ("🏟️ أندية الهواة", "150$/ش", "لوحة المدرب ومحرك الريمونتادا (VIP)", "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop"),
            ("🎽 أندية القسم الأول", "500$/ش", "بث الدرون والتوأم الرقمي للمباريات", "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop"),
            ("🏆 أندية البطولات الكبرى", "1500$/ش", "الدخول السيبراني المعزول Cyber Sandbox", "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop"),
            ("📋 الامتثال + بورصة اللاعبين", "%2.5 + %5", "عمولة بورصة %2.5 | %5 للمنصة + %2.5 للنشأة", "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop"),
            ("📣 الرعاة والمستشهرين", "500$/ش", "500$ شهرياً أو 5000$ سنوياً (منفصل خارجياً)", "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop"),
            ("🏅 الاتحاد الكروي", "150,000$/سنة", "تقارير الفيفا العلنية للتكنولوجيا", "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop"),
            ("🚌 اللوجستية والفروع", "30$/ش", "تتبع حافلات الفريق والمعدات الميدانية", "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop"),
        ],
        "cats": ["🌍 الكل", "⚽ اللاعبون", "🏟️ الأندية", "📡 الكشافة", "📋 المال", "🏅 الاتحادات"],
    },
    "🇬🇧 English": {
        "title": "Omnia DeepArena Global Platform",
        "tagline": "The story of football told here",
        "sub": "⚽ Everything that matters in football — and only football.",
        "search": "🔎 Search a pack...",
        "open": "⚽ Open service",
        "back": "⬅️ Back to Home",
        "pitch": "Tactical Map",
        "playing": "🎶 Playing now",
        "stopped": "🔇 Stopped",
        "play": "▶️ Play",
        "stop": "⏸️ Pause",
        "dl": "⬇️ Download",
        "packs": [
            ("🥅 Youth Pack", "$20/Mo", "FREE under 16 with Parental Consent & GDPR", "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop"),
            ("👟 Seniors Pack", "$30/Mo", "YOLO26 Kinematic Tracking & Readiness", "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop"),
            ("📡 Scouts Market", "$50/Mo", "Ingestion Radar & Encrypted Channels", "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop"),
            ("🏟️ Amateur Clubs", "$150/Mo", "Coach HUD & Remontada Engine (VIP)", "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop"),
            ("🎽 Division 1 Clubs", "$500/Mo", "Drone Feed & Digital Twins", "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop"),
            ("🏆 Championship Clubs", "$1500/Mo", "Military-Grade Cyber Sandbox", "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop"),
            ("📋 Compliance + Token", "2.5% + 5%", "2.5% Token | 5% Platform + 2.5% Youth", "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop"),
            ("📣 Sponsors", "$500/Mo", "$500/Mo or $5000/Yr (fund isolated)", "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop"),
            ("🏅 Federation", "$150K/Yr", "FIFA Tech-Penetration Reports", "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop"),
            ("🚌 Logistics", "$30/Mo", "Team Bus & Field Assets Tracking", "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop"),
        ],
        "cats": ["🌍 All", "⚽ Players", "🏟️ Clubs", "📡 Scouts", "📋 Finance", "🏅 Federations"],
    },
    "🇫🇷 Français": {
        "title": "Plateforme Globale Omnia DeepArena",
        "tagline": "L'histoire du football racontée ici",
        "sub": "⚽ Tout ce qui compte pour le football — et rien que le football.",
        "search": "🔎 Rechercher...",
        "open": "⚽ Ouvrir",
        "back": "⬅️ Retour",
        "pitch": "Carte Tactique",
        "playing": "🎶 En lecture",
        "stopped": "🔇 Arrêté",
        "play": "▶️ Lecture",
        "stop": "⏸️ Pause",
        "dl": "⬇️ Télécharger",
        "packs": [
            ("🥅 Pack Jeunes", "20$/M", "GRATUIT -16 ans avec Consentement", "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop"),
            ("👟 Pack Seniors", "30$/M", "Suivi YOLO26 & Préparation Physique", "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop"),
            ("📡 Recruteurs", "50$/M", "Radar d'Ingestion & Canaux Chiffrés", "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop"),
            ("🏟️ Clubs Amateurs", "150$/M", "HUD Entraîneur & Remontada (VIP)", "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop"),
            ("🎽 Division 1", "500$/M", "Flux Drone & Jumeaux Numériques", "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop"),
            ("🏆 Top Clubs", "1500$/M", "Cyber Sandbox Militaire", "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop"),
            ("📋 Conformité + Token", "2.5% + 5%", "2.5% Token | 5% Plateforme + 2.5% Formation", "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop"),
            ("📣 Sponsors", "500$/M", "500$/M ou 5000$/An (fonds isolé)", "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop"),
            ("🏅 Fédération", "150K$/An", "Rapports FIFA Publics", "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop"),
            ("🚌 Logistique", "30$/M", "Suivi Bus Équipe & Actifs", "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop"),
        ],
        "cats": ["🌍 Tout", "⚽ Joueurs", "🏟️ Clubs", "📡 Recruteurs", "📋 Finance", "🏅 Fédérations"],
    },
    "🇪🇸 Español": {
        "title": "Plataforma Global Omnia DeepArena",
        "tagline": "La historia del fútbol contada aquí",
        "sub": "⚽ Todo lo que importa en el fútbol — y solo fútbol.",
        "search": "🔎 Buscar...",
        "open": "⚽ Abrir",
        "back": "⬅️ Volver",
        "pitch": "Mapa Táctico",
        "playing": "🎶 Reproduciendo",
        "stopped": "🔇 Detenido",
        "play": "▶️ Reproducir",
        "stop": "⏸️ Pausar",
        "dl": "⬇️ Descargar",
        "packs": [
            ("🥅 Juvenil", "20$/M", "GRATIS -16 con Consentimiento", "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop"),
            ("👟 Seniors", "30$/M", "YOLO26 y Preparación Física", "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop"),
            ("📡 Ojeadores", "50$/M", "Radar y Canales Cifrados", "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop"),
            ("🏟️ Amateurs", "150$/M", "HUD Entrenador y Remontada (VIP)", "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop"),
            ("🎽 Primera Div", "500$/M", "Drones y Gemelos Digitales", "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop"),
            ("🏆 Grandes Clubes", "1500$/M", "Cyber Sandbox Militar", "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop"),
            ("📋 Cumplimiento + Token", "2.5% + 5%", "2.5% Token | 5% Plataforma + 2.5% Formación", "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop"),
            ("📣 Patrocinadores", "500$/M", "500$/M o 5000$/Año (aislado)", "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop"),
            ("🏅 Federación", "150K$/Año", "Informes FIFA Públicos", "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop"),
            ("🚌 Logística", "30$/M", "Autobús y Activos del Equipo", "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop"),
        ],
        "cats": ["🌍 Todo", "⚽ Jugadores", "🏟️ Clubs", "📡 Ojeadores", "📋 Finanzas", "🏅 Federaciones"],
    },
    "🇮🇹 Italiano": {
        "title": "Piattaforma Globale Omnia DeepArena",
        "tagline": "La storia del calcio raccontata qui",
        "sub": "⚽ Tutto ciò che conta nel calcio — e solo il calcio.",
        "search": "🔎 Cerca...",
        "open": "⚽ Apri",
        "back": "⬅️ Indietro",
        "pitch": "Mappa Tattica",
        "playing": "🎶 In riproduzione",
        "stopped": "🔇 Fermato",
        "play": "▶️ Riproduci",
        "stop": "⏸️ Pausa",
        "dl": "⬇️ Scarica",
        "packs": [
            ("🥅 Giovani", "20$/M", "GRATIS -16 con Consenso", "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop"),
            ("👟 Seniors", "30$/M", "YOLO26 e Preparazione Fisica", "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop"),
            ("📡 Scout", "50$/M", "Radar e Canali Crittografati", "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop"),
            ("🏟️ Dilettanti", "150$/M", "HUD Allenatore e Remontada (VIP)", "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop"),
            ("🎽 Prima Div", "500$/M", "Drone e Gemelli Digitali", "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop"),
            ("🏆 Grandi Club", "1500$/M", "Cyber Sandbox Militare", "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop"),
            ("📋 Conformità + Token", "2.5% + 5%", "2.5% Token | 5% Piattaforma + 2.5% Formazione", "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop"),
            ("📣 Sponsor", "500$/M", "500$/M o 5000$/Anno (isolato)", "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop"),
            ("🏅 Federazione", "150K$/Anno", "Report FIFA Pubblici", "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop"),
            ("🚌 Logistica", "30$/M", "Bus Squadra e Asset", "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop"),
        ],
        "cats": ["🌍 Tutto", "⚽ Giocatori", "🏟️ Club", "📡 Scout", "📋 Finanza", "🏅 Federazioni"],
    },
    "🇵🇹 Português": {
        "title": "Plataforma Global Omnia DeepArena",
        "tagline": "A história do futebol contada aqui",
        "sub": "⚽ Tudo o que importa no futebol — e só futebol.",
        "search": "🔎 Pesquisar...",
        "open": "⚽ Abrir",
        "back": "⬅️ Voltar",
        "pitch": "Mapa Tático",
        "playing": "🎶 Reproduzindo",
        "stopped": "🔇 Parado",
        "play": "▶️ Reproduzir",
        "stop": "⏸️ Pausar",
        "dl": "⬇️ Baixar",
        "packs": [
            ("🥅 Juvenil", "20$/M", "GRÁTIS -16 com Consentimento", "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80&auto=format&fit=crop"),
            ("👟 Seniors", "30$/M", "YOLO26 e Prontidão Física", "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&q=80&auto=format&fit=crop"),
            ("📡 Olheiros", "50$/M", "Radar e Canais Cifrados", "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=800&q=80&auto=format&fit=crop"),
            ("🏟️ Amadores", "150$/M", "HUD Treinador e Remontada (VIP)", "https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&q=80&auto=format&fit=crop"),
            ("🎽 Primeira Div", "500$/M", "Drone e Gêmeos Digitais", "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?w=800&q=80&auto=format&fit=crop"),
            ("🏆 Grandes", "1500$/M", "Cyber Sandbox Militar", "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=800&q=80&auto=format&fit=crop"),
            ("📋 Conformidade + Token", "2.5% + 5%", "2.5% Token | 5% Plataforma + 2.5% Formação", "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80&auto=format&fit=crop"),
            ("📣 Patrocinadores", "500$/M", "500$/M ou 5000$/Ano (isolado)", "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?w=800&q=80&auto=format&fit=crop"),
            ("🏅 Federação", "150K$/Ano", "Relatórios FIFA Públicos", "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&q=80&auto=format&fit=crop"),
            ("🚌 Logística", "30$/M", "Ônibus e Ativos da Equipe", "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80&auto=format&fit=crop"),
        ],
        "cats": ["🌍 Tudo", "⚽ Jogadores", "🏟️ Clubes", "📡 Olheiros", "📋 Finanças", "🏅 Federações"],
    },
}

# الفئات (10 باقات: 7 و 8 مدموجتان في رقم 7)
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

# مشغل موسيقى دوري الأبطال
st.sidebar.markdown("### 🎵 دوري أبطال أوروبا")
c1, c2 = st.sidebar.columns(2)
with c1:
    if st.button(t["play"], key="play_btn"):
        st.session_state.playing = True
        st.rerun()
with c2:
    if st.button(t["stop"], key="stop_btn"):
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

st.sidebar.markdown("---")
st.sidebar.markdown(f"**🌐 {lang}**")

# ══════════════════════════════════════════════════════════════
# عرض الصفحات
# ══════════════════════════════════════════════════════════════
def show_home():
    d = "rtl" if rtl else "ltr"
    # HERO
    st.markdown(f"""
    <div class="hero {d}" dir="{d}">
        <div class="ball-float">⚽</div>
        <div class="lens-flare"></div>
        <div class="hero-eyebrow">OMNIA DEEPARENA • 2030</div>
        <div class="hero-title"><span class="hero-text">{esc(t['title'])}</span></div>
        <div class="hero-tagline">✦ {esc(t['tagline'])} ✦</div>
        <div class="hero-sub">{esc(t['sub'])}</div>
        <div class="hero-credit">A FOOTBALL STORY</div>
    </div>
    """, unsafe_allow_html=True)

    # PITCH 3D
    st.markdown(f"""
    <div class="pitch-wrap">
        <div class="pitch-label">⚽ {esc(t['pitch'])} ⚽</div>
        <div class="pitch"></div>
    </div>
    """, unsafe_allow_html=True)

    # البحث
    query = st.text_input(t["search"], label_visibility="collapsed")
    needle = query.strip().casefold()

    # التبويبات
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

            # عرض بطاقتين في كل صف
            for row_start in range(0, len(shown), 2):
                cols = st.columns(2, gap="large")
                for col, i in zip(cols, shown[row_start:row_start + 2]):
                    name, price, desc, img = packs[i]
                    with col:
                        st.markdown(f"""
                        <div class="glass-card {d}" dir="{d}">
                            <div class="card-tape"></div>
                            <div class="card-img-wrap">
                                <img class="card-img" src="{img}" loading="lazy" alt="football">
                                <div class="card-icon">{name.split()[0]}</div>
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
    name, price, desc, img = t["packs"][i]

    st.markdown(f"""
    <div class="hero {d}" dir="{d}" style="padding:40px 30px;">
        <div class="hero-eyebrow">PACK #P{i+1}</div>
        <div class="hero-title"><span class="hero-text">{esc(name)}</span></div>
        <div class="hero-sub">{esc(desc)}</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(img, use_container_width=True)
    with col2:
        st.markdown(f"""
        <div class="glass-card {d}" dir="{d}" style="padding:20px;">
            <div class="card-body">
                <h3 style="color:#00ff88; margin-top:0;">💰 {esc(price)}</h3>
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
