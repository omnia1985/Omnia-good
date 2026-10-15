import streamlit as st

# ==========================================
# 1. إعدادات الصفحة الأساسية
# ==========================================
st.set_page_config(
    page_title="Omnia Football Arena 2030",
    layout="wide",
    page_icon="⚽"
)

# ==========================================
# 2. تصميم الملعب + إجبار الأعمدة أفقياً + الزجاجية
# ==========================================
st.markdown("""
<style>
    /* إجبار الأعمدة على البقاء أفقية حتى على الهاتف */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 4px !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
    }
    div[data-testid="column"] {
        min-width: 0 !important;
        flex: 1 1 0 !important;
        padding: 2px !important;
    }
    
    /* خلفية الملعب */
    .stApp {
        background: repeating-linear-gradient(0deg, #0d3d14 0px, #0d3d14 40px, #14501c 40px, #14501c 80px);
        background-attachment: fixed;
        color: #ffffff;
    }
    
    /* حاوية الملعب */
    .pitch-container {
        position: relative;
        background: rgba(0, 0, 0, 0.25);
        border: 2px solid rgba(255, 255, 255, 0.6);
        border-radius: 15px;
        padding: 15px 8px;
        margin: 10px auto;
        box-shadow: inset 0 0 60px rgba(0,0,0,0.5);
    }
    
    /* بطاقات اللاعبين */
    div.stButton > button {
        background: rgba(0, 0, 0, 0.75) !important;
        backdrop-filter: blur(10px) !important;
        border: 2px solid #00ff88 !important;
        border-radius: 10px !important;
        color: #ffffff !important;
        padding: 6px 2px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(0, 255, 136, 0.3) !important;
        width: 100% !important;
        white-space: pre-wrap !important;
        font-size: 9px !important;
        line-height: 1.2 !important;
        min-height: 60px !important;
    }
    div.stButton > button:hover {
        transform: scale(1.08) !important;
        border-color: #ffaa00 !important;
        box-shadow: 0 0 25px rgba(255, 170, 0, 0.7) !important;
        color: #ffaa00 !important;
    }
    
    /* حارس المرمى */
    .gk-btn div.stButton > button {
        background: rgba(255, 170, 0, 0.3) !important;
        border: 3px solid #ffaa00 !important;
        box-shadow: 0 0 30px rgba(255, 170, 0, 0.9) !important;
        color: #ffaa00 !important;
    }
    
    /* بطاقة VIP للـ 150$ */
    .vip-card {
        background: rgba(255, 170, 0, 0.1);
        border: 2px solid #ffaa00;
        box-shadow: 0 0 25px rgba(255, 170, 0, 0.5);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        position: relative;
    }
    .vip-card::before {
        content: "⭐ VIP";
        position: absolute;
        top: -10px; right: 15px;
        background: #ffaa00; color: #000;
        font-size: 10px; font-weight: bold;
        padding: 2px 8px; border-radius: 8px;
    }
    
    /* البطاقات الزجاجية */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(0, 255, 136, 0.3);
        border-radius: 15px;
        padding: 15px;
        margin: 8px 0;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    h1 { 
        color: #ffffff !important; 
        text-align: center; 
        text-shadow: 0 0 15px rgba(0, 255, 136, 0.9);
        font-size: 20px !important;
    }
    h3 { 
        color: #ffffff !important; 
        text-align: center; 
        text-shadow: 0 0 10px rgba(0, 255, 136, 0.8);
        font-size: 12px !important;
        margin: 10px 0 5px 0 !important;
    }
    p { font-size: 13px; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. بيانات اللغات الست الكاملة
# ==========================================
LANG_DATA = {
    "🇸🇦 العربية": {
        "title": "🏟️ Omnia Football Arena 2030",
        "subtitle": "انقر على أي لاعب للانتقال إلى صفحته. حارس المرمى هو الصفحة الرئيسية.",
        "audio_label": "🎵 الأجواء والموسيقى",
        "attack": "⚔️ خط الهجوم",
        "midfield": "⚙️ خط الوسط",
        "defense": "🛡️ خط الدفاع",
        "gk": "🧤 حارس المرمى (app.py)",
        "gk_you": "أنت هنا الآن",
        "back": "⬅️ العودة إلى الملعب",
        "packages_title": "💎 باقات الاشتراك المتاحة",
        "p1": "👶 الناشئين: 20$/ش (مجاناً دون 16 سنة والـ GDPR)",
        "p2": "🏃 اللاعبين الكبار: 30$/ش (تتبع YOLO26)",
        "p3": "🔍 الكشافين: 50$/ش",
        "p4": "🏆 أندية الهواة: 150$/ش (الريمونتادا)", 
        "p5": "⚽ أندية القسم الأول: 500$/ش",
        "p6": "👑 الأندية الكبرى: 1500$/ش (Sandbox)",
        "stats_title": "📊 إحصائيات متقدمة",
        "plan_title": "🎯 خطة التطوير"
    },
    "🇬🇧 English": {
        "title": "🏟️ Omnia Football Arena 2030",
        "subtitle": "Click any player to open their page. Goalkeeper is the main page.",
        "audio_label": "🎵 Stadium Atmosphere",
        "attack": "⚔️ Attack Line",
        "midfield": "⚙️ Midfield Line",
        "defense": "🛡️ Defense Line",
        "gk": "🧤 Goalkeeper (app.py)",
        "gk_you": "You are here",
        "back": "⬅️ Back to Pitch",
        "packages_title": "💎 Subscription Packages",
        "p1": "👶 Youth: $20/Mo (FREE under 16 & GDPR)",
        "p2": "🏃 Seniors: $30/Mo (YOLO26 Tracking)",
        "p3": "🔍 Scouts: $50/Mo",
        "p4": "🏆 Amateur Clubs: $150/Mo",
        "p5": "⚽ Division 1: $500/Mo",
        "p6": "👑 Elite Clubs: $1500/Mo (Sandbox)",
        "stats_title": "📊 Advanced Stats",
        "plan_title": "🎯 Development Plan"
    },
    "🇫🇷 Français": {
        "title": "🏟️ Omnia Football Arena 2030",
        "subtitle": "Cliquez sur un joueur pour ouvrir sa page. Le gardien est la page principale.",
        "audio_label": "🎵 Ambiance du Stade",
        "attack": "⚔️ Ligne d'Attaque",
        "midfield": "⚙️ Milieu de Terrain",
        "defense": "🛡️ Ligne de Défense",
        "gk": "🧤 Gardien de But (app.py)",
        "gk_you": "Vous êtes ici",
        "back": "⬅️ Retour au Terrain",
        "packages_title": "💎 Forfaits d'Abonnement",
        "p1": "👶 Jeunes: 20$/M (GRATUIT -16 ans & RGPD)",
        "p2": "🏃 Seniors: 30$/M (YOLO26)",
        "p3": "🔍 Recruteurs: 50$/M",
        "p4": "🏆 Clubs Amateurs: 150$/M",
        "p5": "⚽ Division 1: 500$/M",
        "p6": "👑 Clubs Élite: 1500$/M (Sandbox)",
        "stats_title": "📊 Statistiques Avancées",
        "plan_title": "🎯 Plan de Développement"
    },
    "🇪🇸 Español": {
        "title": "🏟️ Omnia Football Arena 2030",
        "subtitle": "Haz clic en un jugador para abrir su página. El portero es la página principal.",
        "audio_label": "🎵 Ambiente del Estadio",
        "attack": "⚔️ Línea de Ataque",
        "midfield": "⚙️ Línea de Mediocampo",
        "defense": "🛡️ Línea Defensiva",
        "gk": "🧤 Portero (app.py)",
        "gk_you": "Estás aquí",
        "back": "⬅️ Volver al Campo",
        "packages_title": "💎 Paquetes de Suscripción",
        "p1": "👶 Juvenil: 20$/M (GRATIS -16 & RGPD)",
        "p2": "🏃 Seniors: 30$/M (YOLO26)",
        "p3": "🔍 Scouts: 50$/M",
        "p4": "🏆 Clubes Amateurs: 150$/M",
        "p5": "⚽ Primera División: 500$/M",
        "p6": "👑 Clubes Élite: 1500$/M (Sandbox)",
        "stats_title": "📊 Estadísticas Avanzadas",
        "plan_title": "🎯 Plan de Desarrollo"
    },
    "🇮🇹 Italiano": {
        "title": "🏟️ Omnia Football Arena 2030",
        "subtitle": "Clicca su un giocatore per aprire la sua pagina. Il portiere è la pagina principale.",
        "audio_label": "🎵 Atmosfera dello Stadio",
        "attack": "⚔️ Linea d'Attacco",
        "midfield": "⚙️ Linea di Centrocampo",
        "defense": "🛡️ Linea Difensiva",
        "gk": "🧤 Portiere (app.py)",
        "gk_you": "Sei qui",
        "back": "⬅️ Torna al Campo",
        "packages_title": "💎 Pacchetti di Abbonamento",
        "p1": "👶 Giovani: 20$/M (GRATIS -16 & GDPR)",
        "p2": "🏃 Seniores: 30$/M (YOLO26)",
        "p3": "🔍 Scout: 50$/M",
        "p4": "🏆 Club Dilettanti: 150$/M",
        "p5": "⚽ Prima Divisione: 500$/M",
        "p6": "👑 Club d'Élite: 1500$/M (Sandbox)",
        "stats_title": "📊 Statistiche Avanzate",
        "plan_title": "🎯 Piano di Sviluppo"
    },
    "🇵🇹 Português": {
        "title": "🏟️ Omnia Football Arena 2030",
        "subtitle": "Clique em um jogador para abrir a página. O goleiro é a página principal.",
        "audio_label": "🎵 Atmosfera do Estádio",
        "attack": "⚔️ Linha de Ataque",
        "midfield": "⚙️ Linha de Meio-Campo",
        "defense": "🛡️ Linha Defensiva",
        "gk": "🧤 Goleiro (app.py)",
        "gk_you": "Você está aqui",
        "back": "⬅️ Voltar ao Campo",
        "packages_title": "💎 Pacotes de Assinatura",
        "p1": "👶 Juvenil: 20$/M (GRÁTIS -16 & GDPR)",
        "p2": "🏃 Seniores: 30$/M (YOLO26)",
        "p3": "🔍 Scouts: 50$/M",
        "p4": "🏆 Clubes Amadores: 150$/M",
        "p5": "⚽ Primeira Divisão: 500$/M",
        "p6": "👑 Clubes de Elite: 1500$/M (Sandbox)",
        "stats_title": "📊 Estatísticas Avançadas",
        "plan_title": "🎯 Plano de Desenvolvimento"
    }
}

# ==========================================
# 4. بيانات اللاعبين (الـ 10 + الرئيسية)
# ==========================================
PLAYERS_DATA = {
    "Page 1": {"pos": "🛡️ RB", "img": "https://images.unsplash.com/photo-1552674605-db6ffd4facb5?w=800&auto=format&fit=crop"},
    "Page 2": {"pos": "🛡️ CB", "img": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop"},
    "Page 3": {"pos": "⚙️ DM", "img": "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&auto=format&fit=crop"},
    "Page 4": {"pos": "⚙️ CM", "img": "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&auto=format&fit=crop"},
    "Page 5": {"pos": "🚀 RW", "img": "https://images.unsplash.com/photo-1552674605-db6ffd4facb5?w=800&auto=format&fit=crop"},
    "Page 6": {"pos": "🛡️ LB", "img": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop"},
    "Page 7": {"pos": "⚙️ CM", "img": "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&auto=format&fit=crop"},
    "Page 8": {"pos": "🛡️ CB", "img": "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&auto=format&fit=crop"},
    "Page 9": {"pos": "🚀 ST", "img": "https://images.unsplash.com/photo-1552674605-db6ffd4facb5?w=800&auto=format&fit=crop"},
    "Page 10": {"pos": "🚀 LW", "img": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop"},
}

# ==========================================
# 5. الشريط الجانبي: اللغات + الموسيقى
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/football2.png", width=80)
    selected_lang = st.selectbox("🌐 Language / اللغة", list(LANG_DATA.keys()))
    tx = LANG_DATA[selected_lang]
    
    st.markdown("---")
    st.markdown(f"### {tx['audio_label']}")
    track = st.radio("", ["🏆 Champions League", "🔊 Stadium Anthem"], label_visibility="collapsed")
    audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" if "Champions" in track else "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
    st.audio(audio_url, format="audio/mp3")
    
    st.markdown("---")
    st.info("💡 **Omnia DeepArena 2030:** منصة كروية متكاملة.")

# ==========================================
# 6. دالة عرض صفحة اللاعب
# ==========================================
def show_player_page(page_id):
    data = PLAYERS_DATA[page_id]
    
    st.markdown(f"<h1>{data['pos']} - {page_id}</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(data['img'], use_container_width=True)
    with col2:
        st.markdown(f"""
        <div class="glass-card">
            <h3 style="color: #00ff88; margin-top:0;">{tx['stats_title']}</h3>
            <ul style="color: #fff;">
                <li>88% • 91% • 10.5 km • 34.2 km/h</li>
                <li>Pass Accuracy: 91%</li>
                <li>Tactical Rating: 88%</li>
            </ul>
        </div>
        <div class="glass-card">
            <h3 style="color: #00ff88; margin-top:0;">{tx['plan_title']}</h3>
            <p style="color: #fff;">Tactical positioning and fast decision-making.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button(tx['back'], use_container_width=True):
        st.session_state.page = "main"
        st.rerun()

# ==========================================
# 7. دالة عرض الملعب + الباقات (حارس المرمى)
# ==========================================
def show_tactical_board():
    st.markdown(f"<h1>{tx['title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#ccc; font-size:11px;'>{tx['subtitle']}</p>", unsafe_allow_html=True)
    
    st.markdown('<div class="pitch-container">', unsafe_allow_html=True)
    
    # --- خط الهجوم ---
    st.markdown(f"<h3>{tx['attack']}</h3>", unsafe_allow_html=True)
    atk_cols = st.columns(3)
    with atk_cols[0]:
        if st.button(f"🚀 LW\nPage 10", key="btn_p10", use_container_width=True):
            st.session_state.page = "Page 10"; st.rerun()
    with atk_cols[1]:
        if st.button(f"🚀 ST\nPage 9", key="btn_p9", use_container_width=True):
            st.session_state.page = "Page 9"; st.rerun()
    with atk_cols[2]:
        if st.button(f"🚀 RW\nPage 5", key="btn_p5", use_container_width=True):
            st.session_state.page = "Page 5"; st.rerun()
    
    # --- خط الوسط ---
    st.markdown(f"<h3>{tx['midfield']}</h3>", unsafe_allow_html=True)
    mid_cols = st.columns(4)
    with mid_cols[0]:
        if st.button(f"⚙️ CM\nPage 4", key="btn_p4", use_container_width=True):
            st.session_state.page = "Page 4"; st.rerun()
    with mid_cols[1]:
        if st.button(f"⚙️ CM\nPage 7", key="btn_p7", use_container_width=True):
            st.session_state.page = "Page 7"; st.rerun()
    with mid_cols[2]:
        if st.button(f"⚙️ CM\nPage 11", key="btn_p11", use_container_width=True):
            st.session_state.page = "Page 4"; st.rerun()
    with mid_cols[3]:
        if st.button(f"⚙️ DM\nPage 3", key="btn_p3", use_container_width=True):
            st.session_state.page = "Page 3"; st.rerun()

    # --- خط الدفاع ---
    st.markdown(f"<h3>{tx['defense']}</h3>", unsafe_allow_html=True)
    def_cols = st.columns(4)
    with def_cols[0]:
        if st.button(f"🛡️ LB\nPage 6", key="btn_p6", use_container_width=True):
            st.session_state.page = "Page 6"; st.rerun()
    with def_cols[1]:
        if st.button(f"🛡️ CB\nPage 8", key="btn_p8", use_container_width=True):
            st.session_state.page = "Page 8"; st.rerun()
    with def_cols[2]:
        if st.button(f"🛡️ CB\nPage 2", key="btn_p2", use_container_width=True):
            st.session_state.page = "Page 2"; st.rerun()
    with def_cols[3]:
        if st.button(f"🛡️ RB\nPage 1", key="btn_p1", use_container_width=True):
            st.session_state.page = "Page 1"; st.rerun()

    # --- حارس المرمى ---
    st.markdown(f"<h3 style='color:#ffaa00;'>{tx['gk']}</h3>", unsafe_allow_html=True)
    gk_col = st.columns([1, 1, 1])
    with gk_col[1]:
        st.markdown('<div class="gk-btn">', unsafe_allow_html=True)
        st.button(f"🧤 GK\n{tx['gk_you']}", key="main_app", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    
    # ==========================================
    # 🎁 الباقات داخل حارس المرمى (Page الرئيسية)
    # ==========================================
    st.markdown("---")
    st.markdown(f"### {tx['packages_title']}")
    
    pk1, pk2, pk3 = st.columns(3)
    with pk1:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:30px;">👶</span><p style="color:#fff; margin:5px 0;">{tx["p1"]}</p></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:30px;">🏃</span><p style="color:#fff; margin:5px 0;">{tx["p2"]}</p></div>', unsafe_allow_html=True)
    with pk2:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:30px;">🔍</span><p style="color:#fff; margin:5px 0;">{tx["p3"]}</p></div>', unsafe_allow_html=True)
        # باقة VIP 150$
        st.markdown(f'<div class="vip-card"><span style="font-size:30px;">🏆</span><p style="color:#ffaa00; margin:5px 0; font-weight:bold;">{tx["p4"]}</p></div>', unsafe_allow_html=True)
    with pk3:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:30px;">⚽</span><p style="color:#fff; margin:5px 0;">{tx["p5"]}</p></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:30px;">👑</span><p style="color:#fff; margin:5px 0;">{tx["p6"]}</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.success("✅ Omnia DeepArena 2030 • Ready")

# ==========================================
# 8. إدارة الحالة
# ==========================================
def main():
    if "page" not in st.session_state:
        st.session_state.page = "main"
        
    if st.session_state.page == "main":
        show_tactical_board()
    else:
        show_player_page(st.session_state.page)

if __name__ == "__main__":
    main()
