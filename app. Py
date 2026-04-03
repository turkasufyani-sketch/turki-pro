import streamlit as st
import google.generativeai as genai

# 1. إعدادات المتصفح والعنوان (الاسم الجديد هنا)
st.set_page_config(page_title="TURKI SUFYANI Platform", page_icon="🚀", layout="wide")

# 2. ربط الذكاء الاصطناعي (تأكد من وضع مفتاحك السري بدلاً من الجملة العربية)
API_KEY = "ضع_مفتاحك_السري_هنا"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# 3. تصميم القائمة الجانبية للتنقل
with st.sidebar:
    st.title("📂 أقسام المنصة")
    choice = st.radio("انتقل إلى:", ["🏠 الرئيسية", "🗣️ تعلم اللغات", "📚 المكتبة الرقمية", "🧠 تطوير الذات"])
    st.markdown("---")
    st.info("Developed by: TURKI SUFYANI")

# 4. محتوى الأقسام بناءً على الاختيار
if choice == "🏠 الرئيسية":
    st.title("TURKI SUFYANI Platform 🚀")
    st.subheader("مرحباً بك في منصتي المتكاملة لتطوير الذات واللغات")
    st.write("هذه المنصة هي بوابتك لتعلم الإنجليزية، الإسبانية، والبحث في علوم النفس ولغة الجسد.")

elif choice == "🗣️ تعلم اللغات":
    st.title("🗣️ مدرب اللغات الذكي (AI Tutor)")
    st.write("أنا هنا لمساعدتك في ممارسة الإنجليزية والإسبانية وتصحيح أخطائك.")
    
    # صندوق المحادثة
    user_input = st.chat_input("اكتب سؤالك أو الجملة التي تريد ترجمتها...")
    if user_input:
        with st.spinner('جاري التفكير...'):
            try:
                response = model.generate_content(user_input)
                st.markdown("### 🤖 الرد:")
                st.write(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")

elif choice == "📚 المكتبة الرقمية":
    st.title("📚 المكتبة الرقمية")
    st.write("هنا ستكون مكتبتك الخاصة بالكتب والملفات التعليمية.")
    st.info("هذا القسم قيد التطوير ليناسب احتياجاتك.")

elif choice == "🧠 تطوير الذات":
    st.title("🧠 تطوير الذات وعلم النفس")
    st.write("نصائح وتقنيات لتعزيز الثقة بالنفس وفهم لغة الجسد.")
    st.warning("قريباً: دورات تفاعلية في الشخصية والذكاء الاجتماعي.")
