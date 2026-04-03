import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة لتكون مثل تطبيق الجوال
st.set_page_config(page_title="منصة تركي سفياني", page_icon="🏫", layout="centered")

# ⚠️ ضع مفتاحك السري هنا بين علامتي التنصيص
API_KEY = "AIzaSyAI1y3ZcK1RgCICJKuF3ACrkPcAYzUb6GM"
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
except:
    pass

# كود CSS لجعل الأزرار مربعة وكبيرة مثل منصة "مدرستي"
st.markdown("""
    <style>
    div.stButton > button {
        background-color: white;
        color: #1f2937;
        width: 100%;
        height: 120px;
        border-radius: 15px;
        border: 2px solid #e5e7eb;
        font-size: 22px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        border-color: #10b981; /* لون أخضر مثل مدرستي */
        color: #10b981;
    }
    </style>
""", unsafe_allow_html=True)

# نظام التنقل بين الصفحات (بدون قائمة جانبية)
if 'page' not in st.session_state:
    st.session_state.page = "الرئيسية"

def go_to(page_name):
    st.session_state.page = page_name

# زر العودة للرئيسية يظهر في كل الصفحات ما عدا الرئيسية
if st.session_state.page != "الرئيسية":
    st.button("🏠 العودة للرئيسية", on_click=go_to, args=("الرئيسية",))
    st.markdown("---")

# ==========================================
# 1. الصفحة الرئيسية (واجهة مدرستي)
# ==========================================
if st.session_state.page == "الرئيسية":
    st.markdown("<h2 style='text-align: center; color: #0d9488;'>مرحباً بك تركي عبدالله سفياني 🏫</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>ثانوية الإمام الشافعي بالعارضة - مسارات | الصف أول ثانوي أ</p>", unsafe_allow_html=True)
    st.write("")
    
    # تقسيم الأزرار مثل مدرستي
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🤖\nالبوت الذكي"): go_to("البوت الذكي")
        st.write("")
        if st.button("📚\nمكتبة الروايات"): go_to("مكتبة الروايات")
    with col2:
        if st.button("🔤\nخزانة الكلمات"): go_to("خزانة الكلمات")
        st.write("")
        if st.button("📺\nالفيديوهات"): go_to("الفيديوهات")

# ==========================================
# 2. البوت الذكي (تم تطوير شكل المحادثة)
# ==========================================
elif st.session_state.page == "البوت الذكي":
    st.title("🤖 المدرس الذكي الخاص بك")
    st.info("تحدث معي بالإنجليزية لتطوير لغتك، أو اسألني عن أي قاعدة!")
    
    user_input = st.chat_input("اكتب رسالتك هنا...")
    if user_input:
        st.chat_message("user").write(user_input)
        try:
            response = model.generate_content(user_input)
            st.chat_message("assistant").write(response.text)
        except Exception as e:
            st.error("❌ البوت لا يرد! السبب: لم تقم بوضع مفتاح API صحيح في الكود، أو أن المفتاح معطل.")

# ==========================================
# 3. مكتبة الروايات (تفتح بروابط حقيقية)
# ==========================================
elif st.session_state.page == "مكتبة الروايات":
    st.title("📚 مكتبة الروايات المجانية")
    st.write("هذه الروايات تفتح مباشرة للقراءة والتدرب:")
    
    c1, c2 = st.columns(2)
    with c1:
        # صورة غلاف رواية
        st.image("https://english-e-reader.net/covers/A_Little_Princess-Frances_Hodgson_Burnett.jpg", use_container_width=True)
        st.subheader("A Little Princess")
        st.caption("المستوى: A1 - مبتدئ")
        # رابط حقيقي يفتح القصة
        st.link_button("📖 اقرأ الرواية الآن", "https://english-e-reader.net/book/a-little-princess-frances-hodgson-burnett")
        
    with c2:
        st.image("https://english-e-reader.net/covers/Sherlock_Holmes_and_the_Duke_s_Son-Arthur_Conan_Doyle.jpg", use_container_width=True)
        st.subheader("Sherlock Holmes")
        st.caption("المستوى: A1 - مبتدئ")
        st.link_button("📖 اقرأ الرواية الآن", "https://english-e-reader.net/book/sherlock-holmes-and-the-dukes-son-arthur-conan-doyle")

# ==========================================
# 4. خزانة الكلمات (جدول كلمات حقيقي)
# ==========================================
elif st.session_state.page == "خزانة الكلمات":
    st.title("🔤 خزانة الكلمات (A1 - C2)")
    
    tab1, tab2, tab3 = st.tabs(["مبتدئ A1", "أساسي A2", "متوسط B1"])
    
    with tab1:
        st.write("أهم 10 كلمات للمبتدئين:")
        # جدول كلمات حقيقي يعرض الكلمة ومعناها
        st.table({
            "الكلمة (English)": ["Accommodation", "Beautiful", "Country", "Dictionary", "Environment", "Friend", "Important", "Journey", "Knowledge", "Language"],
            "المعنى (Arabic)": ["مكان إقامة", "جميل", "دولة / ريف", "قاموس", "بيئة", "صديق", "مهم", "رحلة", "معرفة", "لغة"]
        })
    with tab2:
        st.info("قريباً: سيتم إضافة 800 كلمة خاصة بمستوى A2.")
    with tab3:
        st.info("قريباً: سيتم إضافة 4000 كلمة خاصة بمستوى B1.")

# ==========================================
# 5. الفيديوهات (روابط قنوات يوتيوب حقيقية)
# ==========================================
elif st.session_state.page == "الفيديوهات":
    st.title("📺 الدروس المرئية")
    st.write("أفضل القنوات المعتمدة لتعلم الإنجليزية:")
    
    st.video("https://www.youtube.com/watch?v=juKd26qkywQ") # فيديو يشتغل داخل الموقع
    st.link_button("📺 الذهاب لقناة BBC Learning English", "https://www.youtube.com/user/bbclearningenglish")
    st.link_button("📺 الذهاب لقناة ZAmericanEnglish", "https://www.youtube.com/c/ZAmericanEnglish")


