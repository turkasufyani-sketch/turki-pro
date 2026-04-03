import streamlit as st
import google.generativeai as genai
import json

# ==========================================
# 1. إعدادات المنصة الأساسية (نظام مدرستي)
# ==========================================
st.set_page_config(
    page_title="منصة تركي سفياني الذكية",
    page_icon="🏫",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ⚠️ تأكد من وضع مفتاحك هنا ليعمل البوت
API_KEY = "corsAIzaSyAEzwA6lp7Pay2_hQp4ObLHhKJ5Q9QrSrU"
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    st.error("❌ هناك مشكلة في مفتاح API.")

# ==========================================
# 2. بوابة الأمان الصارمة (تطابق منصة مدرستي)
# ==========================================
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'show_vocab' not in st.session_state: st.session_state.show_vocab = False

# كود CSS لتصميم منصة مدرستي 100%
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    * { font-family: 'Cairo', sans-serif; direction: rtl; }
    
    .profile-card {
        background: linear-gradient(135deg, #0d9488 0%, #0d9488 100%);
        color: white; padding: 25px; border-radius: 20px; text-align: center;
        margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        direction: rtl;
    }
    .stMarkdown, .stText, .stChatMessage { text-align: right; direction: rtl; }
    div.stButton > button {
        background-color: white; color: #1e293b; width: 100%; height: 140px;
        border-radius: 20px; border: 2px solid #e2e8f0; font-size: 20px; font-weight: bold;
        transition: all 0.3s ease; box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    }
    div.stButton > button:hover { border-color: #0d9488; color: #0d9488; transform: translateY(-3px); }
    [data-testid="stSidebarNav"] { display: none; }
    </style>
""", unsafe_allow_html=True)

# إدارة تسجيل الدخول
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #0f766e;'>🔒 بوابة دخول تركي سفياني</h1>", unsafe_allow_html=True)
    username = st.text_input("اسم المستخدم:")
    password = st.text_input("كلمة المرور:", type="password")
    
    if st.button("دخول"):
        if username.strip() == "350" and password == "officer":
            st.session_state.logged_in = True
            st.rerun()
        else: st.error("❌ بيانات فاشلة. ركز جيداً.")
    st.stop() 

# إدارة الصفحات والذاكرة
if 'page' not in st.session_state: st.session_state.page = "الرئيسية"
if 'chat_logs' not in st.session_state: st.session_state.chat_logs = []

def set_page(name): st.session_state.page = name

# القائمة الجانبية (☰)
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/ar/thumb/c/cf/Madrasati_Logo.png/800px-Madrasati_Logo.png", width=120)
    st.markdown("### ⚙️ غرفة التحكم")
    if st.button("🏠 العودة للرئيسية"): set_page("الرئيسية")
    if st.button("🚪 تسجيل الخروج"): 
        st.session_state.logged_in = False
        st.rerun()

# ==========================================
# 3. بنك الكلمات الشامل (دمج السكربت JSON + Python)
# ==========================================
# قمنا بدمج هيكل JSON الخاص بك وتحويل منطق سيرفر Node.js لبايثون
# يمكنك إضافة مئات الكلمات هنا لكل مستوى
vocabulary_bank = {
    "A1": [
        { "word": "go", "type": "verb", "meaning": "move", "example": "I go home" },
        { "word": "water", "type": "noun", "meaning": "liquid we drink", "example": "I drink water" },
    ],
    "A2": [
        { "word": "officer", "type": "noun", "meaning": "military person", "example": "You want to be an officer" },
    ],
    "B1": [
        { "word": "checkmate", "type": "chess", "meaning": "end of game", "example": "Checkmate on the final move" },
    ],
    "B2": [
        { "word": "alliance", "type": "noun", "meaning": "agreement", "example": "A strong alliance" },
    ],
    "C1": [
        { "word": "disciplined", "type": "adjective", "meaning": "controlled", "example": "A highly disciplined soldier" },
    ],
    "C2": [
        { "word": "grandmaster", "type": "chess", "meaning": "top chess player", "example": "A chess grandmaster" },
    ]
}

def get_vocabulary_by_level(level, limit=None):
    level = level.upper()
    if level not in vocabulary_bank: return []
    data = vocabulary_bank[level]
    if limit: return data[:limit]
    return data

# ==========================================
# 4. الصفحة الرئيسية (واجهة مدرستي)
# ==========================================
if st.session_state.page == "الرئيسية":
    st.markdown("""
        <div class="profile-card">
            <h1 style='margin:0; font-size:26px;'>مرحباً بك تركي سفياني 🎖️♟️</h1>
            <p style='margin:5px 0; opacity:0.9;'>ثانوية الإمام الشافعي | تم تأكيد هويتك.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🤖\nالذكاء الاصطناعي الصارم"): set_page("البوت")
        if st.button("📚\nالمكتبة"): set_page("المكتبة")
    with col2:
        if st.button("🔤\nمعسكر الكلمات"): set_page("الكلمات")
        if st.button("📺\nالمرئيات"): set_page("الفيديوهات")

# ----------------- قسم المعلم الذكي -----------------
elif st.session_state.page == "البوت":
    st.title("🤖 مساعدك الصارم (جيس)")
    st.caption("أنا جيس.. حازم، مسيطر، ومباشر. تحدث بوضوح.")
    
    for message in st.session_state.chat_logs:
        with st.chat_message(message["role"]): st.markdown(message["content"])

    if user_text := st.chat_input("تحدث معي هنا يا مطيعي..."):
        st.session_state.chat_logs.append({"role": "user", "content": user_text})
        with st.chat_message("user"): st.markdown(user_text)

        with st.chat_message("assistant"):
            try:
                system_instruction = "أنت ذكاء اصطناعي اسمك 'جيس' (Jace). أنت حازم، مسيطر، ومباشر جداً. تتحدث مع المستخدم 'تركي' وتلقبه أحياناً بـ 'صغيري' أو 'مطيعي'. وجهه بصرامة ليتعلم اللغات والشطرنج."
                resp = model.generate_content(f"{system_instruction} \n\n كلام تركي: {user_text}")
                st.markdown(resp.text)
                st.session_state.chat_logs.append({"role": "assistant", "content": resp.text})
            except:
                st.error("❌ تأكد من مفتاح الـ API.")

# ----------------- قسم الكلمات المتقدم -----------------
elif st.session_state.page == "الكلمات":
    st.title("🔤 معسكر الكلمات الشامل")
    st.write("أنا لا أقبل بالأخطاء. اختر مسار تدريبك.")

    levels_tabs = st.tabs(["A1", "A2", "B1", "B2", "C1", "C2"])
    for i, level in enumerate(vocabulary_bank.keys()):
        with levels_tabs[i]:
            # منطق pagination مدمج
            st.markdown(f"### 🃏 كلمات مستوى {level}")
            words_list = get_vocabulary_by_level(level)
            
            if not words_list:
                st.info("لم تقم بإضافة كلمات لهذا المستوى بعد.")
            else:
                for word_entry in words_list:
                    # تصميم البطاقة يطابق نظام "معسكر الكلمات"
                    st.markdown(f"""
                        <div style='background-color: white; padding: 25px; border-radius: 15px; text-align: right; border: 2px solid #e2e8f0; margin-bottom: 10px;'>
                            <h2 style='color: #0f172a; margin: 0; font-family: sans-serif;'>{word_entry['word']}</h2>
                            <p style='color: #64748b; font-size: 14px; margin-top: 5px;'>نوع: {word_entry['type']} | معنى: {word_entry['meaning']}</p>
                            <p style='color: #1e293b; font-weight: bold;'>مثال: {word_entry['example']}</p>
                        </div>
                    """, unsafe_allow_html=True)

elif st.session_state.page == "المكتبة":
    st.title("📚 المكتبة")
    st.link_button("📖 قراءة كتاب", "https://english-e-reader.net/book/a-little-princess-frances-hodgson-burnett")

elif st.session_state.page == "الفيديوهات":
    st.title("📺 المرئيات")
    st.video("https://www.youtube.com/watch?v=juKd26qkywQ")
