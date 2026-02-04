import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine Surprise", layout="wide")

# 🎨 Global Styling
st.markdown("""
<style>
.stApp {
    background-color: #b30000;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

h1 {
    color: white !important;
    text-align: center;
}

/* Pink gradient buttons */
.stButton>button {
    background: linear-gradient(45deg, #ff4d6d, #ff85a2);
    color: white;
    font-size: 22px;
    padding: 15px 40px;
    border-radius: 30px;
    border: none;
    font-weight: bold;
    transition: 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.08);
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = 1


# ---------------- PAGE 1 ----------------
if st.session_state.page == 1:

    st.markdown(
        "<div style='margin-top:180px; text-align:center; font-size:65px; font-weight:bold;'>❤️ Happy Valentine's Day ❤️</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("Next ➡️"):
            st.session_state.page = 2
            st.rerun()


# ---------------- PAGE 2 ----------------
elif st.session_state.page == 2:

    st.markdown("<h1 style='margin-top:120px;'>Will you be my Valentine? ❤️</h1>", unsafe_allow_html=True)

    # YES button centered
    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("Yes 💖"):
            st.session_state.page = 3
            st.rerun()

    # NO button inside controlled box
    components.html(
        """
        <div style="
            position: relative;
            width: 400px;
            height: 120px;
            margin: 20px auto;
        ">

            <button id="noBtn"
                style="
                    position: absolute;
                    left: 220px;
                    top: 20px;
                    background: linear-gradient(45deg, #ff4d6d, #ff85a2);
                    color: white;
                    font-size: 22px;
                    padding: 15px 40px;
                    border: none;
                    border-radius: 30px;
                    font-weight: bold;
                    cursor: pointer;
                ">
                No 😢
            </button>

        </div>

        <script>
            const noBtn = document.getElementById("noBtn");

            document.addEventListener("mousemove", function(e) {

                const rect = noBtn.getBoundingClientRect();
                const distance = Math.hypot(
                    e.clientX - (rect.left + rect.width / 2),
                    e.clientY - (rect.top + rect.height / 2)
                );

                if (distance < 100) {

                    const moveX = (Math.random() * 120) - 60;
                    const moveY = (Math.random() * 60) - 30;

                    const currentLeft = parseFloat(noBtn.style.left);
                    const currentTop = parseFloat(noBtn.style.top);

                    let newLeft = currentLeft + moveX;
                    let newTop = currentTop + moveY;

                    // Keep inside box boundaries
                    newLeft = Math.max(0, Math.min(newLeft, 280));
                    newTop = Math.max(0, Math.min(newTop, 60));

                    noBtn.style.left = newLeft + "px";
                    noBtn.style.top = newTop + "px";
                }
            });
        </script>
        """,
        height=150,
    )


# ---------------- PAGE 3 ----------------
elif st.session_state.page == 3:

    st.markdown(
        "<div style='text-align:center; margin-top:200px;'><h1 style='font-size:70px;'>I LOVE YOU ❤️</h1></div>",
        unsafe_allow_html=True
    )

    st.image("https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif")


# in terminal run "python -m streamlit run valentine_app.py"