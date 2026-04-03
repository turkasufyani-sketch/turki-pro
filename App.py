import streamlit as st
import google.generativeai as genai

# 1. إعدادات الصفحة (إخفاء القائمة الجانبية في البداية لتشبه التطبيق)
st.set_page_config(page_title="منصة تركي سفياني | مدرستي", page_icon="🏫", layout="centered", initial_sidebar_state="collapsed")

# 2. ربط الذكاء الاصطناعي (ضع مفتاحك السري هنا)
API_KEY = "AIzaSyAI1y3ZcK1RgCICJKuF3ACrkPcAYzUb6GM"
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
except:
    pass

# 3. تصميم واجهة "مدرستي" باستخدام CSS
st.markdown("""
    <style>
    .main-card {
        background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 20px;
        padding: 25px; text-align: center; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .user-name { color: #0f172a; font-weight: bold; font-size: 26px; margin-bottom: 5px; }
    .school-info { color: #64748b; font-size: 16px; margin-bottom: 15px; }
    .status-badge {
        background-color: #f1f5f9; border: 1px solid #cbd5e1; padding: 6px 18px;
        border-radius: 25px; display: inline-block; font-size: 14px; color: #475569; margin: 4px;
    }
    div.stButton > button {
        background-color: white; color: #1e293b; width: 100%; height: 140px;
        border-radius: 20px; border: 2px solid #e2e8f0; font-size: 20px; font-weight: bold;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03); transition: all 0.3s ease;
    }
    div.stButton > button:hover { border-color: #0d9488; color: #0d9488; transform: translateY(-4px); }
    </style>
""", unsafe_allow_html=True)

# 4. نظام الذاكرة والتنقل
if 'page' not in st.session_state: st.session_state.page = "الرئيسية"
if 'messages' not in st.session_state: st.session_state.messages = []

def navigate(page): st.session_state.page = page

# القائمة الجانبية (الثلاث نقاط ☰)
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/ar/thumb/c/cf/Madrasati_Logo.png/800px-Madrasati_Logo.png", width=150)
    st.markdown("---")
    st.write("👤 **الحساب:** تركي عبدالله سفياني")
    st.write("📡 **الحالة:** متصل")
    if st.button("🏠 العودة للرئيسية"): navigate("الرئيسية")

# ==========================================
# الصفحة الرئيسية (Dashboard)
# ==========================================
if st.session_state.page == "الرئيسية":
    st.markdown("""
        <div class="main-card">
            <div class="user-name">مرحباً بك تركي عبدالله سفياني</div>
            <div class="school-info">ثانوية الإمام الشافعي بالعارضة - مسارات</div>
            <div class="status-badge">👨‍🎓 أول ثانوي أ</div>
            <div class="status-badge">🎖️ مستقبل عسكري</div>
            <div class="status-badge">♟️ محترف شطرنج</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🤖\nالمعلم الذكي"): navigate("البوت")
        st.write("")
        if st.button("📚\nالمكتبة الرقمية"): navigate("المكتبة")
    with col2:
        if st.button("🔤\nخزانة الكلمات"): navigate("الكلمات")
        st.write("")
        if st.button("📺\nالفيديوهات التعليمية"): navigate("الفيديوهات")

# ==========================================
# قسم البوت (بذاكرة كاملة)
# ==========================================
elif st.session_state.page == "البوت":
    st.title("🤖 المعلم الذكي (ذاكرة مفعلة)")
    st.info("سأقوم بتصحيح لغتك وتذكر محادثتنا.")
    
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("اكتب سؤالك هنا...")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        try:
            prompt = f"أنت معلم لغات خبير في منصة الطالب تركي سفياني. صحح أخطاءه وشجعه: {user_input}"
            response = model.generate_content(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            st.chat_message("assistant").write(response.text)
        except: st.error("❌ تأكد من صحة مفتاح API")

# ==========================================
# خزانة الكلمات (اللغات الثلاث + تخصصاتك)
# ==========================================
elif st.session_state.page == "الكلمات":
    st.title("🔤 خزانة الكلمات الشاملة")
    l_tabs = st.tabs(["🇬🇧 English", "🇪🇸 Español", "🇫🇷 Français"])
    
    with l_tabs[0]:
        sub = st.tabs(["🎖️ عسكري", "♟️ شطرنج", "📚 مدرسي"])
        with sub[0]: st.table({"الكلمة": ["Rank", "Officer", "Discipline"], "المعنى": ["رتبة", "ضابط", "انضباط"]})
        with sub[1]: st.table({"الكلمة": ["Tactics", "Opening", "Draw"], "المعنى": ["تكتيكات", "افتتاحية", "تعادل"]})
        with sub[2]: st.table({"الكلمة": ["Environment", "Linguistic", "Competencies"], "المعنى": ["بيئة", "لغوي", "كفايات"]})

    with l_tabs[1]:
        st.table({"الإسبانية": ["Hola", "Victoria", "Ajedrez"], "المعنى": ["مرحباً", "نصر", "شطرنج"]})
    
    with l_tabs[2]:
        st.table({"الفرنسية": ["Bonjour", "Officier", "Échecs"], "المعنى": ["صباح الخير", "ضابط", "شطرنج"]})

# ==========================================
# المكتبة الرقمية
# ==========================================
elif st.session_state.page == "المكتبة":
    st.title("📚 المكتبة الرقمية (A1 - C2)")
    st.write("روايات مختارة لرفع مستواك:")
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://english-e-reader.net/covers/A_Little_Princess-Frances_Hodgson_Burnett.jpg")
        st.link_button("📖 قراءة A Little Princess", "https://english-e-reader.net/book/a-little-princess-frances-hodgson-burnett")
    with c2:
        st.image("https://english-e-reader.net/covers/Sherlock_Holmes_and_the_Duke_s_Son-Arthur_Conan_Doyle.jpg")
        st.link_button("📖 قراءة Sherlock Holmes", "https://english-e-reader.net/book/sherlock-holmes-and-the-dukes-son-arthur-conan-doyle")

# ==========================================
# الفيديوهات التعليمية
# ==========================================
elif st.session_state.page == "الفيديوهات":
    st.title("📺 الدروس المرئية")
    st.video("https://www.youtube.com/watch?v=juKd26qkywQ")
    st.link_button("📺 قناة BBC Learning English", "https://www.youtube.com/user/bbclearningenglish")



