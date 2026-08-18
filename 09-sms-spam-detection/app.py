import streamlit as st
import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download("punkt_tab")
nltk.download("stopwords")
model = joblib.load("Multinomial_Naive_Bayes_spam.pkl")
bow = joblib.load("bow_vectorizer.pkl")
stop_words = set(stopwords.words("english"))
def clean_text(txt):
    txt = txt.lower()
    words = word_tokenize(txt)
    cleaned = []
    for word in words:
        if word not in stop_words:
            cleaned.append(word)
    return " ".join(cleaned)
st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📱"
)
st.title("📱 SMS Spam Detector")
st.write("Enter an SMS to check whether it is Spam or Not Spam.")
sms = st.text_area(
    "Enter your message:",
    placeholder="Congratulations! You have won a free prize!"
)
if st.button("Check SMS"):
    if sms.strip() == "":
        st.warning("Please enter an SMS first.")
    else:
        cleaned_sms = clean_text(sms)
        sms_bow = bow.transform([cleaned_sms])
        prediction = model.predict(sms_bow)[0]
        if prediction == 1:
            st.error("🚨 This SMS is SPAM!")
        else:
            st.success("✅ This SMS is NOT SPAM.")