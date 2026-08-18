import streamlit as st
import joblib
model = joblib.load("Multinomial_Naive_Bayes_spam.pkl")
bow = joblib.load("bow_vectorizer.pkl")
st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📱"
)
st.title("📱 SMS Spam Detector")
st.write("Enter an SMS below to check whether it is **Spam** or **Not Spam**.")
sms = st.text_area(
    "Enter your message:",
    placeholder="Example: Congratulations! You have won a free prize!"
)
if st.button("Check SMS"):
    if sms.strip() == "":
        st.warning("Please enter an SMS first.")
    else:
        sms_bow = bow.transform([sms])
        prediction = model.predict(sms_bow)[0]
        if prediction == 1:
            st.error("🚨 This SMS is SPAM!")
        else:
            st.success("✅ This SMS is NOT SPAM.")