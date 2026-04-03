import streamlit as st
import google.generativeai as genai

# 1. إعدادات المنصة (نظام مدرستي المتطور)
st.set_page_config(
    page_title="منصة تركي سفياني الذكية",
    page_icon="🏫",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. تفعيل الذكاء الاصطناعي (تأكد من وضع مفتاحك هنا)
API_KEY = "ضع_مفتاحك_الحقيقي_هنا"
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
except:
    pass

# 3. هندسة الواجهة (CSS) - تصميم عصري مستوحى من منصة مدرستي
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    * { font-family: 'Cairo', sans-serif; direction: rtl; }
    
    .profile-section {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white; padding: 30px; border-radius: 25px; text-align: center;
        margin-bottom: 25px; box-shadow: 0 10px 20px rgba(16, 185, 129, 0.2);
    }
    .main-button-container {
        display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 20px;
    }
    div.stButton > button {
        background-color: #ffffff; color: #1f2937; width: 100%; height: 140px;
        border-radius: 20px; border: 2px solid #f3f4f6; font-size: 18px; font-weight: bold;
        transition: all 0.3s ease; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    div.stButton > button:hover {
        border-color: #10b981; color: #10b981; transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(16, 185, 129, 0.1);
    }
    /* إخفاء شريط التنقل الافتراضي */
    [data-testid="stSidebarNav"] { display: none; }
    </style>
""", unsafe_allow_html=True)

# 4. الذاكرة والتحكم (Session Management)
if 'current_page' not in st.session_state: st.session_state.current_page = "الرئيسية"
if 'chat_logs' not in st.session_state: st.session_state.chat_logs = []

def set_page(name): st.session_state.current_page = name

# القائمة الجانبية (الأنيقة)
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/ar/thumb/c/cf/Madrasati_Logo.png/800px-Madrasati_Logo.png", width=120)
    st.markdown("### 📋 بيانات الطالب")
    st.write("👤 **الاسم:** تركي عبدالله سفياني")
    st.write("🏫 **المدرسة:** الإمام الشافعي بالعارضة")
    st.write("📚 **المسار:** أول ثانوي - مسارات")
    st.markdown("---")
    if st.button("🏠 العودة للرئيسية"): set_page("الرئيسية")

# ==========================================
# الصفحة الرئيسية (Dashboard)
# ==========================================
if st.session_state.current_page == "الرئيسية":
    st.markdown("""
        <div class="profile-section">
            <h1 style='margin:0; font-size:28px;'>مرحباً بك يا تركي 🎖️</h1>
            <p style='margin:5px 0; opacity:0.9;'>نظام التعلم الذكي المتكامل | ثانوية الإمام الشافعي</p>
            <div style='margin-top:15px;'>
                <span style='background:rgba(255,255,255,0.2); padding:5px 15px; border-radius:20px; font-size:13px;'>♟️ محترف شطرنج</span>
                <span style='background:rgba(255,255,255,0.2); padding:5px 15px; border-radius:20px; font-size:13px; margin-right:5px;'>🇸🇦 مستقبل عسكري</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🤖\nالمعلم الذكي"): set_page("البوت")
        if st.button("📚\nالمقررات والكتب"): set_page("المكتبة")
    with col2:
        if st.button("🔤\nخزانة الكلمات"): set_page("الكلمات")
        if st.button("📺\nالفيديوهات"): set_page("الفيديوهات")

# ==========================================
# قسم المعلم الذكي (بذاكرة مستمرة)
# ==========================================
elif st.session_state.current_page == "البوت":
    st.title("🤖 المعلم الذكي")
    st.caption("أنا أتذكر سياق حديثنا.. تحدث معي بالإسكليزية، الإسبانية، أو الفرنسية.")
    
    for message in st.session_state.chat_logs:
        with st.chat_message(message["role"]): st.markdown(message["content"])

    if user_text := st.chat_input("تحدث مع معلمك..."):
        st.session_state.chat_logs.append({"role": "user", "content": user_text})
        with st.chat_message("user"): st.markdown(user_text)

        with st.chat_message("assistant"):
            try:
                system_instruction = "أنت معلم لغات ذكي في منصة الطالب تركي سفياني. كن محفزاً وساعده في لغاته الثلاث وشطرنج وطموحه العسكري."
                resp = model.generate_content(f"{system_instruction} | {user_text}")
                st.markdown(resp.text)
                st.session_state.chat_logs.append({"role": "assistant", "content": resp.text})
            except:
                st.error("❌ عذراً، تأكد من تحديث مفتاح API في الكود.")

# ==========================================
# خزانة الكلمات (التطوير الشامل)
# ==========================================
elif st.session_state.current_page == "الكلمات":
    st.title("🔤 بنك المفردات اللغوية")
    t1, t2, t3 = st.tabs(["🇬🇧 English", "🇪🇸 Español", "🇫🇷 Français"])
    
    with t1:
        st.subheader("📚 كلمات مختارة بعناية")
        st.table({
            "المجال": ["عسكري 🎖️", "شطرنج ♟️", "المنهج 📖"],
            "الكلمة (English)": ["Leadership", "Grandmaster", "Environment"],
            "المعنى (عربي)": ["القيادة", "أستاذ كبير", "البيئة"]
        })

    with t2:
        st.subheader("🇪🇸 المصطلحات الإسبانية")
        st.table({"Palabra": ["Hola", "Ajedrez", "Victoria"], "Traducción": ["مرحباً", "شطرنج", "نصر"]})

    with t3:
        st.subheader("🇫🇷 المصطلحات الفرنسية")
        st.table({"Mot": ["Bonjour", "Officier", "Échecs"], "Traduction": ["صباح الخير", "ضابط", "شطرنج"]})

# ==========================================
# المكتبة الرقمية
# ==========================================
elif st.session_state.current_page == "المكتبة":
    st.title("📚 المكتبة الرقمية")
    st.write("روايات مختارة لتطوير مستواك:")
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://english-e-reader.net/covers/A_Little_Princess-Frances_Hodgson_Burnett.jpg")
        st.link_button("📖 قراءة (A1)", "https://english-e-reader.net/book/a-little-princess-frances-hodgson-burnett")
    with c2:
        st.image("https://english-e-reader.net/covers/Sherlock_Holmes_and_the_Duke_s_Son-Arthur_Conan_Doyle.jpg")
        st.link_button("📖 قراءة (A1)", "https://english-e-reader.net/book/sherlock-holmes-and-the-dukes-son-arthur-conan-doyle")

# ==========================================
# الفيديوهات
# ==========================================
elif st.session_state.current_page == "الفيديوهات":
    st.title("📺 الدروس المرئية")
    st.video("https://www.youtube.com/watch?v=juKd26qkywQ")
    st.link_button("📺 قناة BBC Learning English", "https://www.youtube.com/user/bbclearningenglish")
