import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine Surprise", layout="wide")

# ---------- GLOBAL STYLING ----------
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    margin: 0;
    padding: 0;
    background-color: #b30000;
}

.stApp {
    background-color: #b30000;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Headings */
h1 {
    text-align: center;
    color: white !important;
}

/* Romantic buttons */
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

# ---------- PAGE STATE ----------
if "page" not in st.session_state:
    st.session_state.page = 1


# ================= PAGE 1 =================
if st.session_state.page == 1:

    st.markdown("""
    <div style='margin-top:180px; font-size:65px; font-weight:bold; text-align:center;'>
        ❤️ Happy Valentine's Day ❤️
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("Next ➡️"):
            st.session_state.page = 2
            st.rerun()


# ================= PAGE 2 =================
elif st.session_state.page == 2:

    st.markdown("""
    <h1 style='margin-top:120px;'>
        Will you be my Valentine? ❤️
    </h1>
    """, unsafe_allow_html=True)

    # YES Button
    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("Yes 💖"):
            st.session_state.page = 3
            st.rerun()

    # NO Button (controlled movement box)
    components.html("""
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

                newLeft = Math.max(0, Math.min(newLeft, 280));
                newTop = Math.max(0, Math.min(newTop, 60));

                noBtn.style.left = newLeft + "px";
                noBtn.style.top = newTop + "px";
            }
        });
    </script>
    """, height=150)


# ================= PAGE 3 =================
elif st.session_state.page == 3:

    # We generate a massive string of text to fill the background
    background_text = "I LOVE YOU " * 800

    st.markdown(f"""
    <style>
    /* Hide the Streamlit header and padding to make it truly full-screen */
    header, [data-testid="stHeader"] {{
        display: none;
    }}
    
    .love-wrapper {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: #b30000;
        overflow: hidden;
        z-index: 9999; /* Put it on top of everything */
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .love-pattern {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        font-size: 24px;
        font-weight: bold;
        color: rgba(255, 255, 255, 0.1); /* Faint white background text */
        line-height: 1.4;
        text-align: justify;
        padding: 10px;
        pointer-events: none;
        word-wrap: break-word;
    }}

    .love-main {{
        position: relative;
        font-size: 100px;
        font-weight: 900;
        color: white;
        text-align: center;
        z-index: 10001;
        text-shadow: 0px 0px 20px rgba(0,0,0,0.5);
        animation: pulse 1.5s infinite;
    }}

    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
        100% {{ transform: scale(1); }}
    }}
    </style>

    <div class="love-wrapper">
        <div class="love-pattern">
            {background_text}
        </div>
        <div class="love-main">
            I LOVE YOU ❤️
        </div>
    </div>
    """, unsafe_allow_html=True)
