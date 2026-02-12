import streamlit as st
from logic.predict import predict_prakriti
from logic.recommend import recommend_herbs

st.set_page_config(page_title="Ayurveda AI", layout="centered")

st.title("🌿 Ayurveda AI – Prakriti Prediction")
st.write("Answer a few questions to know your Prakriti and suitable herbs.")

# ---------------- User Inputs ---------------- #

body_size = st.selectbox("Body Size", ["Slim", "Medium", "Large"])
body_weight = st.selectbox(
    "Body Weight",
    [
        "Light - difficulty gaining weight",
        "Moderate - no difficulties in gaining or losing weight",
        "Heavy - difficulties in losing weight"
    ]
)
bone_structure = st.selectbox(
    "Bone Structure",
    [
        "Light, Small bones, prominent joints",
        "Medium bone structure",
        "Large, broad shoulders , heavy bone structure"
    ]
)
complexion = st.selectbox(
    "Complexion",
    [
        "White, pale, tans easily",
        "Fair-skin sunburns easily",
        "Dark-Complexion, tans easily"
    ]
)
nails = st.selectbox(
    "Nails",
    [
        "Dry, Rough, Brittle, Break",
        "Soft, Pink, Smooth",
        "Strong, Oily, Thick"
    ]
)

# ---------------- Prediction ---------------- #

if st.button("🔍 Predict Prakriti"):
    user_input = {
        "Body Size": body_size,
        "Body Weight": body_weight,
        "Bone Structure": bone_structure,
        "Complexion": complexion,
        "Nails": nails
    }

    probs = predict_prakriti(user_input)

    st.subheader("🧠 Prediction Result")
    st.json(probs)

    # Determine primary dosha
    primary = max(probs, key=probs.get)
    st.success(f"**Your Dominant Prakriti: {primary}**")

    # Herb Recommendations
    st.subheader("🌿 Recommended Herbs")
    herbs = recommend_herbs(primary)

    for herb in herbs:
        st.markdown(f"**{herb['name']}**")
        st.write(herb["benefits"])
        st.divider()

    # Explanation
    st.subheader("📖 Explanation")
    st.write(
        "Based on your physical traits like nails, body structure, and complexion, "
        "the model inferred your dominant dosha. Ayurveda traditionally uses these "
        "observable characteristics to determine Prakriti."
    )
