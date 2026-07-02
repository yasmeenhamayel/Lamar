import streamlit as st
import random
import os
import base64

st.set_page_config(page_title="HBD Lamar 🎂", page_icon="🎈", layout="centered")

base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, "collage.jpg")
final_image_path = os.path.join(base_path, "final_photo.png")
audio_path = os.path.join(base_path, "HBD.mp3")

# ---------- CSS + JS ----------
st.markdown("""
<style>
.stApp { background-color: #FFEAF3; }

.center-screen {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.circle-btn button {
    border-radius: 50% !important;
    background-color: #FF3D8A !important;
    color: white !important;
    border: none !important;
    font-weight: bold;
    box-shadow: 0px 15px 30px rgba(255,61,138,0.4);
    transition: transform 0.25s ease;
}

/* class التكبير الحقيقي */
.circle-btn button.pop {
    transform: scale(1.25);
}

/* ===== Regular buttons: bigger + prominent ===== */
div.stButton > button {
    background: linear-gradient(90deg, #FF3D8A, #FF7EB3);
    color: white;
    font-size: 26px;
    font-weight: bold;
    border: none;
    border-radius: 50px;
    padding: 1rem 2.5rem;
    width: 100%;
    box-shadow: 0 6px 18px rgba(255,61,138,0.45);
    transition: all 0.25s ease-in-out;
}

div.stButton > button:hover {
    transform: translateY(-4px) scale(1.03);
    box-shadow: 0 10px 24px rgba(255,61,138,0.6);
    background: linear-gradient(90deg, #FF7EB3, #FF3D8A);
    cursor: pointer;
}

div.stButton > button:active {
    transform: translateY(0) scale(0.98);
}
</style>

<script>
document.addEventListener("click", function(e) {
    if (e.target.tagName === "BUTTON") {
        e.target.classList.add("pop");
    }
});
</script>
""", unsafe_allow_html=True)

# ---------- State ----------
if "stage" not in st.session_state: st.session_state.stage = 1
if "btn_count" not in st.session_state: st.session_state.btn_count = 0
if "confirm" not in st.session_state: st.session_state.confirm = 0

# ---------- STAGE 1 ----------
if st.session_state.stage == 1:
    st.markdown(
        "<h2 style='text-align:center;color:#D6337A;position:fixed;top:15%;width:100%'>"
        "بتعرفو شو فيه اليوم؟!! 🤔</h2>",
        unsafe_allow_html=True
    )

    btns = [
        {"t": "شو؟", "s": 160},
        {"t": "معقول ما بتعرفو؟", "s": 260},
        {"t": "!!!!", "s": 400},
        {"t": "عيد ميلاد لماار!", "s": 580}
    ]
    curr = btns[st.session_state.btn_count]

    st.markdown(f"""
    <style>
    .circle-btn button {{
        width: {curr['s']}px;
        height: {curr['s']}px;
        font-size: {curr['s']/5.5}px;
    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="circle-btn center-screen">', unsafe_allow_html=True)
    if st.button(curr["t"]):
        if st.session_state.btn_count < 3:
            st.session_state.btn_count += 1
        else:
            st.session_state.stage = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- STAGE 2 ----------
elif st.session_state.stage == 2:
    st.markdown("<h1 style='text-align:center;color:#D6337A;'>🎉 IT'S LAMAR'S BIRTHDAY!! 🎉</h1>", unsafe_allow_html=True)
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)

    if st.session_state.confirm == 0:
        if st.button("أنا لمار، دخلوني! ✨"):
            st.session_state.confirm = 1
            st.rerun()
    else:
        st.error("⚠️ متأكدة انتي لمار؟")
        if st.button(" أناااااا لماااار 😂"):
            st.session_state.stage = 3
            st.rerun()

# ---------- STAGE 3 ----------
elif st.session_state.stage == 3:
    st.markdown("<h2 style='text-align:center;color:#D6337A;'>يلا نكمل! 🎈</h2>", unsafe_allow_html=True)
    if st.button("نروح للمفاجأة؟ 🥁"):
        st.session_state.stage = 4
        st.rerun()

# ---------- STAGE 4 ----------
elif st.session_state.stage == 4:
    st.balloons()
    st.balloons()
    st.markdown("<h1 style='text-align:center;color:#FF3D8A;'>🎊 HAPPY BIRTHDAY SWEETY 🎊</h1>", unsafe_allow_html=True)

    if os.path.exists(audio_path):
        with open(audio_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            st.markdown(
                f"""
                <audio id="bday-audio" autoplay controls>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                <script>
                const audio = document.getElementById("bday-audio");
                const tryPlay = audio.play();
                if (tryPlay !== undefined) {{
                    tryPlay.catch(function(error) {{
                        const note = document.createElement("p");
                        note.innerText = "🎵 اضغطي زر التشغيل فوق لسماع الأغنية 🎵";
                        note.style.textAlign = "center";
                        note.style.color = "#D6337A";
                        note.style.fontWeight = "bold";
                        note.style.fontSize = "18px";
                        audio.insertAdjacentElement("afterend", note);
                    }});
                }}
                </script>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("حطي ملف HBD.mp3 داخل المشروع 🎵")

    if os.path.exists(final_image_path):
        st.image(final_image_path, use_container_width=True)

    if st.button("إعادة 🔄"):
        st.session_state.stage = 1
        st.session_state.btn_count = 0
        st.rerun()