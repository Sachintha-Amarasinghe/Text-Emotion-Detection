import streamlit as st
import pandas as pd
import altair as alt
import joblib

# Load the trained model
pipe_lr = joblib.load(open("text_emotion.pkl", "rb"))

# Dictionary to map emotions to emojis
emotions_emoji_dict = {
    "anger": "😠", "disgust": "🤮", "fear": "😨😱", "happy": "🤗",
    "joy": "😂", "neutral": "😐", "sad": "😔", "sadness": "😔",
    "shame": "😳", "surprise": "😮"
}

# Function to predict emotions
def predict_emotions(docx):
    results = pipe_lr.predict([docx])
    return results[0]

# Function to get prediction probabilities
def get_prediction_proba(docx):
    results = pipe_lr.predict_proba([docx])
    return results

# Main function for Streamlit app
def main():
    st.title("Text Emotion Detection")
    st.subheader("Detect Emotions In Text")

    # Form to input text
    with st.form(key='my_form'):
        raw_text = st.text_area("Type Here")
        submit_text = st.form_submit_button(label='Submit')

    # Processing the input text
    if submit_text:
        col1, col2 = st.columns(2)

        prediction = predict_emotions(raw_text)
        probability = get_prediction_proba(raw_text)

        with col1:
            # Styling original text and prediction
            st.success("Original Text")
            st.write(raw_text)

            st.success("Prediction")
            emoji_icon = emotions_emoji_dict[prediction]
            # Applying custom style to prediction label
            styled_prediction = f'<span style="color: red; font-size: 20px;">{prediction}</span>'
            st.write(f"{styled_prediction}: {emoji_icon}", unsafe_allow_html=True)

        with col2:
            # Styling prediction probability
            st.success("Prediction Probability")
            proba_df = pd.DataFrame(probability, columns=pipe_lr.classes_)
            proba_df_clean = proba_df.T.reset_index()
            proba_df_clean.columns = ["emotions", "probability"]

            fig = alt.Chart(proba_df_clean).mark_bar().encode(x='emotions', y='probability', color='emotions')
            st.altair_chart(fig, use_container_width=True)

if __name__ == '__main__':
    main()
