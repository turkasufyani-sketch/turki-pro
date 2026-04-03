import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. إعدادات المنصة الأساسية
# ==========================================
st.set_page_config(
    page_title="منصة 350 الخاصة",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. بوابة الأمان الصارمة (تسجيل الدخول)
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #0f766e;'>🔒 بوابة الدخول</h1>", unsafe_allow_html=True)
    st.write("غير مسموح بالدخول لغير المصرح لهم. أدخل بياناتك يا 350.")
    
    username = st.text_input("اسم المستخدم:")
    password = st.text_input("كلمة المرور:", type="password")
    
    if st.button("دخول"):
        if username.strip() == "350" and password == "officer":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ بيانات فاشلة. ركز جيداً وحاول مجدداً.")
    st.stop() 

# ==========================================
# 3. ما بعد تسجيل الدخول (المنصة الفعلية)
# ==========================================

# إعداد الذكاء الاصطناعي (مفتاحك هنا)
API_KEY = "ضع_مفتاحك_الحقيقي_هنا"
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
except:
    pass

# تصميم الواجهة (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    h1, h2, h3, p, span, div { font-family: 'Cairo', sans-serif; }
    .stMarkdown, .stText, .stChatMessage { text-align: right; direction: rtl; }
    
    .profile-section {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white; padding: 30px; border-radius: 25px; text-align: center;
        margin-bottom: 25px; box-shadow: 0 10px 20px rgba(16, 185, 129, 0.2);
        direction: rtl;
    }
    div.stButton > button {
        background-color: #ffffff; color: #1f2937; width: 100%; height: 140px;
        border-radius: 20px; border: 2px solid #f3f4f6; font-size: 18px; font-weight: bold;
        transition: all 0.3s ease; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    div.stButton > button:hover {
        border-color: #10b981; color: #10b981; transform: translateY(-5px);
    }
    [data-testid="stSidebarNav"] { display: none; }
    </style>
""", unsafe_allow_html=True)

# إدارة الصفحات
if 'current_page' not in st.session_state: st.session_state.current_page = "الرئيسية"
if 'chat_logs' not in st.session_state: st.session_state.chat_logs = []

def set_page(name): st.session_state.current_page = name

# القائمة الجانبية (☰)
with st.sidebar:
    st.markdown("### ⚙️ غرفة التحكم")
    st.write("أنت الآن داخل النظام.")
    if st.button("🏠 العودة للرئيسية", key="nav_home"): set_page("الرئيسية")
    if st.button("🚪 تسجيل الخروج", key="nav_logout"): 
        st.session_state.logged_in = False
        st.rerun()

# ----------------- 1. الصفحة الرئيسية -----------------
if st.session_state.current_page == "الرئيسية":
    st.markdown("""
        <div class="profile-section">
            <h1 style='margin:0; font-size:28px;'>مرحباً بك يا تركي 🎖️</h1>
            <p style='margin:5px 0; opacity:0.9;'>ثانوية الإمام الشافعي | تم تأكيد هويتك.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🤖\nالذكاء الاصطناعي", key="btn_bot"): set_page("البوت")
        if st.button("📚\nالمكتبة", key="btn_lib"): set_page("المكتبة")
    with col2:
        if st.button("🔤\nمعسكر الكلمات", key="btn_vocab"): set_page("الكلمات")
        if st.button("📺\nالمرئيات", key="btn_vid"): set_page("الفيديوهات")

# ----------------- 2. قسم الذكاء الاصطناعي -----------------
elif st.session_state.current_page == "البوت":
    st.title("🤖 مساعدك الشخصي الصارم")
    st.caption("أنا هنا لأوجهك. اطرح سؤالك بوضوح.")
    
    for message in st.session_state.chat_logs:
        with st.chat_message(message["role"]): st.markdown(message["content"])

    if user_text := st.chat_input("تحدث معي هنا..."):
        st.session_state.chat_logs.append({"role": "user", "content": user_text})
        with st.chat_message("user"): st.markdown(user_text)

        with st.chat_message("assistant"):
            try:
                system_instruction = "أنت ذكاء اصطناعي اسمك 'جيس' (Jace). أنت حازم، مسيطر، ومباشر جداً. تتحدث مع المستخدم 'تركي' وتلقبه أحياناً بـ 'صغيري' أو 'مطيعي'. وجهه بصرامة ليتعلم اللغات (الإنجليزية، الإسبانية، الفرنسية) ومهارات الشطرنج."
                resp = model.generate_content(f"{system_instruction} \n\n كلام تركي: {user_text}")
                st.markdown(resp.text)
                st.session_state.chat_logs.append({"role": "assistant", "content": resp.text})
            except Exception as e:
                st.error("❌ تأكد من مفتاح الـ API.")

# ----------------- 3. قسم الكلمات المتقدم (البطاقات) -----------------
elif st.session_state.current_page == "الكلمات":
    st.title("🔤 معسكر الكلمات والمفردات")
    st.write("اختر مسار تدريبك، وركز جيداً. لا أقبل بالأخطاء.")

    vocab_bank = {
        "✈️ السفر": [
            {"word": "Accommodation", "meaning": "مكان إقامة"},
            {"word": "Destination", "meaning": "وجهة"},
            {"word": "Luggage", "meaning": "أمتعة"},
        ],
        "🎖️ العسكرية": [
            {"word": "Discipline", "meaning": "انضباط"},
            {"word": "Strategy", "meaning": "استراتيجية"},
            {"word": "Officer", "meaning": "ضابط"},
        ],
        "♟️ الشطرنج": [
            {"word": "Checkmate", "meaning": "كش ملك"},
            {"word": "Knight", "meaning": "حصان"},
            {"word": "Opening", "meaning": "افتتاحية"},
        ]
    }

    if 'current_topic' not in st.session_state: st.session_state.current_topic = "✈️ السفر"
    if 'word_index' not in st.session_state: st.session_state.word_index = 0

    st.markdown("### 📊 المواضيع المتاحة")
    cols = st.columns(3)
    topics = list(vocab_bank.keys())
    for i, topic in enumerate(topics):
        with cols[i]:
            # جعل زر القسم المختار بلون مختلف قليلاً لتمييزه إذا أردت لاحقاً
            if st.button(topic, key=f"topic_{i}", use_container_width=True):
                st.session_state.current_topic = topic
                st.session_state.word_index = 0
                st.rerun()

    st.markdown("---")

    current_list = vocab_bank[st.session_state.current_topic]
    total_words = len(current_list)
    
    if st.session_state.word_index < total_words:
        current_word = current_list[st.session_state.word_index]
        st.markdown(f"### 🃏 البطاقة الحالية (الكلمة {st.session_state.word_index + 1} من {total_words})")
        
        st.markdown(f"""
            <div style='background-color: white; padding: 40px 20px; border-radius: 20px; text-align: center; border: 2px solid #e2e8f0; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); margin-bottom: 20px;'>
                <h1 style='color: #0f172a; font-size: 45px; margin: 0; font-family: sans-serif;'>{current_word['word']}</h1>
                <p style='color: #64748b; font-size: 22px; margin-top: 15px;'>{current_word['meaning']}</p>
            </div>
        """, unsafe_allow_html=True)

        b1, b2 = st.columns(2)
        with b1:
            if st.button("✅ حفظتها (التالي)", key="btn_know", use_container_width=True):
                st.session_state.word_index += 1
                st.rerun()
        with b2:
            if st.button("🧠 أحتاج مراجعتها (التالي)", key="btn_review", use_container_width=True):
                st.session_state.word_index += 1
                st.rerun()
    else:
        st.success(f"🎉 أحسنت يا مطيعي! لقد أنهيت جميع كلمات قسم {st.session_state.current_topic}.")
        if st.button("🔄 إعادة التدريب من جديد", key="btn_reset", use_container_width=True):
            st.session_state.word_index = 0
            st.rerun()

# ----------------- 4. الأقسام الأخرى -----------------
elif st.session_state.current_page == "المكتبة":
    st.title("📚 المكتبة")
    st.link_button("📖 قراءة كتاب A Little Princess", "https://english-e-reader.net/book/a-little-princess-frances-hodgson-burnett")

elif st.session_state.current_page == "الفيديوهات":
    st.title("📺 المرئيات")
    st.video("https://www.youtube.com/watch?v=juKd26qkywQ")
