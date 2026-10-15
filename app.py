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
# 2. تصميم الملعب التكتيكي والبطاقات (CSS)
# ==========================================
st.markdown("""
<style>
    /* خلفية الملعب الأخضر */
    .stApp {
        background: linear-gradient(180deg, #1b5e20 0%, #2e7d32 50%, #1b5e20 100%);
        background-attachment: fixed;
        color: #ffffff;
    }
    
    /* خطوط الملعب */
    .pitch-container {
        background: repeating-linear-gradient(0deg, transparent, transparent 50px, rgba(255,255,255,0.05) 50px, rgba(255,255,255,0.05) 100px);
        border: 3px solid rgba(255, 255, 255, 0.6);
        border-radius: 15px;
        padding: 20px;
        margin: 20px auto;
        max-width: 1000px;
        box-shadow: 0 0 30px rgba(0,0,0,0.5);
    }
    
    /* تنسيق أزرار اللاعبين (البطاقات الزجاجية) */
    div.stButton > button {
        background: rgba(0, 0, 0, 0.6) !important;
        backdrop-filter: blur(10px) !important;
        border: 2px solid #00ff88 !important;
        border-radius: 15px !important;
        color: #ffffff !important;
        padding: 15px 5px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(0, 255, 136, 0.2) !important;
        width: 100% !important;
        white-space: pre-wrap !important;
    }
    div.stButton > button:hover {
        transform: scale(1.05) !important;
        border-color: #ffaa00 !important;
        box-shadow: 0 0 25px rgba(255, 170, 0, 0.6) !important;
        color: #ffaa00 !important;
    }
    
    /* بطاقة حارس المرمى */
    .gk-btn div.stButton > button {
        background: rgba(255, 170, 0, 0.2) !important;
        border: 3px solid #ffaa00 !important;
        box-shadow: 0 0 30px rgba(255, 170, 0, 0.8) !important;
    }

    h1, h2, h3 { color: #ffffff !important; text-align: center; text-shadow: 0 0 10px rgba(0, 255, 136, 0.8); }
    
    /* تصميم بطاقات الإحصائيات في صفحات اللاعبين */
    .glass-card {
        background: rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid #00ff88;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0, 255, 136, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. بيانات اللاعبين (الـ 10 صفحات + الرئيسية)
# ==========================================
PLAYERS_DATA = {
    "Page 1": {"pos": "🛡️ RB", "name": "الظهير الأيمن", "desc": "تحليل الأداء الدفاعي، العرضيات، والالتحامات في الجهة اليمنى.", "img": "https://images.unsplash.com/photo-1552674605-db6ffd4facb5?w=800&auto=format&fit=crop"},
    "Page 2": {"pos": "🛡️ CB", "name": "قلب دفاع (أيمن)", "desc": "الصلابة الدفاعية، التشتيت، وبناء اللعب من الخلف.", "img": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop"},
    "Page 3": {"pos": "⚙️ DM", "name": "الوسط المدافع", "desc": "قطع الكرات، الاعتراض، وحماية خط الدفاع.", "img": "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&auto=format&fit=crop"},
    "Page 4": {"pos": "⚙️ CM", "name": "وسط ميدان (هجومي)", "desc": "الرؤية، التمريرات البينية، والتحكم في الإيقاع.", "img": "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&auto=format&fit=crop"},
    "Page 5": {"pos": "🚀 RW", "name": "الجناح الأيمن", "desc": "السرعة، المراوغة، والتسديد من الجهة اليمنى.", "img": "https://images.unsplash.com/photo-1552674605-db6ffd4facb5?w=800&auto=format&fit=crop"},
    "Page 6": {"pos": "🛡️ LB", "name": "الظهير الأيسر", "desc": "الدعم الهجومي والدفاعي في الجهة اليسرى.", "img": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop"},
    "Page 7": {"pos": "⚙️ CM", "name": "وسط ميدان (مدافع)", "desc": "التوازن التكتيكي والانتقال السريع بين الدفاع والهجوم.", "img": "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800&auto=format&fit=crop"},
    "Page 8": {"pos": "🛡️ CB", "name": "قلب دفاع (أيسر)", "desc": "الكرات الهوائية، التغطية، والقيادة الدفاعية.", "img": "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=800&auto=format&fit=crop"},
    "Page 9": {"pos": "🚀 ST", "name": "رأس الحربة", "desc": "إنهاء الهجمات، التمركز داخل المنطقة، والضغط العالي.", "img": "https://images.unsplash.com/photo-1552674605-db6ffd4facb5?w=800&auto=format&fit=crop"},
    "Page 10": {"pos": "🚀 LW", "name": "الجناح الأيسر", "desc": "الانطلاقات، العرضيات، والتهديد المباشر للمرمى.", "img": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&auto=format&fit=crop"},
}

# ==========================================
# 4. دالة عرض صفحة اللاعب
# ==========================================
def show_player_page(page_id):
    data = PLAYERS_DATA[page_id]
    
    st.markdown(f"<h1>{data['pos']} - {data['name']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #ccc; text-align:center; font-size: 18px;'>{data['desc']}</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(data['img'], use_container_width=True, caption=data['name'])
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color: #00ff88; margin-top:0;">📊 إحصائيات متقدمة</h3>
            <ul style="color: #fff; font-size: 16px;">
                <li>معدل الأداء التكتيكي: 88%</li>
                <li>دقة التمريرات: 91%</li>
                <li>المسافة المقطوعة: 10.5 كم</li>
                <li>السرعة القصوى: 34.2 كم/س</li>
            </ul>
            <p style="font-size: 12px; color: #888;">* هذه البيانات تجريبية لغرض العرض التكتيكي.</p>
        </div>
        <div class="glass-card">
            <h3 style="color: #00ff88; margin-top:0;">🎯 خطة التطوير</h3>
            <p style="color: #fff;">تحسين التمركز واتخاذ القرارات السريعة تحت الضغط التكتيكي.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    # زر العودة إلى الملعب (حارس المرمى)
    if st.button("⬅️ العودة إلى الملعب التكتيكي (GK)", use_container_width=True):
        st.session_state.page = "main"
        st.rerun()

# ==========================================
# 5. دالة عرض الملعب التكتيكي (حارس المرمى)
# ==========================================
def show_tactical_board():
    st.markdown("<h1>🏟️ Omnia Football Arena 2030</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ccc;'>انقر على أي لاعب للانتقال إلى صفحته الخاصة. الصفحة الرئيسية هي حارس المرمى.</p>", unsafe_allow_html=True)
    
    st.markdown('<div class="pitch-container">', unsafe_allow_html=True)
    
    # --- خط الهجوم (3 لاعبين) ---
    st.markdown("<h3>⚔️ خط الهجوم</h3>", unsafe_allow_html=True)
    atk_cols = st.columns(3)
    with atk_cols[0]:
        if st.button("🚀 LW\nالجناح الأيسر\n(Page 10)", key="btn_p10", use_container_width=True):
            st.session_state.page = "Page 10"; st.rerun()
    with atk_cols[1]:
        if st.button("🚀 ST\nرأس الحربة\n(Page 9)", key="btn_p9", use_container_width=True):
            st.session_state.page = "Page 9"; st.rerun()
    with atk_cols[2]:
        if st.button("🚀 RW\nالجناح الأيمن\n(Page 5)", key="btn_p5", use_container_width=True):
            st.session_state.page = "Page 5"; st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- خط الوسط (3 لاعبين) ---
    st.markdown("<h3>⚙️ خط الوسط</h3>", unsafe_allow_html=True)
    mid_cols = st.columns(3)
    with mid_cols[0]:
        if st.button("⚙️ CM\nوسط (هجومي)\n(Page 4)", key="btn_p4", use_container_width=True):
            st.session_state.page = "Page 4"; st.rerun()
    with mid_cols[1]:
        if st.button("⚙️ CM\nوسط (مدافع)\n(Page 7)", key="btn_p7", use_container_width=True):
            st.session_state.page = "Page 7"; st.rerun()
    with mid_cols[2]:
        if st.button("⚙️ DM\nوسط مدافع\n(Page 3)", key="btn_p3", use_container_width=True):
            st.session_state.page = "Page 3"; st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # --- خط الدفاع (4 لاعبين) ---
    st.markdown("<h3>🛡️ خط الدفاع</h3>", unsafe_allow_html=True)
    def_cols = st.columns(4)
    with def_cols[0]:
        if st.button("🛡️ LB\nظهير أيسر\n(Page 6)", key="btn_p6", use_container_width=True):
            st.session_state.page = "Page 6"; st.rerun()
    with def_cols[1]:
        if st.button("🛡️ CB\nقلب دفاع (أيسر)\n(Page 8)", key="btn_p8", use_container_width=True):
            st.session_state.page = "Page 8"; st.rerun()
    with def_cols[2]:
        if st.button("🛡️ CB\nقلب دفاع (أيمن)\n(Page 2)", key="btn_p2", use_container_width=True):
            st.session_state.page = "Page 2"; st.rerun()
    with def_cols[3]:
        if st.button("🛡️ RB\nظهير أيمن\n(Page 1)", key="btn_p1", use_container_width=True):
            st.session_state.page = "Page 1"; st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # --- حارس المرمى (الصفحة الرئيسية app.py) ---
    st.markdown("<h3 style='color:#ffaa00;'>🧤 حارس المرمى (الصفحة الرئيسية)</h3>", unsafe_allow_html=True)
    gk_col = st.columns([1, 2, 1])
    with gk_col[1]:
        st.markdown('<div class="gk-btn">', unsafe_allow_html=True)
        st.button("🧤 GK\napp.py\nأنت هنا الآن", key="main_app", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.success("✅ **جاهز:** انقر على أي لاعب لفتح صفحته. الكود يعمل بملف واحد فقط!")

# ==========================================
# 6. إدارة الحالة (State Management)
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
