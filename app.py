"""Omnia DeepArena IA — الصفحة الرئيسية (app.py)

تشغيل:   streamlit run app.py
الصفحات: ضع كل باقة داخل مجلد pages/ بملف يبدأ اسمه برقمها،
         مثال: pages/1_Youth.py  أو  pages/8_Compliance.py
"""
import html
import re
from pathlib import Path

import streamlit as st

# ══════════════════════════════════════════════════════════════
# 1) إعداد الصفحة — يجب أن يكون أول أمر Streamlit
# ══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Omnia DeepArena IA",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════
# 2) التصميم الزجاجي + لمسات النيون (CSS فقط، بلا موارد خارجية)
# ══════════════════════════════════════════════════════════════
CSS = """
<style>
:root { --neon:#00ff88; --cyan:#00d4ff; --ink:#eaf6f0; --muted:#b4c7bf; }

/* خلفية بتدرجات CSS فقط: بلا صور خارجية (أسرع، وأنسب للـ GDPR) */
.stApp {
    background:
        radial-gradient(1000px 560px at 8% -8%, rgba(0,255,136,.13), transparent 60%),
        radial-gradient(900px 600px at 100% 108%, rgba(0,212,255,.11), transparent 60%),
        linear-gradient(160deg, #040a18 0%, #01100a 100%);
    background-attachment: fixed;
    color: var(--ink);
}
[data-testid="stHeader"] { background: transparent; }
footer { visibility: hidden; }
.block-container { padding-top: 2rem; }
.rtl { direction: rtl; text-align: right; }

/* الشريط الجانبي الزجاجي */
[data-testid="stSidebar"] {
    background: rgba(255,255,255,.04) !important;
    -webkit-backdrop-filter: blur(16px);
    backdrop-filter: blur(16px);
    border-inline-end: 1px solid rgba(0,255,136,.18);
}
[data-testid="stSidebar"] label p,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p { color: var(--ink) !important; }
[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background: rgba(255,255,255,.06) !important;
    border: 1px solid rgba(0,255,136,.25) !important;
}
[data-testid="stSidebar"] div[data-baseweb="select"] * { color: var(--ink) !important; }

/* البطل (Hero) مع رسمة ملعب بالنيون */
.hero {
    position: relative; overflow: hidden;
    padding: 22px 20px; margin-bottom: 14px;
    border-radius: 18px;
    border: 1px solid rgba(0,255,136,.20);
    background: rgba(255,255,255,.04);
    -webkit-backdrop-filter: blur(14px);
    backdrop-filter: blur(14px);
    box-shadow: 0 10px 40px rgba(0,0,0,.35), 0 0 30px rgba(0,255,136,.06);
}
.hero::before {
    content: ""; position: absolute; inset: 0; pointer-events: none; opacity: .45;
    background:
        radial-gradient(circle at 90% 50%, transparent 0 38px, rgba(0,255,136,.55) 39px 40px, transparent 41px),
        linear-gradient(90deg, transparent calc(90% - 1px), rgba(0,255,136,.35) calc(90% - 1px) calc(90% + 1px), transparent calc(90% + 1px));
}
.hero.rtl::before { transform: scaleX(-1); }
.hero > * { position: relative; }
.hero-title { font-size: clamp(1.45rem, 4.6vw, 2.4rem); font-weight: 800; line-height: 1.3; }
.hero-text {
    background: linear-gradient(90deg, var(--neon), var(--cyan));
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-sub { color: var(--muted); margin-top: 8px; font-size: .95rem; line-height: 1.7; }
.hero-line {
    height: 2px; margin-top: 14px; border-radius: 2px;
    background: linear-gradient(90deg, var(--neon), transparent);
    box-shadow: 0 0 12px var(--neon);
}
.hero.rtl .hero-line { background: linear-gradient(270deg, var(--neon), transparent); }

/* الكروت الزجاجية */
.glass-card {
    background: rgba(255,255,255,.05);
    -webkit-backdrop-filter: blur(14px);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(0,255,136,.18);
    border-radius: 16px;
    padding: 16px 18px;
    margin-bottom: 8px;
    box-shadow: 0 8px 32px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.06);
    transition: transform .2s ease, border-color .2s ease, box-shadow .2s ease;
}
.glass-card:hover {
    transform: translateY(-3px);
    border-color: var(--neon);
    box-shadow: 0 12px 40px rgba(0,255,136,.16), inset 0 1px 0 rgba(255,255,255,.08);
}
.card-title { color: var(--neon); font-weight: 700; font-size: 1.02rem; text-shadow: 0 0 12px rgba(0,255,136,.35); }
.card-desc { color: #dbe7e1; font-size: .88rem; line-height: 1.7; margin-top: 6px; }

/* أزرار النيون */
div.stButton > button {
    width: 100%;
    background: rgba(0,255,136,.06);
    color: var(--neon);
    border: 1px solid rgba(0,255,136,.40);
    border-radius: 12px;
    font-weight: 600;
    transition: all .2s ease;
}
div.stButton > button:hover {
    background: rgba(0,255,136,.16);
    border-color: var(--neon);
    color: #fff;
    box-shadow: 0 0 18px rgba(0,255,136,.35);
}
div.stButton > button:active { transform: scale(.98); }

/* خانة البحث */
div[data-baseweb="input"] {
    background: rgba(255,255,255,.06) !important;
    border: 1px solid rgba(0,255,136,.25) !important;
    border-radius: 12px !important;
}
div[data-baseweb="input"] > div { background: transparent !important; }
div[data-baseweb="input"]:focus-within {
    border-color: var(--neon) !important;
    box-shadow: 0 0 0 1px var(--neon), 0 0 18px rgba(0,255,136,.25);
}
div[data-baseweb="input"] input {
    color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important;
}
div[data-baseweb="input"] input::placeholder {
    color: rgba(234,246,240,.55) !important; -webkit-text-fill-color: rgba(234,246,240,.55) !important;
}

/* التبويبات */
.stTabs [data-baseweb="tab"] p { color: var(--muted) !important; font-weight: 600; }
.stTabs [data-baseweb="tab"][aria-selected="true"] p {
    color: var(--neon) !important; text-shadow: 0 0 10px rgba(0,255,136,.45);
}
.stTabs [data-baseweb="tab-highlight"] { background-color: var(--neon) !important; box-shadow: 0 0 10px var(--neon); }
.stTabs [data-baseweb="tab-border"] { background-color: rgba(255,255,255,.10) !important; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# 3) النصوص — كل قائمة: [العنوان، عنوان مشغّل الصوت، ثم الباقات P1…P11]
#    الباقة رقم n موجودة في الفهرس n+1
# ══════════════════════════════════════════════════════════════
LANGS = {
    "🇸🇦 العربية": [
        "🏟️ منصة Omnia DeepArena الرقمية العالمية", "🎵 مشغل الأجواء والموسيقى المشحونة",
        "👶 باقة الناشئين والأطفال (صفحة 1): 20$/ش (✨ مجاناً دون 16 سنة بموافقة الولي والـ GDPR وتفعيل كروت التشبيه)",
        "🏃 باقة اللاعبين الكبار وسينيور (صفحة 2): 30$/ش (تتبع حركة YOLO26 والوصول التشريحي والجاهزية البدنية)",
        "🔍 باقة الكشافين ووكلاء الأندية (صفحة 3): 50$/ش (رادار الفرز وقنوات التفاوض المشفرة لجلب العمولات)",
        "🏪 باقة أندية الهواة والأكاديميات (صفحة 4): 150$/ش (لوحة المدرب ومحرك الريمونتادا بـ 50,000 محاكاة خططية)",
        "🏢 باقة الأندية المتوسطة والدرجة الأولى (صفحة 5): 500$/ش (سحب بث طائرات الدرون والتوأم الرقمي للمباريات)",
        "🏰 باقة أندية البطولات والكؤوس الكبرى (صفحة 6): 1500$/ش (الدخول السيبراني المعزول Cyber Sandbox وحظر التجسس)",
        "📊 بورصة أسهم اللاعبين والتسييل المالي (صفحة 7): نسبة عمولة إدارية ثابتة %2.5 (تداول الأسهم المصغرة بـ 15$ خارجاً)",
        "⚖️ بوابة الامتثال وآلية التضامن الفيفا (صفحة 8): نسبة عمولة صفقات %5 للمنصة | نسبة حق رعاية نشأة %2.5 للأكاديمية",
        "🎯 صفحة إدارة المستشهرين والرعاة (صفحة 9): 500$/ش أو 5000$/سنوياً رسوم تشغيل (مبلغ الاستشهار منفصل تماماً خارجاً بوضوح)",
        "🏆 باقة الاتحاد الكروي والمنتخبات (صفحة 10): 150,000$ سنوياً ظاهر وعلني (لإصدار تقارير التطور ونسبة التكنولوجيا للفيفا)",
        "🚛 إدارة الفروع والربط اللوجستي للأصول (صفحة 11): 30$/شهرياً (تتبع سيارات ومعدات الميدان وإبراز العمولات للنزاهة)",
    ],
    "🇬🇧 English": [
        "🏟️ Omnia DeepArena Global Platform", "🎵 Audio HUD & Atmosphere",
        "👶 Youth Pack (P1): $20/Mo (✨ 100% FREE under 16 with Parental Consent & GDPR Star Cards)",
        "🏃 Seniors Pack (P2): $30/Mo (Real-Time YOLO26 Kinematic Tracking & Anatomical Readiness)",
        "🔍 Scouts Market (P3): $50/Mo (Advanced Ingestion Radar & Encrypted Negotiation Channels)",
        "🏪 Amateur Clubs (P4): $150/Mo (Integrated Coach HUD & 50,000 Remontada Simulations)",
        "🏢 Division 1 Clubs (P5): $500/Mo (Drone Feed Integration & Live Digital Twins Orchestration)",
        "🏰 Championship Clubs (P6): $1500/Mo (Military-Grade Cyber Sandbox for Counter-Tactical Espionage)",
        "📊 FinTech Tokenization (P7): Public 2.5% Platform Admin Commission (Micro-Tokens at $15/share outside)",
        "⚖️ FIFA Solidarity Gate (P8): 5% Platform Transaction Fee | 2.5% Automated Youth Training Right",
        "🎯 Sponsors Management (P9): $500/Mo or $5000/Yr Fee (Sponsorship fund isolated outside clearly)",
        "🏆 National Association (P10): $150,000/Yr Public & Visible (Generates Tech-Penetration Reports for FIFA)",
        "🚛 Logistics & Branches (P11): $30/Mo (Tracking company field fleet & assets with public commission display)",
    ],
    "🇫🇷 Français": [
        "🏟️ Plateforme Globale Omnia DeepArena", "🎵 Audio HUD & Ambiance",
        "👶 Pack Jeunes (P1): 20$/Mois (✨ GRATUIT moins de 16 ans avec Consentement Parental & GDPR)",
        "🏃 Pack Seniors (P2): 30$/Mois (Suivi Cinématique YOLO26 & Préparation Anatomique)",
        "🔍 Marché Recruteurs (P3): 50$/Mois (Radar d'Ingestion & Négociations Chiffrées)",
        "🏪 Clubs Amateurs (P4): 150$/Mois (HUD Entraîneur & 50 000 Simulations de Remontada)",
        "🏢 Division 1 Clubs (P5): 500$/Mois (Flux Drone & Orchestration Jumeaux Numériques)",
        "🏰 Top Clubs (P6): 1500$/Mois (Cyber Sandbox de Niveau Militaire Contre l'Espionnage)",
        "📊 Tokenisation FinTech (P7): Commission Admin 2.5% (Micro-Tokens à 15$/action dehors)",
        "⚖️ Solidarité FIFA (P8): Commission Plateforme 5% | Droit de Formation 2.5%",
        "🎯 Gestion Sponsors (P9): Frais 500$/Mois (Fonds de sponsoring isolé à l'extérieur)",
        "🏆 Fédération Souveraine (P10): 150 000$/An Public (Rapports de Pénétration Tech FIFA)",
        "🚛 Logistique & Filiales (P11): 30$/Mois (Suivi de flotte & affichage public des commissions)",
    ],
    "🇪🇸 Español": [
        "🏟️ Plataforma Global Omnia DeepArena", "🎵 Audio HUD y Atmósfera",
        "👶 Paquete Juvenil (P1): 20$/Mes (✨ GRATIS menos de 16 años con Consentimiento Parental & GDPR)",
        "🏃 Paquete Seniors (P2): 30$/Mes (Movimiento YOLO26 y Preparación Anatómica)",
        "🔍 Mercado Agentes (P3): 50$/Mes (Radar Ingestión y Canales de Negociación Cifrados)",
        "🏪 Clubs Amateurs (P4): 150$/Mes (HUD Entrenador y 50,000 Simulaciones de Remontada)",
        "🏢 Primera División (P5): 500$/Mes (Integración Drones y Gemelos Digitales)",
        "🏰 Clubs Grandes (P6): 1500$/Mes (Cyber Sandbox Contra Espionaje Táctico)",
        "📊 Tokenización FinTech (P7): Comisión Admin 2.5% (Micro-Tokens a 15$/acción afuera)",
        "⚖️ Solidaridad FIFA (P8): Comisión Plataforma 5% | Derecho Formación 2.5%",
        "🎯 Patrocinadores (P9): Tarifa 500$/Mes (Fondo de patrocinio aislado afuera)",
        "🏆 Asociación Nacional (P10): 150,000$/Año Público (Informes de Penetración Tech FIFA)",
        "🚛 Hub Logístico (P11): 30$/Mes (Seguimiento de flota y comisiones públicas)",
    ],
    "🇮🇹 Italiano": [
        "🏟️ Piattaforma Globale Omnia DeepArena", "🎵 Audio HUD & Atmosfera",
        "👶 Pacchetto Giovani (P1): 20$/Mese (✨ GRATIS sotto 16 con Consenso Parentale & GDPR)",
        "🏃 Pacchetto Seniors (P2): 30$/Mese (Tracciamento Cinematico YOLO26 & Prontezza)",
        "🔍 Mercato Scout (P3): 50$/Mese (Radar Ingestione & Canali Crittografati)",
        "🏪 Club Dilettanti (P4): 150$/Mese (HUD Allenatore & 50.000 Simulazioni Remontada)",
        "🏢 Prima Divisione (P5): 500$/Mese (Feed Drone & Gemelli Digitali Live)",
        "🏰 Grandi Club (P6): 1500$/Mese (Cyber Sandbox Contro lo Spionaggio Tattico)",
        "📊 Tokenizzazione FinTech (P7): Commissione Admin 2.5% (Micro-Token a 15$/azione fuori)",
        "⚖️ Solidarietà FIFA (P8): Commissione 5% | Diritto di Formazione 2.5%",
        "🎯 Gestione Sponsor (P9): Quota 500$/Mese (Fondo sponsor isolato esternamente)",
        "🏆 Federazione Sovrana (P10): 150.000$/Anno Pubblico (Report Penetrazione Tech FIFA)",
        "🚛 Logistica & Filiali (P11): 30$/Mese (Tracciamento flotta & commissioni pubbliche)",
    ],
    "🇵🇹 Português": [
        "🏟️ Plataforma Global Omnia DeepArena", "🎵 Áudio HUD & Atmosfera",
        "👶 Pack Juvenil (P1): 20$/Mês (✨ GRÁTIS menor de 16 com Consentimento & GDPR)",
        "🏃 Pack Seniors (P2): 30$/Mês (Rastreamento YOLO26 & Prontidão Anatómica)",
        "🔍 Mercado Agentes (P3): 50$/Mês (Radar Ingestão & Canais Cifrados)",
        "🏪 Clubes Amadores (P4): 150$/Mês (HUD Treinador & 50.000 Simulações Remontada)",
        "🏢 Primeira Divisão (P5): 500$/Mês (Feed Drone & Gêmeos Digitais ao Vivo)",
        "🏰 Grandes Clubes (P6): 1500$/Mês (Cyber Sandbox Contra Espionagem Táctica)",
        "📊 Tokenização FinTech (P7): Comissão Admin 2.5% (Micro-Tokens a 15$/ação fora)",
        "⚖️ Solidariedade FIFA (P8): Comissão 5% | Direito de Formação 2.5%",
        "🎯 Patrocinadores (P9): Taxa 500$/Mês (Fundo de patrocínio isolado fora)",
        "🏆 Associação Nacional (P10): 150.000$/Ano Visível (Relatórios Penetração Tech FIFA)",
        "🚛 Hub Logístico (P11): 30$/Mês (Rastreamento de frota & comissões públicas)",
    ],
}

# نصوص الواجهة المساعدة + أسماء الفئات (نفس ترتيب CATS)
UI = {
    "🇸🇦 العربية": {
        "sub": "⚽ كل ما يهم كرة القدم — وكرة القدم فقط. تصفّح الباقات واللوائح المالية الموحّدة بسهولة.",
        "search": "🔎 ابحث عن باقة أو لائحة...",
        "open": "🚀 فتح الخدمة",
        "soon": "🛠️ هذه الصفحة قيد الإعداد",
        "empty": "لا توجد نتائج مطابقة",
        "cats": ["🌍 الكل", "⚽ اللاعبون", "🏟️ الأندية", "🔍 الكشافة والوكلاء", "⚖️ المال والامتثال", "🏆 الاتحادات والرعاة"],
    },
    "🇬🇧 English": {
        "sub": "⚽ Everything that matters in football — and only football. Browse the packs and unified financial rules with ease.",
        "search": "🔎 Search a pack or rule...",
        "open": "🚀 Open service",
        "soon": "🛠️ This page is not ready yet",
        "empty": "No matching results",
        "cats": ["🌍 All", "⚽ Players", "🏟️ Clubs", "🔍 Scouts & Agents", "⚖️ Finance & Compliance", "🏆 Federations & Sponsors"],
    },
    "🇫🇷 Français": {
        "sub": "⚽ Tout ce qui compte pour le football — et rien que le football. Parcourez facilement les forfaits et les règles financières unifiées.",
        "search": "🔎 Rechercher un forfait ou une règle...",
        "open": "🚀 Ouvrir le service",
        "soon": "🛠️ Cette page n'est pas encore prête",
        "empty": "Aucun résultat",
        "cats": ["🌍 Tout", "⚽ Joueurs", "🏟️ Clubs", "🔍 Recruteurs & Agents", "⚖️ Finance & Conformité", "🏆 Fédérations & Sponsors"],
    },
    "🇪🇸 Español": {
        "sub": "⚽ Todo lo que importa en el fútbol — y solo fútbol. Explora fácilmente los paquetes y las reglas financieras unificadas.",
        "search": "🔎 Buscar un paquete o una regla...",
        "open": "🚀 Abrir servicio",
        "soon": "🛠️ Esta página aún no está lista",
        "empty": "Sin resultados",
        "cats": ["🌍 Todo", "⚽ Jugadores", "🏟️ Clubes", "🔍 Ojeadores y Agentes", "⚖️ Finanzas y Cumplimiento", "🏆 Federaciones y Patrocinadores"],
    },
    "🇮🇹 Italiano": {
        "sub": "⚽ Tutto ciò che conta nel calcio — e solo il calcio. Esplora facilmente i pacchetti e le regole finanziarie unificate.",
        "search": "🔎 Cerca un pacchetto o una regola...",
        "open": "🚀 Apri il servizio",
        "soon": "🛠️ Questa pagina non è ancora pronta",
        "empty": "Nessun risultato",
        "cats": ["🌍 Tutto", "⚽ Giocatori", "🏟️ Club", "🔍 Scout e Agenti", "⚖️ Finanza e Conformità", "🏆 Federazioni e Sponsor"],
    },
    "🇵🇹 Português": {
        "sub": "⚽ Tudo o que importa no futebol — e só futebol. Explore facilmente os pacotes e as regras financeiras unificadas.",
        "search": "🔎 Pesquisar um pacote ou regra...",
        "open": "🚀 Abrir serviço",
        "soon": "🛠️ Esta página ainda não está pronta",
        "empty": "Sem resultados",
        "cats": ["🌍 Tudo", "⚽ Jogadores", "🏟️ Clubes", "🔍 Olheiros e Agentes", "⚖️ Finanças e Conformidade", "🏆 Federações e Patrocinadores"],
    },
}

# الفئات حسب أطراف كرة القدم (أرقام الباقات) — None = الكل
CATS = [None, {1, 2}, {4, 5, 6, 11}, {3}, {7, 8}, {9, 10}]

RTL = {"🇸🇦 العربية"}

# ملفان صوتيان تجريبيان — استبدلهما بملفاتك
# (الأفضل رفعها في المستودع واستخدام مسار محلي مثل "assets/ambience.mp3")
AUDIO = {
    "🏆 Champions League": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "🔊 Experituelle Stadium": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
}


# ══════════════════════════════════════════════════════════════
# 4) دوال مساعدة
# ══════════════════════════════════════════════════════════════
def esc(text: str) -> str:
    """تهريب HTML + منع Streamlit من تفسير $...$ كمعادلة رياضية."""
    return html.escape(text).replace("$", "&#36;")


@st.cache_data(ttl=60, show_spinner=False)
def find_pages() -> dict[int, str]:
    """يربط رقم الباقة بملفها داخل pages/ (أول ملف يبدأ اسمه بالرقم)."""
    found: dict[int, str] = {}
    for f in sorted((Path(__file__).parent / "pages").glob("*.py")):
        m = re.match(r"(?i)(?:page|p)?[_\-\s]*0*(\d+)", f.stem)
        if m:
            found.setdefault(int(m.group(1)), f"pages/{f.name}")
    return found


def open_page(n: int, ui: dict) -> None:
    target = find_pages().get(n)
    if target:
        st.switch_page(target)  # يوقف السكربت ويفتح الصفحة
    else:
        st.toast(f"{ui['soon']} — `pages/{n}_*.py`", icon="🛠️")


def card(title: str, desc: str, rtl: bool) -> None:
    direction = "rtl" if rtl else "ltr"
    st.markdown(
        f'<div class="glass-card {direction}" dir="{direction}">'
        f'<div class="card-title">{esc(title)}</div>'
        f'<div class="card-desc">{esc(desc)}</div></div>',
        unsafe_allow_html=True,
    )


def render_grid(pages: list, prefix: str, d: list, ui: dict, rtl: bool) -> None:
    if not pages:
        card("🔎", ui["empty"], rtl)
        return
    # صفوف من عمودين: على الجوال تتراص الكروت بالترتيب الطبيعي 1، 2، 3…
    for i in range(0, len(pages), 2):
        for col, n in zip(st.columns(2, gap="medium"), pages[i:i + 2]):
            with col:
                title, _, desc = d[n + 1].partition(":")
                card(title.strip(), desc.strip(), rtl)
                if st.button(ui["open"], key=f"{prefix}_{n}"):
                    open_page(n, ui)


# ══════════════════════════════════════════════════════════════
# 5) الشريط الجانبي: اللغة + الأجواء الصوتية
# ══════════════════════════════════════════════════════════════
names = list(LANGS)
saved = st.session_state.get("lang", names[0])
lang = st.sidebar.selectbox(
    "🌐 Language / اللغة", names, index=names.index(saved) if saved in names else 0
)
st.session_state["lang"] = lang  # تقرؤه بقية صفحات pages/ ويبقى عند التنقل
d, ui = LANGS[lang], UI[lang]
is_rtl = lang in RTL

track = st.sidebar.radio(d[1], list(AUDIO))
st.sidebar.audio(AUDIO[track])

# ══════════════════════════════════════════════════════════════
# 6) الواجهة الرئيسية
# ══════════════════════════════════════════════════════════════
direction = "rtl" if is_rtl else "ltr"
icon, _, title_text = d[0].partition(" ")
st.markdown(
    f'<div class="hero {direction}" dir="{direction}">'
    f'<div class="hero-title"><span>{esc(icon)}</span> <span class="hero-text">{esc(title_text)}</span></div>'
    f'<div class="hero-sub">{esc(ui["sub"])}</div>'
    f'<div class="hero-line"></div></div>',
    unsafe_allow_html=True,
)

query = st.text_input(ui["search"], placeholder=ui["search"], label_visibility="collapsed")
needle = query.strip().casefold()
all_pages = range(1, len(d) - 1)  # 1…11

for idx, (tab, members) in enumerate(zip(st.tabs(ui["cats"]), CATS)):
    with tab:
        shown = [
            n for n in all_pages
            if (members is None or n in members) and needle in d[n + 1].casefold()
        ]
        render_grid(shown, f"t{idx}", d, ui, is_rtl)
