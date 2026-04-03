import streamlit as st

st.set_page_config(page_title="تعلم اللغات", layout="wide")

# تخزين الصفحة الحالية
if "page" not in st.session_state:
    st.session_state.page = "home"

if "saved_words" not in st.session_state:
    st.session_state.saved_words = []

# ================== الصفحة الرئيسية ==================
if st.session_state.page == "home":
    st.title("🚀 تعلم اللغات")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        if st.button("📚 المكتبة"):
            st.session_state.page = "library"

    with col2:
        if st.button("🧠 المفردات"):
            st.session_state.page = "vocab"

    with col3:
        if st.button("📝 التمارين"):
            st.session_state.page = "practice"

    with col4:
        if st.button("🎯 التحدي اليومي"):
            st.session_state.page = "challenge"

# ================== المكتبة ==================
elif st.session_state.page == "library":
    st.title("📚 المكتبة")

    if st.button("⬅️ رجوع"):
        st.session_state.page = "home"

    st.subheader("The House of Hilltop")
    if st.button("اقرأ القصة 1"):
        st.session_state.page = "story1"

# ================== القصة ==================
elif st.session_state.page == "story1":
    st.title("📖 القصة")

    if st.button("⬅️ رجوع"):
        st.session_state.page = "library"

    st.write("I am amazed by this ancient house.")

    if st.button("💾 حفظ amazed"):
        st.session_state.saved_words.append(("amazed", "مندهش"))

    if st.button("💾 حفظ ancient"):
        st.session_state.saved_words.append(("ancient", "قديم"))

# ================== المفردات ==================
elif st.session_state.page == "vocab":
    st.title("🧠 المفردات")

    if st.button("⬅️ رجوع"):
        st.session_state.page = "home"

    if len(st.session_state.saved_words) == 0:
        st.write("لا توجد كلمات محفوظة")
    else:
        for word, meaning in st.session_state.saved_words:
            st.write(f"{word} = {meaning}")

    if st.button("🎯 تدرب"):
        st.session_state.page = "practice"

# ================== التمارين ==================
elif st.session_state.page == "practice":
    st.title("📝 التمارين")

    if st.button("⬅️ رجوع"):
        st.session_state.page = "home"

    question = "amazed"
    answer = st.text_input("وش معنى amazed؟")

    if st.button("تحقق"):
        if answer.strip() == "مندهش":
            st.success("صح 🔥")
        else:
            st.error("خطأ ❌")

# ================== التحدي ==================
elif st.session_state.page == "challenge":
    st.title("🎯 التحدي اليومي")

    if st.button("⬅️ رجوع"):
        st.session_state.page = "home"

    st.write("ترجم: I am happy")

    answer = st.text_input("الإجابة:")

    if st.button("تحقق"):
        if "سعيد" in answer:
            st.success("ممتاز 😎")
        else:
            st.error("حاول مرة ثانية")
