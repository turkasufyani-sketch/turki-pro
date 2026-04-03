import streamlit as st
import google.generativeai as genai

# إعدادات المنصة
st.set_page_config(page_title="TURKI SUFYANI Platform", page_icon="🚀", layout="wide")

# ⚠️ ضع مفتاحك الجديد هنا
API_KEY = "AIzaSyAI1y3ZcK1RgCICJKuF3ACrkPcAYzUb6GM"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# القائمة الجانبية
with st.sidebar:
    st.title("📂 أقسام المنصة")
    choice = st.radio("انتقل إلى:", [
        "🏠 الرئيسية", 
        "🗣️ البوت الذكي", 
        "📚 مكتبة الكتب", 
        "📖 قسم القراءة", 
        "📺 فيديوهات تعليمية", 
        "🔤 خزانة الكلمات"
    ])
    st.markdown("---")
    st.info("Developed by: 350 (Turki) 🎖️")

# 1. الرئيسية
if choice == "🏠 الرئيسية":
    st.title("TURKI SUFYANI Platform 🚀")
    st.subheader("منصتك المتكاملة لإتقان الإنجليزية، الإسبانية، والفرنسية")
    st.write("اختر القسم الذي تريده من القائمة الجانبية للبدء.")

# 2. البوت الذكي
elif choice == "🗣️ البوت الذكي":
    st.title("🤖 مدرب اللغات الذكي")
    st.write("اطلب مني تصحيح القواعد، أو التدرب على محادثة بالإنجليزية، الإسبانية، أو الفرنسية.")
    user_input = st.chat_input("تحدث معي هنا...")
    if user_input:
        try:
            instruction = "أنت معلم لغات خبير متعدد اللغات. صحح الأخطاء بدقة واشرح القواعد إذا لزم الأمر: "
            response = model.generate_content(instruction + user_input)
            st.success(response.text)
        except Exception as e:
            st.error("⚠️ عذراً، تأكد من وضع مفتاح API صحيح.")

# 3. مكتبة الكتب
elif choice == "📚 مكتبة الكتب":
    st.title("📚 المكتبة الرقمية")
    lang = st.radio("اختر اللغة:", ["🇬🇧 الإنجليزية", "🇪🇸 الإسبانية", "🇫🇷 الفرنسية"], horizontal=True)
    
    tabs = st.tabs(["A1", "A2", "B1", "B2", "C1", "C2"])
    if lang == "🇬🇧 الإنجليزية":
        with tabs[0]: st.button("📖 تحميل كتب الإنجليزية A1")
        with tabs[3]: st.button("📖 تحميل كتب الإنجليزية B2")
    elif lang == "🇪🇸 الإسبانية":
        with tabs[0]: st.button("📖 تحميل كتب الإسبانية A1")
        with tabs[3]: st.button("📖 تحميل كتب الإسبانية B2")
    else:
        with tabs[0]: st.button("📖 تحميل كتب الفرنسية A1")
        with tabs[3]: st.button("📖 تحميل كتب الفرنسية B2")

# 4. قسم القراءة
elif choice == "📖 قسم القراءة":
    st.title("📖 تدريبات القراءة")
    lang = st.radio("اختر اللغة:", ["🇬🇧 الإنجليزية", "🇪🇸 الإسبانية", "🇫🇷 الفرنسية"], horizontal=True)
    
    tabs = st.tabs(["A1", "A2", "B1", "B2", "C1", "C2"])
    if lang == "🇬🇧 الإنجليزية":
        with tabs[0]: st.info("Hello! My name is Turki. I am a student. (English A1)")
    elif lang == "🇪🇸 الإسبانية":
        with tabs[0]: st.info("¡Hola! Me llamo Turki. Soy estudiante. (Español A1)")
    else:
        with tabs[0]: st.info("Bonjour ! Je m'appelle Turki. Je suis étudiant. (Français A1)")
        with tabs[3]: st.info("Le développement rapide de la technologie a changé nos vies. (Français B2)")

# 5. فيديوهات تعليمية
elif choice == "📺 فيديوهات تعليمية":
    st.title("📺 مكتبة المرئيات")
    lang = st.radio("اختر اللغة:", ["🇬🇧 الإنجليزية", "🇪🇸 الإسبانية", "🇫🇷 الفرنسية"], horizontal=True)
    
    if lang == "🇬🇧 الإنجليزية":
        st.subheader("مصادر اللغة الإنجليزية")
        st.markdown("- [BBC Learning English](https://www.bbc.co.uk/learningenglish/)")
    elif lang == "🇪🇸 الإسبانية":
        st.subheader("مصادر اللغة الإسبانية")
        st.markdown("- [Dreaming Spanish](https://www.dreamingspanish.com/)")
    else:
        st.subheader("مصادر اللغة الفرنسية")
        st.markdown("- [TV5MONDE - Apprendre le français](https://apprendre.tv5monde.com/)")
        st.markdown("- [Français avec Pierre (YouTube)](https://www.youtube.com/c/FrancaisavecPierre)")

# 6. خزانة الكلمات
elif choice == "🔤 خزانة الكلمات":
    st.title("🔤 بنك المفردات (Vocabulary Target)")
    lang = st.radio("اختر المسار:", ["🇬🇧 الإنجليزية", "🇪🇸 الإسبانية", "🇫🇷 الفرنسية"], horizontal=True)
    
    st.write(f"**أهدافك في {lang}:**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="مستوى A1", value="1,500 كلمة")
        st.metric(label="مستوى A2", value="800 كلمة")
    with col2:
        st.metric(label="مستوى B1", value="4,000 كلمة")
        st.metric(label="مستوى B2", value="2,500 كلمة")
    with col3:
        st.metric(label="مستوى C1", value="8,000 كلمة")
        st.metric(label="مستوى C2", value="5,000 كلمة")

